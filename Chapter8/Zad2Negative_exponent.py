'''
Given a positive real number a and integer n.

Compute a^n.
Write a function power(a, n) to calculate the
results using the function and print the result of the expression.

Don't use the same function from the standard library.
'''


def power(a, n):
    result = a**n
    return result


try:
    a = input('Input a: ')
    n = int(input('Input n: '))
    power_a_n = power(a, n)
    print('a^n: {}'.format(power_a_n))
except NameError:
    print ('Incorrect Input Value. Program finished')
