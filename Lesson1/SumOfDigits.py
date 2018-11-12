'''
Given a three digit integer number, print sum of its digits.
'''


integer = int(input('Please, provide three digit integer: '))
integerString = str(integer)

if (len(integerString) == 3):
    print('Sum of digit: {}'.format(sum([int(a) for a in integerString])))
else:
    print('Improper amount of digits. Program finished')
