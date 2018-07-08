'''
Date calculator - write a script that adds custom number of years,
days and hours and minutes to current date and
displays the result in human readable format
'''


import datetime
from datetime import timedelta
from datetime import date
from datetime import datetime


def calculate_date(yr, days, hours, minutes):
    today = date.today()

    custom_date = today.replace(year=today.year + yr)
    del_time = timedelta(days + (hours/24) + (minutes/(60*24)))
    custom_date = custom_date + del_time

    timestamp = custom_date.ctime()

    print(timestamp)


calculate_date(1, 1, 5, 0)
