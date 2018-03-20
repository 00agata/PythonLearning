'''
Created on 22 lut 2018

@author: agata.wiewiora

N numbers are given in the input. 
Read them and print their sum.

The first line of input contains the integer N, 
which is the number of integers to follow. 
Each of the next N lines contains one integer. 
Print the sum of these N integers. 

'''


sum_of_numbers = 0

N = int(input('How many numbers? '))

if type(N) == int and N > 0:
    for nums in range(0, N):
        number = int(input('provide next number: '))
        if type(number) == int:
            sum_of_numbers = sum_of_numbers + number
        else:
            print('Invalid value')
            number = int(input('provide next valid number: '))
            sum_of_numbers = sum_of_numbers + number
            
    print('Sum of N = {} numbers is : {}'.format(N, sum_of_numbers))
else:
    print('Invalid value. Program is finished')
