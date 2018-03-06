'''
Created on 14 lut 2018

@author: agata.wiewiora

Given two integers, print the smaller value. 

'''

a = int(input('Provide int a:'))
b = int(input('Provide int b:'))

if type(a) == int and type(b) == int:
    if (a == b):
        print('Both are equal')
    else:
        print('Min of {}, {}:'.format(a,b))
        print(min(a,b))
else:
    print('Incorrect input value')
