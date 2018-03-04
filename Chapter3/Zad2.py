'''
Created on 14 lut 2018

@author: agata.wiewiora

For the given integer X print 1 if it's positive, 
-1 if it's negative, or 0 if it's equal to zero.

Try to use the cascade if-elif-else for it. 

'''


X = int(input('Provide integer: '))

if type(X) == int:
    if X > 0:
        print('1')
    elif X == 0:
        print('0')
    else:
        print('-1')
else:
    print('Incorrect input value')
