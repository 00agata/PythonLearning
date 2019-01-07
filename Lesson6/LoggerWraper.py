'''
Logger wrapper - write a function called logger_wrapper
 that wraps call to any function in order to log passed args.
The function must take foo, *args and **kwargs, prints
*args and **kwargs in human readable format and finally call
foo with args and kwargs
'''


def logger_wrapper(foo, *args, **kwargs):
    print(foo)
    print(args)
    print(kwargs)
    foo(*args, **kwargs)


def foo(*args, **kwargs):
    for item in args:
        print(item)
    for key, value in kwargs.items():
        print('{}: {}'.format(key, value))


logger_wraper(foo, 4, 5, 6, 7, name='ola', surname='nowak')
