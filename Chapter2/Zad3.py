'''
Created on 12 lut 2018

@author: agata.wiewiora

Given a three-digit number. Find the sum of its digits. 

'''

integer = input("Please, provide sample three-digit integer: ")
if type(integer) == int and integer > 99 and integer < 1000 :
    ones_digit = integer % 10
    print('ones {}'.format(ones_digit))
    hundreds_digit = integer / 100
    print('hundreds {}'.format(hundreds_digit))
    tens_digit = (integer / 10) % 10
    print('tens {}'.format(tens_digit))
    sum_of_digits = ones_digit + tens_digit + hundreds_digit
    print('Sum of all digits is {}'.format(sum_of_digits))
else:
    print('Incorrect input value')
