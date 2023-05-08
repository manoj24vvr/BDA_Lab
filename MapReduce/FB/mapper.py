#!/usr/bin/python3

import sys

for line in sys.stdin:
    line = line.strip()
    user, friends = line.split(":")
    friends_list = friends.split(",")
    for i in range(len(friends_list)):
        for j in range(i+1, len(friends_list)):
            print(f"{friends_list[i]}, {friends_list[j]}\t{user}")

