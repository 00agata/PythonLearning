'''
Created on 19 lut 2018

@author: agata.wiewiora

Chocolate bar has the form of a rectangle divided into nm portions.
Chocolate bar can be split into two rectangular parts 
by breaking it along a selected straight line on its pattern. 
Determine whether it is possible to split it so that one of 
the parts will have exactly k squares.

The program reads three integers: n, m, and k. It should print YES or NO.
'''


n = int(input('n: '))
m = int(input('m: '))
k = int(input('k: '))
line = int(input('line: '))
horizontal_or_vertical = int(input('Set 1 if horizontal, 0 if vertical division: '))

if type(n) == int and type(m) == int and type(k) == int and type(line) == int and type(horizontal_or_vertical) == int:
    whole_choc = n * m
    if (horizontal_or_vertical == 1):
        part_1 = n * (m - line)
        part_2 = whole_choc - part_1
        if (part_1 == k or part_2 == k):
            print('YES')
        else:
            print('NO')
    elif (horizontal_or_vertical == 0):
        part_1 = n * (m - line)
        part_2 = whole_choc - part_1
        if (part_1 == k or part_2 == k):
            print('YES')
        else:
            print('NO')
else:
    print('Invalid input value')
