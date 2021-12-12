##############################
#   TokenGuard by ZaikoARG   #
#   All Rights Reserved :)   #
##############################

# https://github.com/ZaikoARG | Discord: ZaikoARG#1187

from ctypes import *
from ctypes.wintypes import *
import mem_edit
import ctypes
import ctypes.wintypes
import re
import time
import psutil
import logs
import shared_variables

class GetUserToken(): # Class for Read Memory and Get Discord Token
    def __init__(self, process_id):

        self.process_id = process_id
        ### OpenProcess and create Handle
        privileges = {
        'PROCESS_QUERY_INFORMATION': 0x0400,
        'PROCESS_VM_OPERATION': 0x0008,
        'PROCESS_VM_READ': 0x0010,
        'PROCESS_VM_WRITE': 0x0020,
        }
        privileges['PROCESS_RW'] = (
            privileges['PROCESS_QUERY_INFORMATION'] |
            privileges['PROCESS_VM_OPERATION'] |
            privileges['PROCESS_VM_READ'] |
            privileges['PROCESS_VM_WRITE']
            )

        self.process = ctypes.windll.kernel32.OpenProcess(
            privileges['PROCESS_RW'],
            False,
            process_id
            )

    def search_memory(self) -> str:
        ### Search in memory process
        def read_memory(handle, base_address: int, read_buffer):
            try:
                ctypes.windll.kernel32.ReadProcessMemory(
                    handle,
                    base_address,
                    ctypes.byref(read_buffer),
                    ctypes.sizeof(read_buffer),
                    None
                    )
            except (BufferError, ValueError, TypeError):
                pass

            return read_buffer
        try:
            proc = mem_edit.Process(self.process_id)
        except Exception as e:
            print(e)
        STRLEN = create_string_buffer(4096)
        count = 0
        pattern = re.compile(r'417574686f72697a6174696f6e000000430000003b000000[a-zA-Z0-9]{118}')

        reference = "417574686f72697a6174696f6e000000430000003b000000"
        try:
            for start, finish in proc.list_mapped_regions(writeable_only=False):
                address = start
                while (address < finish):
                    try:
                        buffer = read_memory(self.process, address, STRLEN).raw.hex()
                        if reference in buffer:
                            xddddd = pattern.findall(buffer)
                            if xddddd and xddddd[0].replace("417574686f72697a6174696f6e000000430000003b000000", "")[:2] != "00":
                                return xddddd[0].replace("417574686f72697a6174696f6e000000430000003b000000", "")
                    except Exception as e:
                        if psutil.pid_exists() != True:
                            shared_variables.DiscordError = True
                        pass
                    address += 4096
        except:
            shared_variables.DiscordError = True
        return None

class MyStruct(ctypes.Structure):
        _fields_ = [
               ('first_member', ctypes.c_ulong),
               ('second_member', ctypes.c_void_p),
               ]


def Token_Memory_Cleaner(PID:int, token:str) -> None: # Class for Delete Token Traces in Discord Process Memory
    pr = mem_edit.Process
    count = 0
    try:
        p = pr(PID)
    except:
        shared_variables.DiscordError = True
    while shared_variables.Protection_Status == True:
        try:
            with pr.open_process(PID) as p:
                s = MyStruct()
                s.first_member = 0
                s.second_member = 0
                for addr in p.search_all_memory(bytes.fromhex(token)):
                    p.write_memory(addr, s)
                    count +=1
                if count != 0:
                    logs.WriteLogs(count, "memory")
            time.sleep(5)
            count = 0
        except:
            shared_variables.DiscordError = True
    return