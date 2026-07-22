import os
import time

BASE_DIR=os.path.dirname(os.path.abspath(__file__))


DATABASE_DIR=os.path.join(BASE_DIR,"database")
DATABASE_PATH=os.path.join(DATABASE_DIR,"student.db")
EXPORT_DIR = os.path.join(BASE_DIR,"exports")


time_stamp = time.strftime("%Y%m%d_%H%M%S")
EXP_PATH = f"students_export_{time_stamp}.csv"
EXPORT_PATH = os.path.join(EXPORT_DIR,EXP_PATH)
