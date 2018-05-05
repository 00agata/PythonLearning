'''
Given a positive real number a and integer n.

Compute a^n.
Write a function power(a, n) to calculate the
results using the function and print the result of the expression.

Don't use the same function from the standard library.
'''


def power(a, n):
    if a > 0 and n >= 0:
        result = 1
        for i in range(0, n):
            result *= a
        return result
    else:
        raise ValueError


try:
    a = input('Input a: ')
    n = int(input('Input n: '))
    power_a_n = power(a, n)
    print('a^n: {}'.format(power_a_n))
except (NameError, ValueError):
    print ('Incorrect Input Value. Program finished')
