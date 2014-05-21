#!/usr/bin/env python
import re
import json
RAWDATA = []
for line in open("../draga_mail"):
	if "http://" in line:
		RAWDATA.append(line)
MSG = [i.split(" ") for i in RAWDATA]
UTC = []
URL = []
TXT = []
LAT = []
LON = []
ALT = []
TIME = []
for index in range(len(MSG)):
	ALT.append(MSG[index][3])
	UTC.append(MSG[index][7:10])
	URL.append(re.split('=|&', MSG[index][10]))	
	TXT.append(MSG[index][11:])
for index in range(len(URL)):
	LAT.append(URL[index][1])
	LON.append(URL[index][3])
for index in range(len(UTC)):
	TIME.append(UTC[index][0] + " " + UTC[index][1] + " " + UTC[index][2])
data = []
for index in range(len(MSG)):
	data.append({'alt':ALT[index], 'lat':LAT[index], 'lng':LON[index], 'title':TIME[index], 'content':' '.join(TXT[index])})

j = json.dumps(data, indent=2)
f = open('map.json', 'w')
print >> f, j
f.close()
