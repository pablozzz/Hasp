from ctypes import *
kernel32  = windll.kernel32 

#List of function names which adresses we find (example hasp-emulated functions)

func_list = ["GetCommandLineA",
             "GetProcAddress",
             "GetCurrentProcess",
             "GetStartupInfoA",
             "GetCurrentProcessId",
             "GetCurrentThreadId"]

def find_func_adress(dll,function):
#Function input - dll name and name of function the return funtion's adress
    
        handle  = kernel32.GetModuleHandleA(dll)
        address = kernel32.GetProcAddress(handle, function)
        kernel32.CloseHandle(handle)
        return address

# loop for all functions
def main(func_list):
	for x in func_list:
		printf_address = find_func_adress("kernel32.dll",x) #change dll name if need
		print "[*] Address of %s: 0x%08x" % (x, printf_address)

if __name__ == '__main__': main(func_list)
	

