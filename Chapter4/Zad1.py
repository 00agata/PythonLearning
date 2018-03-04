'''
Created on 22 lut 2018

@author: agata.wiewiora

Given two integers A and B (A <= B). 
Print all numbers from A to B inclusively.

'''


A = int(input('please, provide A: '))
B = int(input('please, provide B, B > A'))

if type(A) == int and type(B) == int and A <= B:
    for numbers in range (A,B+1):
        print (numbers)
else:
    print('Incorrect input value. Check, if A <=B ')
