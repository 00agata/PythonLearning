'''
Given a positive real number,
print its first digit of fractional part.
'''


number = float(input('Please, provide real number: '))
numberToString = str(number)

if ('.' in numberToString):
    idx = numberToString.find('.')
    print('Fractional part: {}'.format(numberToString[idx+1:idx+2]))
else:
    print('Fractional part does not exists')
