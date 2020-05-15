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