'''
Created on 23 lut 2018

@author: agata.wiewiora

Given N numbers: the first number in the input is N, 
after that N integers are given. 
Count the number of zeros among the given integers and print it.

You need to count the number of numbers 
that are equal to zero, not the number of zero digits. 

'''

N = int(input('N '))
sum_of_zeros = 0

if type(N) == int and N > 0:
    for nums in range(0, N):
        number = int(input('provide next number: '))
        if type(number) == int:
            if number == 0:
                sum_of_zeros = sum_of_zeros + 1
        else:
            print('Invalid value')
            
    print('There is {} of  0 in given number '.format(sum_of_zeros))
else:
    print('Invalid value. Program is finished')
