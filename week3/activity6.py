from pymysql import Connection

class YooBeeDatabase:
    def __init__(self, host='localhost', port=3306, user='root', password='Yoobee@2025!', db='test'):
        self.conn = Connection(
            host=host,
            port=port,
            user=user,
            password=password
        )
        self.conn.select_db(db)
        self.cursor = self.conn.cursor()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is None:
            self.conn.commit()
        else:
            self.conn.rollback()
        self.cursor.close()
        self.conn.close()

    def execute(self, sql, params=None):
        # insert, update, delete
        self.cursor.execute(sql, params or ())
        return self.cursor.rowcount

    def fetch_all(self, sql, params=None):
        # select all data
        self.cursor.execute(sql, params or ())
        return self.cursor.fetchall()

    def fetch_one(self, sql, params=None):
        # select one data
        self.cursor.execute(sql, params or ())
        return self.cursor.fetchone()

    # program
    def add_program(self, name, code):
        return self.execute("INSERT INTO program(name, code) VALUES (%s, %s)", (name, code))

    def get_programs(self):
        return self.fetch_all("SELECT id, name, code FROM program")

    def update_program(self, program_id, name=None, code=None):
        return self.execute("UPDATE program SET name=%s, code=%s WHERE id=%s", (name, code, program_id))

    def delete_program(self, program_id):
        return self.execute("DELETE FROM program WHERE id=%s", (program_id,))

    # student
    def add_student(self, student_id, name, gender, nationality, email, program_id, birth_date):
        return self.execute("""
            INSERT INTO student(student_id, name, gender, nationality, email, program_id, birth_date)
            VALUES (%s,%s,%s,%s,%s,%s,%s)
        """, (student_id, name, gender, nationality, email, program_id, birth_date))

    def get_students(self):
        return self.fetch_all("SELECT id, student_id, name, gender, nationality, email FROM student")

    def update_student(self, student_id, name=None, email=None):
        return self.execute("UPDATE student SET name=%s, email=%s WHERE student_id=%s", (name, email, student_id))

    def delete_student(self, student_id):
        return self.execute("DELETE FROM student WHERE student_id=%s", (student_id,))

    # teacher
    def add_teacher(self, name, email, program_id):
        return self.execute("INSERT INTO teacher(name, email, program_id) VALUES (%s,%s,%s)", (name, email, program_id))

    def get_teachers(self):
        return self.fetch_all("SELECT id, name, email FROM teacher")

    def update_teacher(self, teacher_id, name=None, email=None):
        return self.execute("UPDATE teacher SET name=%s, email=%s WHERE id=%s", (name, email, teacher_id))

    def delete_teacher(self, teacher_id):
        return self.execute("DELETE FROM teacher WHERE id=%s", (teacher_id,))

    # teacher_student_table
    def add_teacher_student(self, student_id, teacher_id):
        return self.execute("INSERT INTO teacher_student_table(student_id, teacher_id) VALUES (%s,%s)", (student_id, teacher_id))

    def get_teacher_students(self):
        return self.fetch_all("SELECT student_id, teacher_id FROM teacher_student_table")

    def delete_teacher_student(self, student_id, teacher_id):
        return self.execute("DELETE FROM teacher_student_table WHERE student_id=%s AND teacher_id=%s", (student_id, teacher_id))

if __name__ == "__main__":
    with YooBeeDatabase() as db:
        # db.add_program("Computer Science", "CS")
        # print("Programs:", db.get_programs())

        # student
        # db.add_student("CS", "Ray2", "FEMALE", "NZ", "ray@test.com", 2, "2000-01-01")
        # print("Students:", db.get_students())
        #
        # # teacher
        # db.add_teacher("TOM", "tom@test.com", 2)
        # print("Teachers:", db.get_teachers())
        # #
        # # # teacher_student_table
        db.add_teacher_student(4, 3)
        print("Teacher-Student Links:", db.get_teacher_students())
