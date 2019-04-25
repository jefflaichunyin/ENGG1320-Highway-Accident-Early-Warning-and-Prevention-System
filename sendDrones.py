#!/usr/bin/python3
import cgi
import requests
import os
drone_IP = "192.168.1.102"
url = "http://" + drone_IP + "/on"
os.system("echo 'engg1320' | sudo -S  ./blink.py")
try:
    requests.get(url,timeout=1)
except:
    print('Content-type: text/html\n\n')
    print('<head><meta http-equiv="refresh" content="0; url=livestream.html" /></head>')
