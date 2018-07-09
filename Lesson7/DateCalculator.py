'''
Date calculator - write a script that adds custom number of years,
days and hours and minutes to current date and
displays the result in human readable format
'''


import datetime
from datetime import timedelta


def calculate_date(yr, days, hours, minutes):
    today = datetime.date.today()

    custom_date = today.replace(year=today.year + yr)
    del_time = timedelta(days + (hours/24) + (minutes/(60*24)))
    custom_date = custom_date + del_time

    print(custom_date)


calculate_date(1, 1, 5, 0)
