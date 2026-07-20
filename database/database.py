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

def view_std():
    connection = create_connection()
    cursor=connection.cursor()
    cursor.execute("""
            SELECT * FROM student;
    """
    )
    data=cursor.fetchall()
    cursor.close()
    connection.close()
    return data

def get_std(rollnum):
    connection = create_connection()
    cursor=connection.cursor()
    cursor.execute("""

        SELECT * FROM student WHERE roll_no = ?""",
        (rollnum,)
        
        )
    std_data=cursor.fetchone()
    cursor.close()
    connection.close()
    return std_data

def update_student_db(oldroll,roll_no,name,dob,department,year,section,father_name,mother_name,parent_phone,email,python_marks,math_marks,english_marks,total,average,grade,status):
    connection=create_connection()
    cursor=connection.cursor()

    cursor.execute("""
            UPDATE student  
            SET 
                    roll_no = ?,
                    name = ?,
                    dob = ?,
                    department = ?,
                    year = ?,
                    section = ?,
                    father_name = ?,
                    mother_name = ?,
                    parent_phone = ?,
                    email = ?,
                    python_marks = ?,
                    math_marks = ?,
                    english_marks = ?,
                    total = ?,
                    average = ?,
                    grade = ?,
                    status = ?
            WHERE roll_no=?""",
            (roll_no,name,dob,department,year,section,father_name,mother_name,parent_phone,email,python_marks,math_marks,english_marks,total,average,grade,status,oldroll,)
        )

    connection.commit()
    cursor.close()
    connection.close()

def delete_std_db(rollnum):
    connection=create_connection()
    cursor=connection.cursor()
    cursor.execute("""

    DELETE FROM student WHERE roll_no = ?""",
    (rollnum,)
    )
    connection.commit()
    cursor.close()
    connection.close()  


def statistics_db():
    connection = create_connection()
    cursor = connection.cursor()
    
    cursor.execute(""" 
        SELECT COUNT(*), MAX(average), MIN(average), AVG(average) 
        FROM student 
    """)
    cmma = cursor.fetchone()
    
    if not cmma or cmma[0] == 0:
        cursor.close()
        connection.close()
        return (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

    total, max_avg, min_avg, avg_avg = cmma

    cursor.execute("""
        SELECT 
            COUNT(CASE WHEN status = 'Pass' THEN 1 END),
            COUNT(CASE WHEN status = 'Fail' THEN 1 END),
            COUNT(CASE WHEN grade = 'A+' THEN 1 END),
            COUNT(CASE WHEN grade = 'A' THEN 1 END),
            COUNT(CASE WHEN grade = 'B' THEN 1 END),
            COUNT(CASE WHEN grade = 'C' THEN 1 END),
            COUNT(CASE WHEN grade = 'D' THEN 1 END),
            COUNT(CASE WHEN grade = 'F' THEN 1 END)
        FROM student
    """)
    counts = cursor.fetchone()
    
    cursor.close()
    connection.close()

    t_pass, t_fail, g_ap, g_a, g_b, g_c, g_d, g_f = counts

    return (total, round(max_avg, 2), round(min_avg, 2), round(avg_avg, 2),t_pass, t_fail, g_ap, g_a, g_b, g_c, g_d, g_f )
    
def search_std_db(opt,val):
    connection = create_connection()
    cursor = connection.cursor()

    result=[]

    columns = {
        1:"roll_no",
        2:"name",
        3:"department",
        4:"year",
    }

    col = columns.get(opt)

    if not col:
        cursor.close()
        connection.close()
        result = None
        return result

    if opt == 2:
        query = f"SELECT * FROM student WHERE {col} LIKE ?" 
        param = (f"%{val}%",)
    elif opt == 3:
        query = f"SELECT * FROM student WHERE {col} LIKE ?" 
        param = (f"%{val}%",)
    else:
        query = f"SELECT * FROM student WHERE {col} = ?"
        param = (val,)

    cursor.execute(query,param)
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    return result


def initialize_database():
    connection=create_connection()
    create_table(connection)
    connection.close()