'''
Timestamp to date - write a script that converts
unix timestamp to human-readable date format
'''


import time
#import datetime
timestamp = int(time.time())

# pure
# print(timestamp)

# without local time zone
# print(datetime.datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S'))

# complete
print(time.ctime(int(timestamp)))
