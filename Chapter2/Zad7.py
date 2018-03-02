'''
Created on 13 lut 2018

@author: agata.wiewiora

Given the integer N - the number of minutes that is passed since midnight 
- how many hours and minutes are displayed on the 24h digital clock?

The program should print two numbers: the number of hours (between 0 and 23) 
and the number of minutes (between 0 and 59).

For example, if N = 150, then 150 minutes have passed since midnight 
- i.e. now is 2:30 am. So the program should print 2 30. 

'''


minutes_since_midnight = int(input('Please, provide the number of minutes since midnight: ' ))
if type(minutes_since_midnight) == int and minutes_since_midnight > 0:
    hours = int(minutes_since_midnight / 60)
    minutes_rest = minutes_since_midnight % 60
    if minutes_rest < 10:
        minutes_rest = str(minutes_rest)
        minutes_rest = '0' + minutes_rest
    if hours < 24:
        print('Current time is {}:{}'.format(hours, minutes_rest))
    elif hours == 24:
        print('Current time is 00:{}'.format(minutes_rest))
    elif hours > 24:
        day = 24*60
        days = int(minutes_since_midnight/day)
        hours = (minutes_since_midnight - days * day)/60
        print('Current time is {}:{}'.format(hours, minutes_rest))
else:
    print('Incorrect input value')
