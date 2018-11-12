'''
Write a program that reads an integer
number and prints its previous and next numbers.
See the examples below for the exact format your answers should take.
There shouldn't be a space before the period.
'''

while(True):
    number = int(input('Please provide integer: '))
    if (-1000000 < number < 100000):
        print('Next:        {}'.format(number+1))
        print('Previous:    {}'.format(number-1))
        break;
    else:
        print('Please, provide number -1000000 < <<number>> < 100000')

