'''
Created on 12 lut 2018

@author: agata.wiewiora

Given a positive real number, print its first digit to the right of the decimal point. 

'''


float_number = input("Please, provide sample real number: ")
if type(float_number) == float and float_number > 0:
    integer_part = int(float_number)
    fractional_part = float_number - integer_part
    fractional_part_tens = fractional_part * 10
    first_digit_of_fractional_part = int(fractional_part_tens)
    print ('Fractional part\'s first digit is {}'.format(first_digit_of_fractional_part))
else:
    print ('Incorrect input value')
