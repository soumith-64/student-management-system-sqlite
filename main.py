from database.database import initialize_database,add_student_db,view_std,get_std,update_student_db,delete_std_db,statistics_db,search_std_db
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

    rollnum = input("Enter Roll Number : ").strip()
    print("")
    name = input("Enter Name : ").strip()
    print("")
    dob = input("Enter DateOfBirth : ").strip()
    print("")
    department = input("Enter Department Name : ").strip().upper()
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

    rollnum = r if (r := input(f"Old Roll Num {old_rollnum} :: Enter New Roll Number : ").strip()) else old_rollnum
    print("")
    name = n if (n := input(f"Old Name {old_name} :: Enter Name : ").strip()) else old_name
    print("")
    dob = d if (d := input(f"Old DOB {old_dob} :: Enter DateOfBirth : ").strip()) else old_dob
    print("")
    department = dep if (dep := input(f"Old Department {old_department} :: Enter Department Name : ").strip().upper()) else old_department
    print("")
    
    while True:
        try:
            y_input = input(f"Old Year {old_year} :: Enter Year : ").strip()
            year = int(y_input) if y_input else old_year
            print("")
            break
        except ValueError:
            print("❌ Invalid input! Please enter a numeric year.\n")
            
    section = s if (s := input(f"Old Section {old_section} :: Enter Section : ").strip()) else old_section
    print("")
    father_name = fn if (fn := input(f"Old Father Name {old_father_name} :: Enter Father Name : ").strip()) else old_father_name
    print("")
    mother_name = mn if (mn := input(f"Old Mother Name {old_mother_name} :: Enter Mother Name : ").strip()) else old_mother_name
    print("")
    parent_phone = pp if (pp := input(f"Old Parent Ph.No {old_parent_phone} :: Enter Parent Phone Number : ").strip()) else old_parent_phone
    print("")
    email = e if (e := input(f"Old Email {old_email} :: Enter Email : ").strip()) else old_email
    print("")
    
    while True:
        try:
            s_pymark = input(f"Old Python Mark {old_python_marks} :: Enter Python Mark : ")
            python_marks = float(s_pymark) if s_pymark else old_python_marks
            print("")
            s_mm = input(f"Old Math Mark {old_math_marks} :: Enter Math Mark : ")
            math_marks = float(s_mm) if s_mm else old_math_marks
            print("")
            s_em = input(f"Old PytEnglish Mark {old_english_marks} :: Enter English Mark : ")
            english_marks = float(s_em) if s_em else old_english_marks
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