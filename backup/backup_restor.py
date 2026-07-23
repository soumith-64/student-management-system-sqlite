import shutil
from config import DATABASE_PATH,BACKUP_PATH
import os , time

def backup_restore_std():   
    print("========================================================================")
    print("                              DATABASE BACKUP                           ")
    print("========================================================================\n")
    print("To Create Backup press -1")
    print("To Restore Backup press -2")
    print("To View Backup press -3")
    print("To Delete Backup press -4")
    print("To Go-Back -5\n")
    opt = [1,2,3,4,5]
    while True:
        try:
            usr_inp = int(input("Your Choice : "))
            if usr_inp in opt:
                if usr_inp == 1:
                    create_backup()
                elif usr_inp == 2:
                    restore_backup()
                elif usr_inp == 3:
                    view_backup()
                elif usr_inp == 4:
                    delete_backup()
                elif usr_inp == 5:
                    print("Going Back....")
                    return
                break
            else:
                print("Enter a Option only which is given")
        except ValueError:
            print("Please enter only numbers")

def create_backup():
    if os.path.exists(DATABASE_PATH):

        start = time.perf_counter()
        shutil.copy2(DATABASE_PATH,BACKUP_PATH)
        end = time.perf_counter()
        t_time = round(end - start , 4)
        print(f"Created Back up sucessfully, location : {BACKUP_PATH} in {t_time} seconds\n")
        print("Back to main menu..")

def restore_backup():
    pass

def view_backup():
    pass

def delete_backup():
    pass