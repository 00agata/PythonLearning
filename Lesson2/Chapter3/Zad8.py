'''
Created on 19 lut 2018

@author: agata.wiewiora



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
        if c - a == d - b:
            print('YES')
        else:
            print('NO')
    else:
        print('Incorrect input value') 
else:
    print('Incorrect input value')
