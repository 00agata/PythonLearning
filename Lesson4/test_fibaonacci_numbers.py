# test_fibonacci_numbers.py

import pytest


# function to be tested - from Lesson3
def fib(n):
    if n is not None:
        if type(n) == int:
            if n == 0:
                return 1
            if n == 1:
                return 1
            elif 1 < n <= 1000:
                return fib(n-1)+fib(n-2)
            elif n > 1000:
                raise ValueError('Max allowed value is 1000')
            else:
                raise ValueError('Incorrect input values')
        else:
            raise TypeError('Invalid input value')
    else:
        raise TypeError('None is incorrect input value')


def test_fibonacci_type_error():
    with pytest.raises(TypeError):
        fib(None)


def test_fibonacci_type_error2():
    with pytest.raises(TypeError):
        fib('aoeu')


def test_fibonacci_value_error():
    with pytest.raises(ValueError):
        fib(-5)


def test_input_values():
    print('Test 0')
    assert fib(0) == 1
    print('Test 1')
    assert fib(1) == 1
    print('Test 2')
    assert fib(2) == 1
    print('Test 5')
    assert fib(5) == 5
    print('Test 10')
    assert fib(10) == 55
