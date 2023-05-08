#!/usr/bin/python3

import sys

current_track_id = None
max_time_downloaded = None
unique_listeners = set()
listener_usage_count = {}
max_time_shared = None

for line in sys.stdin:
    fields = line.strip().split("\t")
    track_id, time_stamp, listener_id = fields
    
    if track_id != current_track_id:
        if current_track_id:
            print(f"\n{current_track_id}\t\t{max_time_downloaded}\t\t{len(unique_listeners)}\t\t{','.join([f'{listener}:{listener_usage_count[listener]}' for listener in listener_usage_count])}\t\t{max_time_shared}\n")
        
        current_track_id = track_id
        max_time_downloaded = None
        unique_listeners = set()
        listener_usage_count = {}
        max_time_shared = None
    
    time_stamp = int(time_stamp)
    if not max_time_downloaded or time_stamp > max_time_downloaded:
        max_time_downloaded = time_stamp
    
    if listener_id not in unique_listeners:
        unique_listeners.add(listener_id)
    
    if listener_id not in listener_usage_count:
        listener_usage_count[listener_id] = 1
    else:
        listener_usage_count[listener_id] += 1
    
    if not max_time_shared or time_stamp > max_time_shared:
        max_time_shared = time_stamp

print("-------------------------------------------------------------------------")

if current_track_id:
    print(f"\n{current_track_id}\t\t{max_time_downloaded}\t\t{len(unique_listeners)}\t\t{','.join([f'{listener}:{listener_usage_count[listener]}' for listener in listener_usage_count])}\t\t{max_time_shared}\n")
