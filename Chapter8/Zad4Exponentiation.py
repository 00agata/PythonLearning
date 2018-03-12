'''
Given a positive real number a and a non-negative integer n.
Calculate a^n without using loops, ** operator
or the built in function.
'''


def power(a, n):
    if a > 0 and n >= 0:
        result = 1
        for i in range(0, n):
            result *= a
        return result
    else:
        print('Incorrect input values')


try:
    a = float(input('Input positive real number a: '))
    n = int(input('Input a non-negative integer n: '))
    power_a_n = power(a, n)
    print('a^n: {}'.format(power_a_n))
except NameError:
    print ('Incorrect Input Value. Program finished')
