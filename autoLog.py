#!/usr/bin/python
import sys
import time
from subprocess import call

sys.path.append('./')

while True :
    time.sleep(2)
    call("caffeinate -u python log.py", shell=True)
