#Code by bigmohammad
#---------------------
#Youtube: bigmohammad
#---------------------
#Instagram: bigmohammad.official

import subprocess
from colorama import init, Fore

# Activate colorama to use ANSI color codes
init(autoreset=True)

def get_hwid():
    try:
        # Execute the appropriate command to retrieve HWID information
        hwid_info = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()
        return hwid_info
    except Exception as e:
        print(f"{Fore.RED}Error retrieving HWID: {e}")

# Call the function to get HWID information
hwid = get_hwid()

if hwid:
    print(f"{Fore.GREEN}HWID: {hwid}")

input(f"\n{Fore.RED}Press Enter to exit...")

