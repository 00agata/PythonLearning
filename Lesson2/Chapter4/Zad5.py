'''
Created on 22 lut 2018

@author: agata.wiewiora

For the given integer N calculate the following sum: 

1^3 + 2^3 + ... + N^3

'''


N = int(input('How many numbers? '))
sum_of_numbers = 0

if type(N) == int and N > 0:
    for num in range(0, N+1):
        sum_of_numbers = sum_of_numbers + num ** 3
    print('Sum of N = {} numbers is : {}'.format(N, sum_of_numbers))
else:
    print('Invalid value. Program is finished')
