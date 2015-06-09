from ctypes import *

kernel32  = windll.kernel32 

#List of function names which adresses we find (example hasp-emulated functions)

find_func = ["GetCommandLineA",
             "GetProcAddress",
             "GetCurrentProcess",
             "GetStartupInfoA",
             "GetCurrentProcessId",
             "GetCurrentThreadId"]

def func_adress_find(dll,function):
#Function input - dll name and name of function the return funtion's adress
    
        handle  = kernel32.GetModuleHandleA(dll)
        address = kernel32.GetProcAddress(handle, function)
        kernel32.CloseHandle(handle)
        return address

# loop for all functions

for x in find_func:
    printf_address = func_adress_find("kernel32.dll",x) #change dll name if need
    print "[*] Address of %s: 0x%08x" % (x, printf_address)

