'''
Created on 19 lut 2018

@author: agata.wiewiora

Chess knight moves like the letter L. 
It can move two cells horizontally and one cell vertically, 
or two cells vertically and one cells horizontally. 
Given two different cells of the chessboard, 
determine whether a knight can go 
from the first cell to the second in one move. 

'''


a = int(input('first cell first parameter: '))
b = int(input('first cell second parameter: '))
c = int(input('second cell first parameter: '))
d = int(input('second cell second parameter: '))


'''
start: (a,b)
stop: (c,d)
Possible movements:
(a-1,b-2),(a-1,b+2),(a+1,b+2),(a+1,b-2)
(a-2,b-1),(a-2,b+1),(a+2,b+1),(a+2,b-1)

'''


if type(a) == int and type(b) == int and type(c) == int and type(d) == int:
    if 1 <= a <= 8 and 1 <= b <= 8 and 1 <= c <= 8 and 1 <= d <= 8:
        possible_movements = [(a-1,b-2),(a-1,b+2),(a+1,b+2),(a+1,b-2),(a-2,b-1),\
                              (a-2,b+1),(a+2,b+1),(a+2,b-1)]
        if (c,d) in possible_movements:
            print('YES')
        else:
            print('NO')
    else:
        print('Incorrect input value. Knight will not go there') 
else:
    print('Incorrect input value')
