from functools import wraps

from database import create_connection
import sqlite3


def with_db(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        conn = create_connection()
        cursor = conn.cursor()
        try:
            result = func(cursor, *args, **kwargs)
            if cursor.connection.in_transaction:
                conn.commit()
            return result
        except sqlite3.Error as e:
            print(f"[DBError] {e}")
        finally:
            conn.close()
    return wrapper


def to_int_or_none(s: str):
    s = (s or "").strip()
    if not s:
        return None
    try:
        return int(s)
    except ValueError:
        return None

def now_expr():
    return "datetime('now')"

# -------------------------
# STUDENT CRUD
# -------------------------
@with_db
def add_stu(cursor, student_id, name, gender, nationality, email, program_id, birth_date):
    prog_id_int = to_int_or_none(program_id)
    cursor.execute(
        f"""
        INSERT INTO student (student_id, name, gender, nationality, email, program_id, birth_date, create_time, update_time)
        VALUES (?, ?, ?, ?, ?, ?, ?, {now_expr()}, {now_expr()})
        """,
        (student_id, name, gender, nationality, email, prog_id_int, birth_date)
    )
    print("[OK] Student created.")

@with_db
def view_stu(cursor):
    """Return all students."""
    cursor.execute(""" SELECT * FROM student """)
    return cursor.fetchall()

@with_db
def update_stu(cursor, student_pk, **fields):
    """
    Update a student by PK (id).
    Only provided fields will be updated; also refresh update_time = now().
    """
    allowed = {"student_id","name","gender","nationality","email","program_id","birth_date","del_time"}
    sets = []
    params = []
    for k, v in fields.items():
        if k in allowed:
            sets.append(f"{k} = ?")
            params.append(v if k != "program_id" else to_int_or_none(v))
    if not sets:
        print("[WARN] Nothing to update.")
        return
    sets.append(f"update_time = {now_expr()}")
    sql = f"UPDATE student SET {', '.join(sets)} WHERE id = ?"
    params.append(student_pk)
    cursor.execute(sql, params)
    if cursor.rowcount:
        print("[OK] Student updated.")
    else:
        print("[INFO] Student not found.")

@with_db
def delete_stu(cursor, student_pk):
    """Delete a student by PK (id). teacher_student_table will delete auto in sqlite."""
    cursor.execute("DELETE FROM student WHERE id = ?", (student_pk,))
    if cursor.rowcount:
        print("[OK] Student deleted.")
    else:
        print("[INFO] Student not found.")

# -------------------------
# PROGRAM CRUD
# -------------------------
@with_db
def add_program(cursor, name, code):
    cursor.execute(
        f"INSERT INTO program (name, code, create_time, update_time) VALUES (?, ?, {now_expr()}, {now_expr()})",
        (name, code)
    )
    print("[OK] Program created.")

@with_db
def view_programs(cursor):
    cursor.execute(""" SELECT * FROM program """)
    return cursor.fetchall()
@with_db
def update_program(cursor, program_pk, **fields):
    """Update a program by PK (id). Only provided fields will be updated; refresh update_time."""
    allowed = {"name", "code", "del_time"}
    sets, params = [], []
    for k, v in fields.items():
        if k in allowed:
            sets.append(f"{k} = ?")
            params.append(v)
    if not sets:
        print("[WARN] Nothing to update.")
        return
    sets.append("update_time = datetime('now')")
    sql = f"UPDATE program SET {', '.join(sets)} WHERE id = ?"
    params.append(program_pk)
    cursor.execute(sql, params)
    if cursor.rowcount:
        print("[OK] Program updated.")
    else:
        print("[INFO] Program not found.")

@with_db
def delete_program(cursor, program_pk):
    """
    Delete a program by PK (id).
    if student exist,can not delete
    teacher_program table will delete auto
    """
    try:
        cursor.execute("DELETE FROM program WHERE id = ?", (program_pk,))
        if cursor.rowcount:
            print("[OK] Program deleted.")
        else:
            print("[INFO] Program not found.")
    except sqlite3.IntegrityError as e:
        # if student exist,can not delete
        print(f"[IntegrityError] Cannot delete program {program_pk}: {e}")
        print("Hint: Reassign or remove students/teachers referencing this program first.")

# -------------------------
# TEACHER CRUD
# -------------------------
@with_db
def add_teacher(cursor, name, email):
    cursor.execute(
        f"INSERT INTO teacher (name, email, create_time, update_time) VALUES (?, ?, {now_expr()}, {now_expr()})",
        (name, email)
    )
    print("[OK] Teacher created.")

@with_db
def view_teachers(cursor):
    cursor.execute(""" SELECT * FROM teacher """)
    return cursor.fetchall()

@with_db
def update_teacher(cursor, teacher_pk, **fields):
    """Update a teacher by PK (id). Only provided fields will be updated; refresh update_time."""
    allowed = {"name", "email", "del_time"}
    sets, params = [], []
    for k, v in fields.items():
        if k in allowed:
            sets.append(f"{k} = ?")
            params.append(v)
    if not sets:
        print("[WARN] Nothing to update.")
        return
    sets.append("update_time = datetime('now')")
    sql = f"UPDATE teacher SET {', '.join(sets)} WHERE id = ?"
    params.append(teacher_pk)
    cursor.execute(sql, params)
    if cursor.rowcount:
        print("[OK] Teacher updated.")
    else:
        print("[INFO] Teacher not found.")

@with_db
def delete_teacher(cursor, teacher_pk):
    """
    Delete a teacher by PK (id).teacher_program table will delete auto in sqlite.
    """
    cursor.execute("DELETE FROM teacher WHERE id = ?", (teacher_pk,))
    if cursor.rowcount:
        print("[OK] Teacher deleted.")
    else:
        print("[INFO] Teacher not found.")

# -------------------------
# RELATION: teacher <-> program (M:N)
# -------------------------
@with_db
def add_teacher_program(cursor, teacher_id, program_id, role=None):
    t_id = to_int_or_none(teacher_id)
    p_id = to_int_or_none(program_id)
    cursor.execute(
        f"""
        INSERT INTO teacher_program (teacher_id, program_id, role, create_time, update_time)
        VALUES (?, ?, ?, {now_expr()}, {now_expr()})
        """,
        (t_id, p_id, role)
    )
    print("[OK] Linked teacher to program.")

@with_db
def view_teacher_program(cursor):
    cursor.execute(""" SELECT * FROM teacher_program """)
    return cursor.fetchall()

# -------------------------
# RELATION: teacher <-> student (M:N)
# -------------------------
@with_db
def add_student_teacher(cursor, student_id, teacher_id):
    s_id = to_int_or_none(student_id)
    t_id = to_int_or_none(teacher_id)
    cursor.execute(
        f"""
        INSERT INTO teacher_student_table (student_id, teacher_id, create_time, update_time)
        VALUES (?, ?, {now_expr()}, {now_expr()})
        """,
        (s_id, t_id)
    )
    print("[OK] add student to teacher.")

@with_db
def view_student_teacher(cursor):
    cursor.execute(""" SELECT * FROM teacher_student_table """)
    return cursor.fetchall()


