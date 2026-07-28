import time,os
from config import LOGGING_FOLDER
def logg(type,value):

    exe_time = time.strftime("%Y-%m-%d %H:%M:%S")
    if value:
        sent =  f"{exe_time} | INFO | {type} | {value} "
    else:
        sent =  f"{exe_time} | INFO | {type} "

    logfile_path = os.path.join(LOGGING_FOLDER,"app.log")

    os.makedirs(LOGGING_FOLDER, exist_ok= True)
    with open(logfile_path,"a") as logging:
        logging.write(f"{sent}\n")
