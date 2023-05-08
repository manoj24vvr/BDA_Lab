#!/usr/bin/python3
#Author : Atyam V V R Manoj 
import sys

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    #concatenate company with date as make it a key
    key = line.split(",")[0]
    friends = line.split(",")[1]
    friend=friends.split(" ")
    for val in friend:
        if int(val) > int(key):
            print('%s,%s\t%s' % (key, val, friends)) # return the key value pair
        else:
            print('%s,%s\t%s' % (val, key, friends))
