from ctypes import *
from ctypes.wintypes import *

PROCESS_ID = 9476 # From TaskManager for Notepad.exe
PROCESS_HEADER_ADDR = 0x7ff7b81e0000 # From SysInternals VMMap utility

# write to address
newValue = 50

PROCESS_VM_READ = 0x0010

k32 = WinDLL('kernel32')
k32.OpenProcess.argtypes = DWORD,BOOL,DWORD
k32.OpenProcess.restype = HANDLE
k32.WriteProcessMemory.argtypes = HANDLE,LPVOID,LPVOID,c_size_t,POINTER(c_size_t)
k32.WriteProcessMemory.restype = BOOL

process = k32.OpenProcess(PROCESS_VM_READ, 0, PROCESS_ID)
s = c_size_t()

k32.WriteProcessMemory(process, PROCESS_HEADER_ADDR, newValue, 255, byref(s))