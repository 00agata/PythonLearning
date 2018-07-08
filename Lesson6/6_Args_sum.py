'''
Args sum - write a function called sum_all
that takes any number of arguments and returns their sum.
'''


def sum_all(*args):
    args_sum = 0
    for arg in args:
        try:
            return sum(args)
        except TypeError:
            return None


print(sum_all(1, 2, 3, 4))
