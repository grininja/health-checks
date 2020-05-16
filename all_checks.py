#!/usr/bin/env python
import os
import sys

def check_reboot():
    """Returns True if the computer have pending reboot"""
    return  os.path.exists("/run/reboot/reboot-required")


def main():
    if check_reboot():
       print("Pending Reboot.")
       sys.exit(1)
    print("Everything Ok")
    sys.exit(0)
main()
