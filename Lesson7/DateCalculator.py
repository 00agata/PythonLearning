'''
Date calculator - write a script that adds custom number of years,
days and hours and minutes to current date and
displays the result in human readable format
'''


import time
import datetime


def calculate_date(yr, days, hr, min):
    timestamp = int(time.time())
    if yr % 4 == 0:
        added_seconds = (yr * 366 * 24 * 60  + hr * 60 + min) * 60
    else:
        added_seconds = (yr * 365 * 24 * 60 + hr * 60 + min) * 60
    requested_timestamp = timestamp + added_seconds
    print(time.ctime(int(requested_timestamp)))


calculate_date(1, 0, 0, 0)
