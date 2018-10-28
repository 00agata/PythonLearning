'''
Given a positive real number, print its fractional part.
'''


number = float(input('Please, provide real number: '))
numberToString = str(number)

if ('.' in numberToString):
    idx = numberToString.find('.')
    print('Fractional part: {}'.format(numberToString[idx:]))
else:
    print('Fractional part does not exists')
