'''
Given a sequence of integers that end with a 0.
Print the sequence in reverse order.

Don't use lists or other data structures.
Use the force of recursion instead.
'''


def reverse_sequence(number):
    if number < 10:
        print(number, end='')
    else:
        print(number % 10, end='')
        reverse_sequence(number//10)


while True:
    num = int(input('Provide positive int, it should finish with 0: '))
    if num % 10 == 0 and num >= 0:
        break;
reverse_sequence(num)
