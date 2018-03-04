'''
Created on 23 lut 2018

@author: agata.wiewiora

Given an integer n, print the sum 1!+2!+3!+...+n!.

This problem has a solution with only one loop, so try to discover it.
And don't use the math library :) 

'''


n = int(input('provide n:'))
s = 0
i = 1

for nums in range (1,n+1):
    i = i * nums
    s = s + i
    print('Current factorial: {}'.format(i))
print('Sum o factorials: {}'.format(s))
