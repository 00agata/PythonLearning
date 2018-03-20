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

whole_choc = n * m

if k <= whole_choc:
    if k != 1:
        if whole_choc % k == 0 or k % n == 0 or k % m == 0:
            print('YES')
        else:
            print('NO')
    else:
        if whole_choc % k == 0 and (k % n == 0 or k % m == 0):
            print('YES')
        else:
            print('NO')
else:
    print('Invalid input value')
