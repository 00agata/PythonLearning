'''
Timestamp to date - write a script that converts
unix timestamp to human-readable date format
'''


import time

timestamp = int(time.time())

print(time.ctime(int(timestamp)))
