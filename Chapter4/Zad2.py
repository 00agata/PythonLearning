'''
Created on 22 lut 2018

@author: agata.wiewiora

Given two integers A and B. 
Print all numbers from A to B inclusively, in ascending order, 
if A < B, or in descending order, if A >= B. 

'''

A = int(input('please, provide A: '))
B = int(input('please, provide B: '))

if type(A) == int and type(B) == int:
    if A <= B:
        for numbers in range (A,B+1):
            print (numbers)
    elif A > B:
        for numbers in range (B,A+1):
            print (numbers)
else:
    print('Incorrect input value. Check, if A <=B ')
