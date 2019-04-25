#!/usr/bin/python3
import cgi
import requests
import os
f=open("status","w")
f.write("No")
f.close()

drone_IP = "192.168.1.102"
url = "http://" + drone_IP + "/off"
os.system("echo 'engg1320' | sudo -S killall -9 blink.py")
os.system("echo 'engg1320' | sudo -S ./stop_blinking.py")
try:
    requests.get(url,timeout=1)
except:
    print('Content-type: text/html\n\n')
    print('')
