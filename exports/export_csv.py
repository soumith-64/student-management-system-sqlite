import csv
from config import EXPORT_PATH
def export_csv_std(data,col_name):

    try:
    
        with open(EXPORT_PATH,mode = "w",newline="",encoding="utf-8") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(col_name)
            writer.writerows(data)
            return EXPORT_PATH
    except OSError:
        print("Sorry some error occured")
        return None
    