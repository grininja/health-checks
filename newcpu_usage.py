#!/usr/bin/env/python
import shutil
import psutil

def check_cpu_usage(percent):
	usage=psutil.cpu_percent(1)
	return usage<percent
if not check_cpu_usage(75):
    print("Error CPU is overloaded")
else:
    print("Everything ok")

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
