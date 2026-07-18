import sqlite3
from config import DATABASE_PATH

def create_connection():
    connection=sqlite3.connect(DATABASE_PATH)
    return connection

def create_table(connection):
    cursor=connection.cursor()
    cursor.execute( """

        CREATE TABLE IF NOT EXISTS student(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        roll_no TEXT UNIQUE NOT NULL,
        name TEXT NOT NULL,
        dob TEXT NOT NULL,
        department TEXT NOT NULL,
        year INTEGER NOT NULL,
        section TEXT NOT NULL,
        father_name TEXT,
        mother_name TEXT,
        parent_phone TEXT,
        email TEXT,
        python_marks REAL DEFAULT 0,
        math_marks REAL DEFAULT 0,
        english_marks REAL DEFAULT 0,
        total REAL DEFAULT 0,
        average REAL DEFAULT 0,
        grade TEXT DEFAULT 'N/A',
        status TEXT DEFAULT 'Pending',
        created_at TEXT DEFAULT CURRENT_TIMESTAMP )

    """
    )
    connection.commit()
    cursor.close()

def add_student_db(roll_no,name,dob,department,year,section,father_name,mother_name,parent_phone,email,python_marks,math_marks,english_marks,total,average,grade,status):
    connection = create_connection()
    cursor=connection.cursor()
    
    cursor.execute("""

        INSERT INTO student(roll_no,name,dob,department,year,section,father_name,mother_name,parent_phone,email,python_marks,math_marks,english_marks,total,average,grade,status)
        VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)""" ,
        (roll_no,name,dob,department,year,section,father_name,mother_name,parent_phone,email,python_marks,math_marks,english_marks,total,average,grade,status))
    connection.commit()
    cursor.close()
    connection.close()
    
def initialize_database():
    connection=create_connection()
    create_table(connection)
    connection.close()