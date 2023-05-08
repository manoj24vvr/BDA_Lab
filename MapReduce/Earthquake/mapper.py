#!/usr/bin/python3
""" mapper.py"""

# this file is used to generate the key-value pairs

import sys

for line in sys.stdin:
    region, date, time, longitude, latitude, magnitude = line.strip().split(',')
    print(f"{region}\t1,{magnitude}")

		
