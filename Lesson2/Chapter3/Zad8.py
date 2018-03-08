'''
Created on 19 lut 2018

@author: agata.wiewiora

In chess, the bishop moves diagonally, any number of squares.
 Given two different squares of the chessboard,
 determine whether a bishop can go from the first
 to the second in one move.
'''


a = int(input('first cell first parameter: '))
b = int(input('first cell second parameter: '))
c = int(input('second cell first parameter: '))
d = int(input('second cell second parameter: '))


'''
start: (a,b)
stop: (c,d)


'''


if type(a) == int and type(b) == int and type(c) == int and type(d) == int:
    if 1 <= a <= 8 and 1 <= b <= 8 and 1 <= c <= 8 and 1 <= d <= 8:
        if abs(c - a) == abs(d - b):
            print('YES')
        else:
            print('NO')
    else:
        print('Incorrect input value') 
else:
    print('Incorrect input value')
