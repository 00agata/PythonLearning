'''
A car can cover distance of N kilometers per day.
How many days will it take to cover a route of length M kilometers?
The program gets two numbers: N and M.
'''


import math

N = int(input('Please, provide integer, '
              'which is car velocity (km per day): '))
M = int(input('Please, provide integer, '
              'which is distance (km): '))

print('Car can cover the distance in {} days'.format(math.ceil(M/N)))
