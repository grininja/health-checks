#!/usr/bin/env python
import os
import sys
import shutil
import socket


def check_reboot():
    """Returns True if the computer have pending reboot"""
    return  os.path.exists("/run/reboot/reboot-required")



def check_disk_full(disk,min_gb,min_percent):
	du= shutil.disk_usage(disk)
	percent_free=100*du.free/du.total
	gigabytes_free=du.free/2**30
	if gigabytes_free<min_gb or percent_free<min_percent:
		return True
	return False

def check_root_full():
    """Returns True if the most partition is full, False otherwise."""
    return check_disk_full(disk="/",min_gb=2,min_percent=10)   

def check_no_network():
    """Returns True if it fails to resolve Google's URL, False otherwise"""
    try:
       socket.gethostbyname("www.google.com")
       return True
    except:
       return  False


checks=[(check_reboot,"Check if any reboot pending"),(check_root_full,"Check partition is full or not"),(check_no_network,"There is network access")]

def main():

    everything_fine=True
    for check,state in checks:
        if check():
           print(state)
           everything_fine =False
    if not everything_fine:
       sys.exit(1)

    print("Everything Ok")
    sys.exit(0)

main()
 
