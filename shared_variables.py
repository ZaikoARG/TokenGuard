##############################
#   TokenGuard by ZaikoARG   #
#   All Rights Reserved :)   #
##############################

# https://github.com/ZaikoARG | Discord: ZaikoARG#1187

import sys
import pathlib
import os
import psutil

# Functions
def get_absolute_path():
    config_name = 'myapp.cfg'
    
    # determine if application is a script file or frozen exe
    if getattr(sys, 'frozen', False):
        application_path = os.path.dirname(sys.executable)
        filename = psutil.Process(os.getpid()).name()
    elif __file__:
        application_path = os.path.dirname(__file__)
        filename = pathlib.Path(os.path.abspath(__file__)).name

    config_path = os.path.join(application_path, config_name)
    config_path = pathlib.Path(config_path).parent.resolve()
    return config_path, filename



# Variables
Protection_Status = False # Set if Protection is Enabled
config_path = str(get_absolute_path()[0]) # Program Path
filename = str(get_absolute_path()[1]) # Executable FileName
WindowHide = "" # Set if Windows is Show or Hide
DiscordError = False # Set Error Flag for Discord
WaitingDiscord = False # Set Waiting Discord Process Status