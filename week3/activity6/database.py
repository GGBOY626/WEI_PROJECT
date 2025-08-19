import sqlite3
DDL = """
PRAGMA foreign_keys = ON;

-- program
CREATE TABLE IF NOT EXISTS program (
  id           INTEGER PRIMARY KEY AUTOINCREMENT,
  name         TEXT NOT NULL,
  code         TEXT NOT NULL,
  update_time  TEXT,
  create_time  TEXT,
  del_time     TEXT
);

-- student
CREATE TABLE IF NOT EXISTS student (
  id           INTEGER PRIMARY KEY AUTOINCREMENT,
  student_id   TEXT NOT NULL UNIQUE,
  name         TEXT NOT NULL,
  gender       TEXT,
  nationality  TEXT,
  email        TEXT,
  program_id   INTEGER REFERENCES program(id) ON DELETE RESTRICT,
  birth_date   TEXT,
  update_time  TEXT,
  create_time  TEXT,
  del_time     TEXT
);
CREATE INDEX IF NOT EXISTS idx_student_program_id ON student(program_id);

-- teacher
CREATE TABLE IF NOT EXISTS teacher (
  id           INTEGER PRIMARY KEY AUTOINCREMENT,
  name         TEXT NOT NULL,
  email        TEXT,
  update_time  TEXT,
  create_time  TEXT,
  del_time     TEXT
);

-- teacher_program
CREATE TABLE IF NOT EXISTS teacher_program (
  teacher_id   INTEGER NOT NULL,
  program_id   INTEGER NOT NULL,
  role         TEXT,
  create_time  TEXT,
  update_time  TEXT,
  del_time     TEXT,
  PRIMARY KEY (teacher_id, program_id),
  FOREIGN KEY (teacher_id) REFERENCES teacher(id) ON DELETE CASCADE,
  FOREIGN KEY (program_id) REFERENCES program(id) ON DELETE CASCADE
);
CREATE INDEX IF NOT EXISTS idx_tp_program ON teacher_program(program_id);
CREATE INDEX IF NOT EXISTS idx_tp_teacher ON teacher_program(teacher_id);

-- teacher_student_table
CREATE TABLE IF NOT EXISTS teacher_student_table (
  student_id   INTEGER NOT NULL,
  teacher_id   INTEGER NOT NULL,
  update_time  TEXT,
  create_time  TEXT,
  del_time     TEXT,
  PRIMARY KEY (student_id, teacher_id),
  FOREIGN KEY (student_id) REFERENCES student(id) ON DELETE CASCADE,
  FOREIGN KEY (teacher_id) REFERENCES teacher(id) ON DELETE CASCADE
);
CREATE INDEX IF NOT EXISTS idx_ts_teacher ON teacher_student_table(teacher_id);

"""
def create_connection():
    conn = sqlite3.connect("users.db")
    return conn

def create_tables():
    with create_connection() as conn:
        conn.executescript(DDL)
