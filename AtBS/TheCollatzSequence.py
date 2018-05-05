'''
Write a function named collatz() that has one parameter named number.
If number is even, then collatz() should print
number // 2 and return this value.
If number is odd, then collatz()
should print and return 3 * number + 1.
'''


def collatz(number):
    result = 0
    if number % 2 == 0:
        result = number // 2
        print(result)
    else:
        result = 3 * number + 1
        print(result)


try:
    user_number = input('Provide sample integer: ')
    user_number = int(user_number)

    print('Type of user input:')
    print(type(user_number))
    print()
    print('Current collatz result is: ')
    collatz(user_number)

except NameError:
    print('Incorrect input value')
