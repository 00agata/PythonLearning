'''
Delta time calculator -
write a script that calculates time difference in days between
current date and custom date in the future.
'''


import time
import datetime


def calculate_delta_for_date(custom_date):
    custom_date_list = custom_date.split(" ")
    custom_year = (str(custom_date_list[0])).split('.')
    custom_time = (str(custom_date_list[1])).split(':')

    year = (int(custom_year[0]))
    month = (int(custom_year[1]))
    day = (int(custom_year[2]))

    hour = (int(custom_time[0]))
    minute = (int(custom_time[1]))
    second = (int(custom_time[2]))

    today = datetime.date.today()
    moment = datetime.datetime.now().time()
    now = datetime.datetime.combine(today, moment)
    my_other_datetime = datetime.datetime(year, month, day,
                                          hour, minute, second)

    delta = now - my_other_datetime
    delta_total_seconds = abs(int(delta.total_seconds()))

    # print(now)
    # print(my_other_datetime)
    # print(delta_total_seconds)
    return delta_total_seconds


custom_date = str(input('Provide custom date in following '
                        'format: 2018.06.10 18:26:19  '))
print('Delta seconds between current time and custom time is: {}'
      ''.format(calculate_delta_for_date(custom_date)))
