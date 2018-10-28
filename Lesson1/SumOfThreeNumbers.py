'''
Write a program that takes three numbers and prints their sum.
Every number is given on a separate line.
'''


def take_numbers_from_user ():
    number1 = int(input('Please provide number: '))
    number2 = int(input('Please provide number: '))
    number3 = int(input('Please provide number: '))
    return([number1, number2, number3])


print('Sum of given integers is following:')
print(sum(take_numbers_from_user()))
