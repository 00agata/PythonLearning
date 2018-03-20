'''
Created on 15 lut 2018

@author: agata.wiewiora

Given two cells of a chessboard. 
If they are painted in one color, print the word YES, 
and if in a different color - NO.

The program receives the input of four numbers from 1 to 8, 
each specifying the column and row number, 
first two - for the first cell, 
and then the last two - for the second cell. 

'''

a = int(input('first cell first parameter: '))
b = int(input('first cell second parameter: '))
c = int(input('second cell first parameter: '))
d = int(input('second cell second parameter: '))

if type(a) == int and type(b) == int and type(c) == int and type(d) == int:
    if 1 <= a <= 8 and 1 <= b <= 8 and 1 <= c <= 8 and 1 <= d <= 8:
        if (abs(c - a) + abs(d - b)) % 2 == 0:
            print('YES')
        else:
            print('NO')
    else:
        print('Incorrect input value')
else:
    print('Incorrect input value')
