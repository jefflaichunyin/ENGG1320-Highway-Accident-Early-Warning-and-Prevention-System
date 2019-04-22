#!/usr/bin/python3
import cgi
import requests
f=open("status","w")
f.write("No")
f.close()

drone_IP = "192.168.0.112"
url = "http://" + drone_IP + "/off"
try:
    requests.get(url,timeout=1)
except:
    print('Content-type: text/html\n\n')
    print('<head><meta http-equiv="refresh" content="0; url=index.html" /></head>')
