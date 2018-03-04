'''
Created on 14 lut 2018

@author: agata.wiewiora

Given three integers, print the smallest value. 

'''

a = int(input('Provide int a:'))
b = int(input('Provide int b:'))
c = int(input('Provide int c:'))

if type(a) == int and type(b) == int and type(c) == int:
    if (a == b == c):
        print ('All are equal')
    else:
        print ('Min of {}, {}, {}:'.format(a,b,c))
        print (min(a,b,c))
else:
    print ('Incorrect input value')
