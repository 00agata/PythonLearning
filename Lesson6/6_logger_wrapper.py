'''
Logger wrapper - write a function called logger_wrapper
that wraps call to any function in order to log passed args.
The function must take foo, *args and **kwargs, prints
args and **kwargs in human readable format and finally call
foo with args and kwargs
'''


def foo(*args, **kwargs):
    print('Foo')
    print(args)
    print(kwargs)


def logger_wrapper(fun, *args, **kwargs):
    print('args: ')
    for arg in args:
        print(arg)
    print('kwargs: ')
    for kwarg in kwargs:
        print(kwarg)

    print('Executing function started')
    fun(*args, **kwargs)


logger_wrapper(foo, 1, 2, third = 3)
