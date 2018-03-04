'''
Created on 22 lut 2018

@author: agata.wiewiora

For the given integer N calculate the following sum: 

1^3 + 2^3 + ... + N^3

'''


N = int(input('How many numbers? '))
sum_of_numbers = 0

if type(N) == int and N > 0:
    for nums in range (0,N):
        number = int(input('provide next number: '))
        if type(number) == int:
            sum_of_numbers = sum_of_numbers + number**3
        else:
            print('Invalid value')
            number = int(input('provide next valid number: '))
            sum_of_numbers = sum_of_numbers + number
            
    print('Sum of N = {} numbers is : {}'.format(N, sum_of_numbers))
else:
    print('Invalid value. Program is finished')
