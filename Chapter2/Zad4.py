'''
Created on 12 lut 2018

@author: agata.wiewiora

Given a positive real number, print its fractional part. 

'''
 

float_number = input("Please, provide sample real number: ")
if type(float_number) == float and float_number > 0:
    integer_part = int(float_number)
    fractional_part = float_number - integer_part
    print ('Fractional part is {}'.format(fractional_part))
else:
    print ('Incorrect input value')
