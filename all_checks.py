#!/usr/bin/env python
import os
import sys
import shutil

def check_reboot():
    """Returns True if the computer have pending reboot"""
    return  os.path.exists("/run/reboot/reboot-required")



def check_disk_usage(disk,min_absolute,min_percent):
	du= shutil.disk_usage(disk)
	percent_free=100*du.free/du.total
	gigabytes_free=du.free/2**30
	if percent_free<min_percent or gigabytes_free<min_absolute:
		return False
	return True

if not check_disk_usage("/",2,10):
    print("Error: Not enough space")
    sys.exit(1)
else:
    print("Everything Ok")
    sys.exit(0) 

def main():
    if check_reboot():
       print("Pending Reboot.")
       sys.exit(1)
    print("Everything Ok")
    sys.exit(0)
    
main()
