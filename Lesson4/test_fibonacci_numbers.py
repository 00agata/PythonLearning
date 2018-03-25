# test_fibonacci_numbers.py

import pytest


# function to be tested - from Lesson3
def fib(n):
    if n is None:
        raise TypeError('None is incorrect input value')
    if type(n) == int:
        a = []
        a1 = 1  # id 1
        a2 = 1  # id 2
        a.append(a1)
        a.append(a2)

        if n == 0:
            return 0
        elif n == 1:
            return a1
        elif n == 2:
            return a2
        elif n > 2:
            print(a[a1])
            print(a[a2])
            for i in range(2, n):
                an = a[i-2] + a[i-1]
                a.append(an)
                print(an)
            return an
        else:
            raise ValueError('Incorrect input values')
    else:
        raise ValueError('Incorrect input value')


def test_fibonacci_type_error():
    with pytest.raises(TypeError):
        fib(None)


def test_fibonacci_value_error():
    with pytest.raises(ValueError):
        fib('aoeu')


def test_input_values():
    print('Test 0')
    assert fib(0) == 0
    print('Test 1')
    assert fib(1) == 1
    print('Test 2')
    assert fib(2) == 1
