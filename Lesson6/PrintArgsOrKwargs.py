'''
Args inspector -
write a function called inspect_args
that prints passed args and kwargs in human-readable format.
'''


def print_all(*args, **kwargs):
    for item in args:
        print('{}: {}'.format(item, item))
    for key, value in kwargs.items():
        print("{}: {}".format(key, value))


print(print_all('ala', 5, new='ola', new1='ula'))
