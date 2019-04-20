#!/usr/bin/python3
import sys
import time

time.sleep(1)
file = open("status", "r")
sys.stdout.write('Content-type: text/event-stream \r\n\r\n')
returnval = file.readline()
file.close()
sys.stdout.write('data: %s \r\n' % returnval)
sys.stdout.write('retry: 1000\r\n\r\n')
sys.stdout.flush()
