'''
Created on 12 lut 2018

@author: agata.wiewiora

A car can cover distance of N kilometers per day. 
How many days will it take to cover a route of length M kilometers? 
The program gets two numbers: N and M.

'''


velocity = input("Please, provide information, how many kilometers can car do per day: ")
if type(velocity) == float or type(velocity) == int  and velocity > 0:
    distance = input("Please, provide the distance: ")
    if type(distance) == float or type(distance) == int and distance > 0:
        time = distance/velocity
        print ('You need {} days to do {} km distance'.format(time, distance))
    else:
        print ('Incorrect input value')
else:
    print ('Incorrect input value')
