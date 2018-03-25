# test_distance.py

import math
import pytest


# function to be tested - from Lesson3
def distance_between_points(x_1, x_2, y_1, y_2):
    if x_1 is None or x_2 is None or y_1 is None or y_2 is None:
        raise TypeError('None is incorrect input value')
    if type(x_1) == int and type(x_2) == int and type(y_1) == int \
            and type(y_2) == int:
        distance = math.sqrt((x_2-x_1)**2 + (y_2-y_1)**2)
        return distance
    else:
        raise ValueError('Incorrect input value')


def test_distance_type_error():
    with pytest.raises(TypeError):
        distance_between_points(None)


def test_distance_value_error():
    with pytest.raises(ValueError):
        distance_between_points('aoeu')


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
