import shutil
from config import DATABASE_PATH,BACKUP_PATH,FINAL_PATH_BACKUP
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
        os.makedirs(FINAL_PATH_BACKUP, exist_ok=True)

        start = time.perf_counter()
        shutil.copy2(DATABASE_PATH, BACKUP_PATH)
        end = time.perf_counter()
        t_time = round(end - start, 4)

        print(f"✅ Created backup successfully! Location: {BACKUP_PATH} in {t_time}s\n")
        print("Back to main menu..\n")
    else:
        print("❌ Database file does not exist to back up!")


def restore_backup():
    print("⚠️ WARNING: Restoring will overwrite your current database!")

    if not os.path.exists(FINAL_PATH_BACKUP):
        print("❌ No backup directory found.")
        return

    files = [f for f in os.listdir(FINAL_PATH_BACKUP) if os.path.isfile(os.path.join(FINAL_PATH_BACKUP, f))]

    if not files:
        print("❌ No backup files found to restore.")
        return

    print("\nAvailable Backup Files:")
    for idx, file in enumerate(files, start=1):
        print(f"[{idx}] - {file}")

    while True:
        try:
            file_no = int(input("\nChoose a backup file number to restore (or 0 to cancel): "))
            
            if file_no == 0:
                print("Restoration cancelled.")
                break
                
            if 1 <= file_no <= len(files):
                chosen_file = files[file_no - 1]
                file_path = os.path.join(FINAL_PATH_BACKUP, chosen_file)

                shutil.copy2(file_path, DATABASE_PATH)
                
                print(f"✅ Successfully restored database from '{chosen_file}'!\n")
                break
            else:
                print(f"Please enter a number between 1 and {len(files)}.")
                
        except ValueError:
            print("❌ Invalid input! Please enter a number.")


def view_backup():
    print("Here are the backedup files : \n")
    print("_____________________________________________________________________________")

    files = [f for f in os.listdir(FINAL_PATH_BACKUP) if os.path.isfile(os.path.join(FINAL_PATH_BACKUP,f))]

    for inx,file in enumerate(files,start=1):
        print(f"[{inx}] - {file}")
        print("_____________________________________________________________________________")

    print("Printed all files\n")
def delete_backup():
    print("⚠️ WARNING: Deleting will overwrite your current database!")
    files = [f for f in os.listdir(FINAL_PATH_BACKUP) if os.path.isfile(os.path.join(FINAL_PATH_BACKUP,f))]

    print("Which file to delete : ")

    for inx,file in enumerate(files,start=1):
        print(f"[{inx}] - {file}\n")

    while True:
        try:
            file_no = int(input("\nChoose a backup file number to delete (or 0 to cancel): "))

            if file_no == 0:
                print("Going Back...")
                break

            if 1<=file_no<=len(files):
                remove_path = os.path.join(FINAL_PATH_BACKUP,files[file_no-1])
                os.remove(remove_path)
                print(f"Backup Files after deleting {os.path.join(FINAL_PATH_BACKUP,files[file_no-1])}")

                for inx,file in enumerate(files,start=1):
                    print(f"[{inx}] - {file}\n")
                
                break
            else:
                print("Enter a valid File No")

        except:
            print("❌ Invalid input! Please enter a number.")