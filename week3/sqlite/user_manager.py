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
        finally:
            conn.close()
    return wrapper

@with_db
def add_user(cursor,name, email):
    try:
        cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))
        print(" User added successfully.")
    except sqlite3.IntegrityError:
        print(" Email must be unique.")

@with_db
def view_users(cursor):
    cursor.execute("SELECT * FROM users")
    return cursor.fetchall()

@with_db
def search_user(cursor, name):
    cursor.execute("SELECT * FROM users WHERE name LIKE ?", ('%' + name + '%',))
    return cursor.fetchall()

@with_db
def delete_user(cursor, user_id):
    cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
    print("🗑️ User deleted.")

@with_db
def add_stu(cursor, stu_name, stu_address):
    cursor.execute("INSERT INTO students (stu_name, stu_address) VALUES (?, ?)", (stu_name, stu_address))
    print("students added successfully.")

@with_db
def view_stu(cursor):
    cursor.execute("SELECT * FROM students")
    return cursor.fetchall()

@with_db
def search_stu(cursor, stu_name):
    cursor.execute("SELECT * FROM students WHERE stu_name LIKE ?", ('%' + stu_name + '%',))
    return cursor.fetchall()

@with_db
def delete_stu(cursor, stu_id):
    cursor.execute("DELETE FROM students WHERE stu_id = ?", (stu_id,))
    print("🗑️ Student deleted.")