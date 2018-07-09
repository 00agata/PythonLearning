'''
Date printer - write a script that displays current date
in human-readable format
'''

import datetime

print('First way: ')
today = datetime.date.today()
print(today)


def print_current_date():
    mylist = []
    today = datetime.date.today()
    mylist.append(str(today))
    for item in mylist:
        date = item
    return date


print('Second way: ')
print('Today is {}'.format(print_current_date()))
