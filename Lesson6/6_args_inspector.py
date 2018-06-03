'''
Args inspector - write a function called
inspect_args that prints passed args and kwargs
in human-readable format.
'''


def inspect_args(*args, **kwargs):
    for arg in args:
        print('arg')
        print(arg)
    for kwarg in kwargs:
        print('kwarg')
        print(kwarg)


inspect_args(1, 2, 3, {'ala': 'ala', 'ola': 'ola'})
inspect_args(1, 2.0, third='3')
