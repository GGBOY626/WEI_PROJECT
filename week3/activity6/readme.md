Yoobee Colleges - Week 3 – Activity 6
Command-Line Application with SQLite3


1. Overview

Project scope
This database supports the records of YB College. 
It save information about students, teachers, and programs, 
and manages the relationships between them. 
The goal is to maintain clean records of who studies in which program 
and which teachers supervise which students.

Story
when new student join our school, 
our personal information and major will be save in the database. 
And the information of teachers also will be saved. Program describe a study field. 
For example software engineer. 
The database also save the relate in teacher and student for the study.

- Program
- Student
- Teacher
- Teacher-Program (M:N relation)
- Teacher-Student (M:N relation)

Core features:
- Add records
- View records
- Delete records

2. Tech Stack
- Python 3.x (standard library only)
- sqlite3 (built-in)
- No external dependencies required

3. Project Structure
.
├─ main.py                # Main entry point (menus)
├─ database.py           # create Database table and connect
├─ README.txt            # This file
└─ school_manager.db     # CRUD method

4. Database Design (SQLite)
Tables:
- program(id, name, code, create_time, update_time, del_time)
- student(id, student_id, name, gender, nationality, email, program_id(FK->program.id), birth_date, create_time, update_time, del_time)
- teacher(id, name, email, create_time, update_time, del_time)
- teacher_program(teacher_id(FK), program_id(FK), role, create_time, update_time, del_time)   -- M:N
- teacher_student_table(student_id(FK), teacher_id(FK), create_time, update_time, del_time)    -- M:N

Notes:
- PRAGMA foreign_keys = ON (enforced)
- All time fields are using SQLite function: datetime('now')

5. How to Run
$ python main.py

Main Menu:
 1) Add student
 2) View students
 3) Add program
 4) View programs
 5) Add teacher
 6) View teachers
 7) Link student <-> teacher (M:N)
 8) View student-teacher links
 9) Link teacher <-> program (M:N)
10) View teacher-program links
11) Update a student
12) Delete a student
13) Update a teacher
14) Delete a teacher
15) Update a program
16) Delete a program
17) Exit

6. Sample Usage
- Add a program (3), then add a teacher (5), then link them (9).
- Add a student (1), assign program_id if needed, link student-teacher (7).
- View lists via options (2/4/6/8/10).
- Delete program (12/14/16). must clear all student link first(delete student of program first).

7. Error Handling & Data Integrity
- Foreign keys enabled via PRAGMA.
- Integrity/Operational errors are caught and displayed.
- Basic input validation: converts numeric PKs with helper function.


