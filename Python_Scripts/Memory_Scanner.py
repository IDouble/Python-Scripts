import ctypes as c
from ctypes import wintypes as w
from struct import *
from time import *
import datetime
import sys

pid = 1234

k32 = c.windll.kernel32

OpenProcess = k32.OpenProcess
OpenProcess.argtypes = [w.DWORD,w.BOOL,w.DWORD]
OpenProcess.restype = w.HANDLE

ReadProcessMemory = k32.ReadProcessMemory
ReadProcessMemory.argtypes = [w.HANDLE,w.LPCVOID,w.LPVOID,c.c_size_t,c.POINTER(c.c_size_t)]
ReadProcessMemory.restype = w.BOOL
PAA = 0x1F0FFF
address = 0x4000000
ph = OpenProcess(PAA,False,int(pid)) #program handle

buff = c.create_string_buffer(4)
bufferSize = (c.sizeof(buff))
bytesRead = c.c_ulonglong(0)

addresses_list = xrange(address,0x9000000,0x4)
log=open(r'out.txt.','wb',0)
for i in addresses_list:
    ReadProcessMemory(ph, c.c_void_p(i), buff, bufferSize, c.byref(bytesRead))
    value = unpack('I',buff)[0]
    if value == int(sys.argv[1]):
        log.write('%x\r\n' % (i, ))