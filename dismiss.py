#!/usr/bin/python3
import cgi
import requests
f=open("status","w")
f.write("No")
f.close()

drone_IP = "192.168.1.102"
url = "http://" + drone_IP + "/off"
try:
    requests.get(url,timeout=1)
except:
    print('Content-type: text/html\n\n')
    print('')
