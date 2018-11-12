# test_fibonacci_numbers.py

import pytest


# function to be tested - from Lesson3
def fib(n):
    if n is not None:
        if type(n) == int:
            a = []
            a1 = 1  # id 1
            a2 = 1  # id 2
            a.append(a1)
            a.append(a2)

            if n == 0:
                return 0  # id 0
            elif n == 1:
                return a1  # id 1
            elif n == 2:
                return a2  # id 2
            elif n > 2:
                print(a[a1])
                print(a[a2])
                for i in range(2, n):
                    an = a[i-2] + a[i-1]
                    a.append(an)
                    print(an)
                return an
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
    assert fib(0) == 0
    print('Test 1')
    assert fib(1) == 1
    print('Test 2')
    assert fib(2) == 1
    print('Test 5')
    assert fib(5) == 5
    print('Test 10')
    assert fib(10) == 55
