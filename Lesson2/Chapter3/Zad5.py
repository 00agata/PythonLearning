'''
Created on 15 lut 2018

@author: agata.wiewiora

Chess rook moves horizontally or vertically. 
Given two different cells of the chessboard, 
determine whether a rook can go from the first cell to the second in one move.

The program receives the input of four numbers from 1 to 8, 
each specifying the column and row number, first two - for the first cell, 
and then the last two - for the second cell. 
The program should output YES if a rook can go from the first cell 
to the second in one move, or NO otherwise. 

'''


a = int(input('first cell first parameter: '))
b = int(input('first cell second parameter: '))
c = int(input('second cell first parameter: '))
d = int(input('second cell second parameter: '))

if type(a) == int and type(b) == int and type(c) == int and type(d) == int:
    if 1 <= a <= 8 and 1 <= b <= 8 and 1 <= c <= 8 and 1 <= d <= 8:
        if c == a or d == b:
            print('YES')
        else:
            print('NO')        
    else:
        print('Incorrect input value') 
else:
    print('Incorrect input value')       
