import os
import re
import math


# def readfile(path):
#     with open(path, "r", encoding="utf-8") as f:    
#         line = f.readline()
#         while line:
#             line = f.readline()
#             newline = line.strip().split()
#             print(newline)

# readfile("planning.log")


# def act_time(hour):
time=['09:20','11:00']
totalSecs = 0
for tm in time:
    timeParts = [int(s) for s in tm.split(':')]
    totalSecs += (timeParts[0] * 60 + timeParts[1]) * 60
totalSecs, sec = divmod(totalSecs, 60)
hr, min = divmod(totalSecs, 60)
print ("%d:%02d:%02d" % (hr, min, sec))

# def hm_to_sec(hm_str):
#     h,m= (hm_str).rsplit(':',2)
#     return int(h)*60*60+int(m)*60
# print(hm_to_sec('1:04'))







# def time_pourcntg():
