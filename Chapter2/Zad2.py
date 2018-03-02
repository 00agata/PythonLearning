'''
Created on 1 lut 2018

@author: agata.wiewiora

Prints tens digit of the integer

'''


integer = input("Please, provide sample integer: ")
if type(integer) == int:
    tens_digit = integer / 10
    print ('Tens digit is {}'.format(tens_digit))
else:
    print ('Incorrect input value')
