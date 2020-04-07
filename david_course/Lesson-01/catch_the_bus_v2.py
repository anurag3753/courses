#!/usr/bin/env python3
"""
   In this version, we have removed the hardwired of route and stop and accept
   it as commandline arg from the user. The top shebang trick will only work in
   linux/unix machines. 
   --- Make sure to do chmod +x catch_the_bus_v2.py
   Usage : 
        With Shebang : ./catch_the_bus_v2.py 14787 22 
        Windows : python catch_the_bus_v2.py 14787 22

"""
import sys
import urllib.request
from xml.etree.ElementTree import XML

if len(sys.argv) != 3:
    print("Usage: catch_the_bus_v2.py route stopid")
    raise SystemExit(0)

route = sys.argv[1]
stopid = sys.argv[2]

u = urllib.request.urlopen('http://ctabustracker.com/bustime/map/getStopPredictions.jsp?stop={}&route={}'.format(route, stopid))
data = u.read()
doc = XML(data)
# print(data)
# It is found out that the relevant information inside the XML doc is present
# in b/w the <pt> tag. So, try to get the data out of the pt tag. 
for pt in doc.findall('.//pt'):
    print(pt.txt)