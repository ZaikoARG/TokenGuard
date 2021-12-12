##############################
#   TokenGuard by ZaikoARG   #
#   All Rights Reserved :)   #
##############################

# https://github.com/ZaikoARG | Discord: ZaikoARG#1187

import os
import time
import datetime
import shared_variables

config_path = shared_variables.config_path

def WriteLogs(data:str, logtype:str): # Write Logs in /logs/TP_LOG.txt
    time.sleep(1)
    filename = config_path + r"\logs\TG_LOG.txt"
    if logtype == "memory":
        data = "{} tokens have been cleared from memory.".format(data)
    else:
        data = "Cleaned {} tokens from local Discord databases.".format(data)

    date = f'[{datetime.datetime.now().strftime("%d/%m/%y %H:%M:%S")}]'

    if os.path.exists(filename) == True:
        num_lines = sum(1 for line in open(filename))
        if num_lines >= 10000:
            with open(filename, "a+") as log:
                log.truncate(f"{date} {data} \n")
        else:
            with open(filename, "a+") as log:
                log.write(f"{date} {data} \n")
    else:
        log = open(filename, "w")
        log.write(f"{date} {data} \n")
