##############################
#   TokenGuard by ZaikoARG   #
#   All Rights Reserved :)   #
##############################

# https://github.com/ZaikoARG | Discord: ZaikoARG#1187

import time
import threading
import psutil
import memory
import files
import psutil
import shared_variables



class TokenProtection():
    def __init__(self) -> None:
        pass

    def start(self):
        # Define Protection Status ON
        shared_variables.Protection_Status = True
        # Get Discord PID
        pid = self.get_discord_pid()
        if pid == None:
            return
        # Get Token
        token = None
        while token == None and shared_variables.Protection_Status == True:
            token = memory.GetUserToken(pid).search_memory()
        # Clear Discord LDB Files And Remove The Tokens
        files.ClearLDB(token)
        time.sleep(1)
        # Initialize the Token Memory Cleaner Thread
        t2 = threading.Thread(target=memory.Token_Memory_Cleaner, args=[pid, token])
        t2.start()
        del token
        return
        
    def stop(self):
        # Define Protection Status OFF
        shared_variables.Protection_Status = False


    def get_discord_pid(self):
        # Waiting for Discord Process and Get the PPID
        while shared_variables.Protection_Status == True:
            time.sleep(1)
            for proc in psutil.process_iter():
                if proc.name() == "Discord.exe":
                    shared_variables.WaitingDiscord = False
                    if psutil.pid_exists(proc.ppid()) == False:
                        return proc.pid
                    else:
                        return proc.ppid()
            if shared_variables.WaitingDiscord == False:
                shared_variables.WaitingDiscord = True
        return None