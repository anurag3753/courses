"""The purpose of this program is to check the california bus time tables. We
   are trying to find out when will be the next bus available from some stop
   for a particular route.
   In this case,
        Stop = 14787
        Route = 22
"""
import urllib.request
from xml.etree.ElementTree import XML
u = urllib.request.urlopen('http://ctabustracker.com/bustime/map/getStopPredictions.jsp?stop=14787&route=22')
data = u.read()
doc = XML(data)
# print(data)
# It is found out that the relevant information inside the XML doc is present
# in b/w the <pt> tag. So, try to get the data out of the pt tag. 
for pt in doc.findall('.//pt'):
    print(pt.text)