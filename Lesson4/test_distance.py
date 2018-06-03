# test_distance.py

import math
import pytest


# function to be tested - from Lesson3
def distance_between_points(x_1, x_2, y_1, y_2):
    if None not in [x_1, x_2, y_1, y_2]:
        if type(x_1) == int and type(x_2) == int and type(y_1) == int \
                and type(y_2) == int:
            if [1000, 1000, 1000, 1000] > [x_1, x_2, y_1, y_2] \
                    > [-1000, -1000, -1000, -1000]:
                distance = math.sqrt((x_2-x_1)**2 + (y_2-y_1)**2)
                return distance
            else:
                raise ValueError('Incorrect input value. \
                Please provide values from (-1000, 1000)')
        else:
            raise TypeError('Invalid input value')
    else:
        raise TypeError('None is incorrect input value')


def test_distance_type_error_for_none_value():
    with pytest.raises(TypeError):
        distance_between_points(None)


def test_distance_type_error():
    with pytest.raises(TypeError):
        distance_between_points('ala', 'ola', 'ula', 'ela')


def test_distance_value_error():
    with pytest.raises(ValueError):
        distance_between_points(23444, 567, 3466, 97096)


def test_input_values():
    print('Test zero length')
    assert distance_between_points(0, 0, 0, 0) == 0
    print('Test negative coordinates')
    assert distance_between_points(-1, -1, -4, -6) == 2
    print('Test vertical distance')
    assert distance_between_points(0, 0, 4, 6) == 2
    print('Test horizontal distance')
    assert distance_between_points(4, 6, 0, 0) == 2
    print('Test normal conditions - difference on both coordinates')
    assert distance_between_points(4, 6, 1, 0) == math.sqrt((6-4)**2 + (0-1)**2)
    print('Test that the order of points does not matter')
    assert distance_between_points(6, 4, 1, 0) == distance_between_points(4, 6, 1, 0)
