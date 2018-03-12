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
        return result
    else:
        result = 3 * number + 1
        return result


try:
    user_number = input('Provide sample integer: ')
    user_number = int(user_number)

    print(type(user_number))

    collatz_result = collatz(user_number)
    print('Current collatz result is: {}'.format(collatz_result))
    while collatz_result != 1:
        collatz_result = collatz(collatz_result)
        print('Current collatz result is: {}'.format(collatz_result))

except NameError:
    print('Incorrect input value')
