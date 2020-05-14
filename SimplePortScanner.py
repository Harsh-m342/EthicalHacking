#!/bin/python

import sys
import socket
from datetime import datetime as dt

#Define our target
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1]) #Translate hostname to IPv4
else:
    print("Invalid amount of arguements.")
    print("Synatx: python3 SimplePortScanner.py <ip>")

#Add a pretty banner
print("-" * 40)
print("Scanning Target: "+ target)
print("Time Started: " + str(dt.now()))
print("-" * 40)

#Try and Catch
try:
    for port in range(1,65535):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target,port)) #returns an error indicator
        if result==0:
            print("PORT {} is open".format(port))
        s.close()
except KeyboardInterrupt:
    print("\nExiting Program.")
    sys.exit()
except socket.gaierror:
    print("Hostname could not be resolved.")
    sys.exit()
except socket.error:
    print("Could not connect to server.")
    sys.exit()


