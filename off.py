#!/usr/bin/python3
import cgi
f=open("status","w")
f.write("No")
f.close()
print('Content-type: text/html\n\n')
print('<head><meta http-equiv="refresh" content="0; url=control.html" /></head>')
