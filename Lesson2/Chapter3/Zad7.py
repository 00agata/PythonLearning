'''
Created on 15 lut 2018

@author: agata.wiewiora

Chess king moves horizontally, vertically or diagonally to any adjacent cell.
Given two different cells of the chessboard, 
determine whether a king can go from the first cell 
to the second in one move.

The program receives the input of four numbers from 1 to 8,
 each specifying the column and row number, 
 first two - for the first cell, 
 and then the last two - for the second cell. 
 The program should output YES if a king can go from the first 
 cell to the second in one move, or NO otherwise. 

'''


a = int(input('first cell first parameter: '))
b = int(input('first cell second parameter: '))
c = int(input('second cell first parameter: '))
d = int(input('second cell second parameter: '))


'''
start: (a,b)
stop: (c,d)
Possible moves:
(a,b+1),(a,b-1),
(a-1,b-1),(a-1,b),(a-1,b+1),
(a+1,b-1),(a+1,b),(a+1,b+1)

'''


if type(a) == int and type(b) == int and type(c) == int and type(d) == int:
    if 1 <= a <= 8 and 1 <= b <= 8 and 1 <= c <= 8 and 1 <= d <= 8:
        if (abs((c - a) * (d - b)) == 0 and (abs(c - a) == 1 or abs(d - b) == 1)) \
                or abs((c - a) * (d - b)) == 1:
            print('YES')
        else:
            print('NO')
    else:
        print('Incorrect input value') 
else:
    print('Incorrect input value')  
