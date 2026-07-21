from database.database import initialize_database,add_student_db,view_std,get_std,update_student_db,delete_std_db,statistics_db,search_std_db
from utils.validator import (
    validate_marks,
    validate_year,
    validate_phone,
    validate_email,
    validate_roll_no,
    validate_name,
    validate_department,
    validate_section,
    validate_dob
)
from utils.helpers import (get_valid_input,get_valid_updt_input)
from time import sleep
initialize_database()

def main_menu():

    opt={1,2,3,4,5,6,7}
    
    while True:

        print("========================================================================")
        print("                      STUDENT MANAGEMENT SYSTEM                         ")
        print("========================================================================\n")
    
        print("To Add Student Press - 1")
        print("To View All Students Press - 2")
        print("To Update Student Info Press - 3")
        print("To Search Student Info Press - 4")
        print("To Delete Student Info Press - 5")
        print("To View Statistics press - 6")
        print("To Exit Press - 7")
        print("")

        try:
            user_choice=int(input("Your Choice :"))
            print("")
        except ValueError:
            print("Please enter only the given number")
            print("Try again...")
            continue

        if user_choice in opt:

            if user_choice == 1:
                add_students()
            elif user_choice == 2:
                get_all_students()
            elif user_choice == 3:
                update_student_info()
            elif user_choice == 4:
                search_std()
            elif user_choice == 5:
                delete_student()
            elif user_choice == 6:
                std_statistcs()
            elif user_choice == 7:
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

    rollnum = get_valid_input("Enter Roll Number : ",validate_roll_no, str)
    print("")
    name = get_valid_input("Enter Name : ", validate_name, str)
    print("")
    dob = get_valid_input("Enter DateOfBirth : ", validate_dob, str)
    print("")
    department = get_valid_input("Enter Department Name : ", validate_department, str)
    print("")
    year = get_valid_input("Enter Year : ", validate_year, int)
    print("")
    section = get_valid_input("Enter Section : ", validate_section, str)
    print("")

    father_name = get_valid_input("Enter Father Name : ", validate_name, str)
    print("")
    mother_name = get_valid_input("Enter Mother Name : ", validate_name, str)
    print("")
    parent_phone = get_valid_input("Enter Parent Phone Number : ", validate_phone, str)
    print("")
    email = get_valid_input("Enter Email : ", validate_email, str)
    print("")

    python_marks = get_valid_input("Enter Python Mark : ", validate_marks, float)
    print("")
    math_marks = get_valid_input("Enter Math Mark : ", validate_marks, float)
    print("")
    english_marks = get_valid_input("Enter English Mark : ", validate_marks, float)
    print("")
    
            
    total = total_mark(python_marks, math_marks, english_marks)
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


def display_student_info(student_detail):
    
    if not student_detail:
        print("📂 No student records found.\n")
        return
        
    else:    
        print("========================================================================")
        print("                            STUDENT DETAIL                              ")
        print("========================================================================\n")

        (id,roll_no, name, dob, department, year, section, father_name, mother_name, 
        parent_phone, email, python_marks, math_marks, english_marks, total, 
        average, grade, status,created_at) = student_detail

        print("")
        print("------------------------------------------------------------------------")
        print(f" Roll Number : {roll_no}")
        print("------------------------------------------------------------------------")
        print(f" Name : {name}")
        print("------------------------------------------------------------------------")
        print(f" Date Of Birth : {dob}")
        print("------------------------------------------------------------------------")
        print(f" Department : {department}")
        print("------------------------------------------------------------------------")
        print(f" Year : {year}")
        print("------------------------------------------------------------------------")
        print(f" Section : {section}")
        print("------------------------------------------------------------------------")
        print(f" Father Name : {father_name}")
        print("------------------------------------------------------------------------")
        print(f" Mother Name : {mother_name}")
        print("------------------------------------------------------------------------")
        print(f" Parents Phone number : {parent_phone}")
        print("------------------------------------------------------------------------")
        print(f" Email : {email}")
        print("------------------------------------------------------------------------")
        print(f" Python Marks : {python_marks}")
        print("------------------------------------------------------------------------")
        print(f" Math Mark : {math_marks}")
        print("------------------------------------------------------------------------")
        print(f" English Mark : {english_marks}")
        print("------------------------------------------------------------------------")
        print(f" Total : {total}")
        print("------------------------------------------------------------------------")
        print(f" Average : {average}")
        print("------------------------------------------------------------------------")
        print(f" Grade : {grade}")
        print("------------------------------------------------------------------------")
        print(f" Status : {status}")
        print("------------------------------------------------------------------------\n")
        print("")


