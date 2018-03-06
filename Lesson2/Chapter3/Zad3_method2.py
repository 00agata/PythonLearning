'''
Created on 14 lut 2018

@author: agata.wiewiora

Given three integers, print the smallest value.

'''


first_integer = float(raw_input('first integer: '))
second_integer = float(raw_input('second integer: '))
third_integer = float(raw_input('third integer: '))

if first_integer == second_integer and first_integer == third_integer:
    print('All equal {}, {}, {}'.format(first_integer, second_integer,
                                        third_integer))
else:
    if first_integer > second_integer:
        if second_integer > third_integer:
            print(third_integer)
        elif second_integer == third_integer:
            print('{}, {}'.format(second_integer, third_integer))
        else:
            print(second_integer)
    elif first_integer == second_integer:
        if third_integer < second_integer:
            print(third_integer)
        else:
            print('{}, {}'.format(first_integer, second_integer))
