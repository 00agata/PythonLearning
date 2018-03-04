'''
Created on 23 lut 2018

@author: agata.wiewiora

Factorial for N
'''


N = int(input('Factorial N? '))
factorial = 1

if type(N) == int and N > 0:
    for nums in range (1,N+1):
        factorial = factorial * nums
    print('N factorial is : {}'.format(factorial))
else:
    print('Invalid value. Program is finished')