def get_all_students():
    
    students_list = view_std() 
    
    if not students_list:
        print("📂 No student records found.\n")
        return
        
    print("========================================================================")
    print("                            STUDENTS VIEWER                             ")
    print("========================================================================\n")
    print("")
    for val in students_list: 

        (id,roll_no, name, dob, department, year, section, father_name, mother_name, 
        parent_phone, email, python_marks, math_marks, english_marks, total, 
        average, grade, status,created_at) = val

        print("========================================================================\n")
        print("------------------------------------------------------------------------")
        print(f" Roll Number : {roll_no}")
        print("------------------------------------------------------------------------")
        print(f" Name : {name}")
        print("------------------------------------------------------------------------")
        print(f" Date Of Birth : {dob}")
        print("------------------------------------------------------------------------")
        print(f" Department : {department}")
        print("------------------------------------------------------------------------")
        print(f" Year : {year}")
        print("------------------------------------------------------------------------")
        print(f" Section : {section}")
        print("------------------------------------------------------------------------")
        print(f" Father Name : {father_name}")
        print("------------------------------------------------------------------------")
        print(f" Mother Name : {mother_name}")
        print("------------------------------------------------------------------------")
        print(f" Parents Phone number : {parent_phone}")
        print("------------------------------------------------------------------------")
        print(f" Email : {email}")
        print("------------------------------------------------------------------------")
        print(f" Python Marks : {python_marks}")
        print("------------------------------------------------------------------------")
        print(f" Math Mark : {math_marks}")
        print("------------------------------------------------------------------------")
        print(f" English Mark : {english_marks}")
        print("------------------------------------------------------------------------")
        print(f" Total : {total}")
        print("------------------------------------------------------------------------")
        print(f" Average : {average}")
        print("------------------------------------------------------------------------")
        print(f" Grade : {grade}")
        print("------------------------------------------------------------------------")
        print(f" Status : {status}")
        print("------------------------------------------------------------------------\n")
        print("========================================================================\n")


def get_updt_input(dtls):

    (usr_id,old_rollnum, old_name, old_dob, old_department, old_year, old_section, old_father_name, 
    old_mother_name, old_parent_phone, old_email, old_python_marks, old_math_marks, 
    old_english_marks, old_total, old_avg, old_grade, old_status,crtd_at) = dtls

    print("To Update type new value or to retain old detail press enter") 


    nrollno = get_valid_updt_input(f"Old Roll Num {old_rollnum} :: Enter New Roll Number : ",validate_roll_no,str,old_rollnum)
    print("")
    name = get_valid_updt_input(f"Old Name {old_name} :: Enter New Name : ",validate_name,str,old_name)
    print("")
    dob = get_valid_updt_input(f"Old DoB {old_dob} :: Enter New DoB : ",validate_dob,str,old_dob)
    print("")
    department = get_valid_updt_input(f"Old Department {old_department} :: Enter New Department : ",validate_department,str,old_department)
    print("")
    
    year = get_valid_updt_input(f"Old Year {old_year} :: Enter New Year : ",validate_roll_no,int,old_year)
    print("")       
    section = get_valid_updt_input(f"Old Section {old_section} :: Enter New Section : ",validate_roll_no,str,old_section)
    print("")
    father_name = get_valid_updt_input(f"Old Father Name {old_father_name} :: Enter New Father Name : ",validate_roll_no,str,old_father_name)
    print("")
    mother_name =get_valid_updt_input(f"Old Mother Name {old_mother_name} :: Enter New Mother Name : ",validate_roll_no,str,old_mother_name)
    print("")
    parent_phone = get_valid_updt_input(f"Old Roll Num {old_parent_phone} :: Enter New Roll Number : ",validate_roll_no,str,old_parent_phone)
    print("")
    email = get_valid_updt_input(f"Old Roll Num {old_rollnum} :: Enter New Roll Number : ",validate_roll_no,str,old_rollnum)
    
    python_marks = get_valid_updt_input(f"Old Roll Num {old_rollnum} :: Enter New Roll Number : ",validate_roll_no,float,old_rollnum)
    print("")
    math_marks = get_valid_updt_input(f"Old Roll Num {old_rollnum} :: Enter New Roll Number : ",validate_roll_no,float,old_rollnum)
    print("")
    english_marks = get_valid_updt_input(f"Old English Mark {old_english_marks} :: Enter New English Mark : ",validate_roll_no,float,old_english_marks)
    print("")
            
    total = total_mark(python_marks, math_marks, english_marks)
    avg = average_mark(total)
    grade = cal_grade(avg)
    status = cal_status(python_marks, math_marks, english_marks)
    
    return (nrollno, name, dob, department, year, section, father_name, 
            mother_name, parent_phone, email, python_marks, math_marks, 
            english_marks, total, avg, grade, status)

