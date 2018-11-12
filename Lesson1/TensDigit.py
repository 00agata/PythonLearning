'''
Given an integer number, print its tens digit.
'''


integer = int(input('Please, provide integer: '))
integerString = str(integer)

if (len(integerString) >= 2):
    print('Tens digit: {}'.format(integerString[-2]))
else:
    print('Tens digit: 0')
