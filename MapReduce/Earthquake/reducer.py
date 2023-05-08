#!/usr/bin/python3
""" reducer.py"""

import sys

counts = {}
magnitudes = {}

for line in sys.stdin:
    region, values = line.strip().split('\t')
    count, magnitude = values.split(',')
    count = int(count)
    magnitude = float(magnitude)

    if region not in counts:
        counts[region] = 0
        magnitudes[region] = 0

    counts[region] += count
    magnitudes[region] += magnitude
    
print("\nRegion\tCount\tTotal Magnitude\t\tAvg.Magnitude\n")

for region in counts:
    count = counts[region]
    total_magnitude = magnitudes[region]
    avg_magnitude = total_magnitude / count
    print(f"{region}\t{count},\t{total_magnitude},\t{avg_magnitude}")
    
print("\n")

max = 0
max_region = None
for i in counts:
	if(counts[i] > max):
		max = counts[i]
		max_region = str(i)
print("Maximum earthquake occurence region is: ",max_region,"(",max,"times)")
