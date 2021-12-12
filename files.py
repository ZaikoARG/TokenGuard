##############################
#   TokenGuard by ZaikoARG   #
#   All Rights Reserved :)   #
##############################

# https://github.com/ZaikoARG | Discord: ZaikoARG#1187

import os
import logs


def ClearLDB(token) -> None:
    # Class for Clear LDB  Files in Discord
    discord_path = os.environ['APPDATA'] + r"\discord\Local Storage\leveldb"
    count = 0
    for file in os.listdir(discord_path):
        if os.path.isfile(discord_path + '\\' + file) == True:
            try:
                with open(discord_path + '\\' + file, "wb+") as ldb:
                    bytes_token = bytes.fromhex(token)
                    if bytes_token in ldb.read():
                        content_cleared = ldb.read().replace(bytes_token, b"")
                        ldb.truncate(content_cleared)
                        count += 1
                    del bytes_token
            except:
                pass
    logs.WriteLogs(count, "files")