#!/usr/bin/env python
import re
import json
from datetime import datetime as dt
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
ISO = []
time_parsed = []
for index in range(len(MSG)):
	ALT.append(MSG[index][3])
	UTC.append(MSG[index][7:9])
	URL.append(re.split('=|&', MSG[index][10]))	
	TXT.append(MSG[index][11:])
for index in range(len(URL)):
	LAT.append(URL[index][1])
	LON.append(URL[index][3])
for index in range(len(UTC)):
	TIME.append(UTC[index][0] + " " + UTC[index][1])
	time_parsed.append(dt.strptime(TIME[index], "%d-%b-%Y %H:%M:%S"))
	ISO.append(dt.strftime(time_parsed[index], "%Y-%m-%d %H:%M:%SZ"))
data = []
for i in range(len(MSG)):
	data.append({'alt':ALT[i], 'lat':LAT[i], 'lng':LON[i], 'title':ISO[i], 'content':' '.join(TXT[i])})

j = json.dumps(data, indent=2)
f = open('map.json', 'w')
print >> f, j
f.close()