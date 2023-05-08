#!/usr/bin/python3

import sys

current_pair = None
current_users = []

for line in sys.stdin:
    pair, user = line.strip().split("\t")
    
    if pair != current_pair:
        if current_pair:
            print(f"{current_pair}\t{', '.join(current_users)}")
        
        current_pair = pair
        current_users = [user]
    else:
        current_users.append(user)

if current_pair:
    print(f"{current_pair}\t{', '.join(current_users)}")

