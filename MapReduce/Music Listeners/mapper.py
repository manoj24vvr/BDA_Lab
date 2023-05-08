#!/usr/bin/python3

import sys

for line in sys.stdin:
    fields = line.strip().split("\t")
    if len(fields) != 5:
        continue
    track_id, time_stamp, event_type, listener_id, platform = fields
    if event_type == "Download":
        print(f"{track_id}\t{time_stamp}\t{listener_id}")
    elif event_type == "Share":
        print(f"{track_id}\t{time_stamp}\t{listener_id}")