def update_student_info():
        print("========================================================================")
        print("                       STUDENTS DETAIL UPDATE                           ")
        print("========================================================================\n")

        student_rollnum = input("Enter The Student Roll Number : ")
        print("")
        print("Student Detail Before Editing ")
        print("")
        old_detail=get_std(student_rollnum)
        display_student_info(old_detail)
        print(" ---Enter new details--- \n")
        get_updt_inp=get_updt_input(old_detail)
        (nrollnum, nname, ndob, ndepartment, nyear, nsection, nfather_name, 
        nmother_name, nparent_phone, nemail, npython_marks, nmath_marks, 
        nenglish_marks, ntotal, navg, ngrade, nstatus)=get_updt_inp
        print(" ---Enter new details--- ")


        try:
            update_student_db(student_rollnum,nrollnum, nname, ndob, ndepartment, nyear, nsection, nfather_name, 
                   nmother_name, nparent_phone, nemail, npython_marks, nmath_marks, 
                   nenglish_marks, ntotal, navg, ngrade, nstatus)
            print("\n" + "="*50)
            print("🎉 SUCCESS: Student details updated successfully!\n")
            print("="*50 + "\n")

            print("Student Detail After Updating ")
            updt_details = get_std(nrollnum)
            display_student_info(updt_details)
        except Exception as e:
            print("\n" + "="*50)
            print(f"❌ ERROR: Failed to update student. Reason: {e}")
            print("="*50 + "\n")

def delete_student():
    print("---Enter Student Roll Number To Delete---")
    drollnum = input("Roll Number : ")
    std_inf = get_std(drollnum)
    if std_inf == None:
        print("Sorry No Data Found")
    else:
        display_student_info(std_inf)
        print("")
        print("Are you sure, Do you want to delete the user above\n")
        print("After deleting you cannot retrive the deleted data \n")
        print("If yes press -- 1 OR press -- 2")
        opt={1,2}
        while True:
            try:
                opt_inp = int(input("Your Choice : "))
            except ValueError:
                print("Please Enter only numbers")

            if opt_inp in opt:
                if opt_inp == 1:
                    delete_std_db(drollnum)
                    print("User Deleted Sucessfully ✅")
                    break
                elif opt_inp == 2:
                    print("Operation Aborted Sucessfully ❌")
                    break
            else:
                print("Try again")

def std_statistcs()     :
        
        total_std,max_avg,min_avg,avg,t_pass,t_fail,g_ap,g_a,g_b,g_c,g_d,g_f = statistics_db()

        print("========================================================================")
        print("                      STUDENT STATISTICS DASHBOARD                      ")
        print("========================================================================\n")  
        print("📚 Total Students : ",total_std)     
        print("✅ Passed Students : ",t_pass)
        print("❌ Failed Students : ",t_fail)
        print("")
        print("")
        print("🏆 Highest Average : ",max_avg)
        print("📉 Lowest Average : ",min_avg)
        print("📊 Class Average : ",avg)
        print("")
        print("")
        print("🥇 Grade A+ : ",g_ap)
        print("🥈 Grade A : ",g_a)
        print("🥉 Grade B : ",g_b)
        print("⭐ Grade C : ",g_c)
        print("📘 Grade D : ",g_d)
        print("❌ Grade F  : ",g_f)


def search_std():
    opt={1,2,3,4,5}
    print(" ---From Which Quantity You Want To Search--- ")
    print("To Search by ROLL NO press --1")
    print("To Search by NAME press --2")
    print("To Search by DEPARTMENT NO press --3")
    print("To Search by YEAR NO press --4")
    print("To go back --5\n")
    while True:
        try:
            usr_inp=int(input("Your Option : "))
            print("")
            break
        except ValueError:
            print("Please enetr only the visible options\n")
    if usr_inp in opt :
        print("Enter the search value : ")
        value = input("Value : ")
        if usr_inp == 5:
            print("Returning back..")
            sleep(.5)
            return
        else:
            res_lst = search_std_db(usr_inp,value)

            if not res_lst:
                print("Sorry No data found with given data ")
                return
            else:
                for val in res_lst:
                    display_student_info(val)
    else:
        print("Please enter only give options")



main_menu()