'''
Args sum - write a function called sum_all
that takes any number of arguments and returns their sum.
'''


def sum_all(*args):
    args_sum = 0
    for arg in args:
        if type(arg) in (int, float):
            args_sum = args_sum + arg
        else:
            print('Invalid argument {}'.format(arg))
    return args_sum


print(sum_all(1, 2, 3, 4, 'a'))

'''
args_sum = 0

while True:

    try:
        arg = int(input('Please, provide integer argument: '))

        if type(arg) == int:
            args_sum = args_sum + arg
            print('Sum equals: {}'.format(args_sum))
        else:
            print('Invalid arg. Please, provide proper arg')
    except ValueError:
        print('Invalid arg. Please, provide proper arg')

'''
