#!/usr/bin/python3
#Author : Atyam V V R Manoj
import sys
import collections

prevkey = None
friends=""
def commonFriends():
    parts = friends.split(" ")
    common = [item for item, count in collections.Counter(parts).items() if count > 1]
    common = map(int, common)
    print('%s %s'%(prevkey, common))
    return 
for line in sys.stdin:
    line = line.strip()
    key, value = line.split('\t')
    if prevkey == key:
        friends = friends+" "+value
    else:
        if prevkey == None:
            prevkey = key
            friends = friends+" "+value
        else:
            commonFriends()
            prevkey = key
            friends=""
            friends = friends+" "+value
commonFriends()
