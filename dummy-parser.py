#!/usr/bin/env python
import re
f = open("iridum.mail")
lines = f.read()
LON=lines.splitlines()
TIME=LON[-1].split(" ")
POSITION=re.split('=|&',LON[-1])
LAT=(POSITION[-3])
LON=(POSITION[-1])
print(LAT,LON,TIME[-4:-1])
f.close
