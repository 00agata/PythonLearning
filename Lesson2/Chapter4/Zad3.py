'''
Created on 22 lut 2018

@author: agata.wiewiora

10 numbers are given in the input. 
Read them and print their sum. Use as few variables as you can.

'''

sum_of_numbers = 0

for nums in range(0, 10):
    number = int(input('provide next number: '))
    if type(number) == int:
        sum_of_numbers = sum_of_numbers + number
    else:
        print('Invalid value')
        number = int(input('provide next valid number: '))
        sum_of_numbers = sum_of_numbers + number

print('Sum: {}'.format(sum_of_numbers))
