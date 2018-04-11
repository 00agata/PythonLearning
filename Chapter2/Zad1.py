'''
Created on 31 sty 2018

@author: agata.wiewiora

Prints last digit of the integer

'''


integer = input("Please, provide sample integer: ")
if type(integer) == int:
    last_digit = integer % 10
    print ('Last digit is {}'.format(last_digit))
else:
    print ('Incorrect input value')
