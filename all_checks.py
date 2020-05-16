#!/usr/bin/env python
import os
import sys
import shutil

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


def main():
    if check_reboot():
       print("Pending Reboot.")
       sys.exit(1)
    if check_disk_full(disk="/",min_gb=2,min_percent=10):
       print("Disk Full")
       sys.exit(1)
    if check_root_full():
       print("Root Partition full")
       sys.exit(1)

    print("Everything Ok")
    sys.exit(0)

main()
