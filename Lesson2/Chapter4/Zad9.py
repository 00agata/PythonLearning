'''
Created on 26 lut 2018

@author: agata.wiewiora

For given integer n <= 9 print a ladder of n steps. 
The k-th step consists of the integers from 1 to k 
without spaces between them.

To do that, you can use the sep and end arguments 
for the function print(). 

'''


n = int(input('provide n < 9:'))
step = ''

if n <= 9:
    for nums in range(1, n+1):
        number = str(nums)
        step = step + number 
        print('Step {} is {}'.format(nums, step))
else:
    print('Incorrect input value')
