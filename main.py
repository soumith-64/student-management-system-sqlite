from database.database import initialize_database,add_student_db
from time import sleep
initialize_database()

def main_menu():

    opt={1,2}
    
    while True:

        print("========================================================================")
        print("                      STUDENT MANAGEMENT SYSTEM                         ")
        print("========================================================================\n")
    
        print("To Add Student Press - 1")
        print("To Exit Press - 2")

        try:
            user_choice=int(input("Your Choice :"))
        except ValueError:
            print("Please enter only the given number")
            print("Try again...")
            continue

        if user_choice in opt:

            if user_choice == 1:
                add_students()
            elif user_choice == 2:
                print("Thank You")
                print("Waiting to manage your students again")
                print("Exiting....")
                sleep(.7)
                break
        else:
            print("Enter only the given options")

def total_mark(py,math,eng):
    opt={1,2}
    totalmark = py + math + eng
    if totalmark == 0:
        print("Are you sure the student total is zero(0)\n")
        print("If yes press -- 1 else press -- 2 \n")
        while True:
            try:
                con_inp = int(input("Yes--1 or no--2 : "))
                print("")
                if con_inp == 1:
                    return totalmark
                elif con_inp == 2:
                    return None
                else:
                    print("Please choose either 1 or 2.")
            except ValueError:
                print("Please enter only numbers")
    return totalmark

def average_mark(total):

    if total == 0:
        return 0.0
    else:
        avgmark=round(total/3,2)
        return avgmark

def cal_grade(avg):

    if avg >= 95:
        grade = "A+"
    elif 80 <= avg < 95:
        grade = "A"
    elif 70 <= avg < 80:
        grade = "B"
    elif 60 <= avg < 70:
        grade = "C"
    elif 50 <= avg < 60:
        grade = "D"
    elif avg < 50:
        grade = "F"

    return grade

def cal_status(py,math,eng):

    if py<35 or math<35 or eng<35:
        s="Fail"
    else:
        s="Pass"
    
    return s

def get_input():

    rollnum = input("Enter Roll Number : ").strip()
    print("")
    name = input("Enter Name : ").strip()
    print("")
    dob = input("Enter DateOfBirth : ").strip()
    print("")
    department = input("Enter Department Name : ").strip()
    print("")
    
    while True:
        try:
            year = int(input("Enter Year : "))
            print("")
            break
        except ValueError:
            print("❌ Invalid input! Please enter a numeric year.")
            
    section = input("Enter Section : ").strip()
    print("")
    father_name = input("Enter Father Name : ").strip()
    print("")
    mother_name = input("Enter Mother Name : ").strip()
    print("")
    parent_phone = input("Enter Parent Phone Number : ").strip()
    print("")
    email = input("Enter Email : ").strip()
    print("")
    
    while True:
        try:
            python_marks = float(input("Enter Python Mark : "))
            print("")
            math_marks = float(input("Enter Math Mark : "))
            print("")
            english_marks = float(input("Enter English Mark : "))
            print("")
            
            total = total_mark(python_marks, math_marks, english_marks)
            if total is not None:
                break
            else:
                print("Re-enter target marks.\n")
        except ValueError:
            print("❌ Invalid input! Marks must be valid numbers.")

    avg = average_mark(total)
    grade = cal_grade(avg)
    status = cal_status(python_marks, math_marks, english_marks)
    
    return (rollnum, name, dob, department, year, section, father_name, 
            mother_name, parent_phone, email, python_marks, math_marks, 
            english_marks, total, avg, grade, status)

def add_students():
    (roll_no, name, dob, department, year, section, father_name, mother_name, 
     parent_phone, email, python_marks, math_marks, english_marks, total, 
     average, grade, status) = get_input()
     
    add_student_db(roll_no, name, dob, department, year, section, father_name, 
                   mother_name, parent_phone, email, python_marks, math_marks, 
                   english_marks, total, average, grade, status)
    print("🎉 Student added successfully to the database!\n")
main_menu()