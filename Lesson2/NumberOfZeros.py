'''
Given N numbers: the first number in the input is N, after
that N integers are given.
Count the number of zeros among the given integers and print it.
You need to count the number of numbers that are equal to zero,
not the number of zero digits.
'''

numberOfZeros = 0

while(True):
    number = str(input('Provide integer: '))
    if type(number) == str:
        for i in list(number):
            if i == '0':
                numberOfZeros = numberOfZeros +1
        print('Number of zeros: {}'.format(numberOfZeros))
    else:
        print('Invalid input value')
