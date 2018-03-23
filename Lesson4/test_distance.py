# test_distance.py

import math
import pytest


def distance_between_points(x_1, x_2, y_1, y_2):

    distance_square = ((x_2-x_1)**2 + (y_2-y_1)**2)

    distance = math.sqrt(distance_square)

    return distance

    def test_distance_between_points(self):

        with pytest.raises(TypeError):
            distance_between_points(1,1,2,2)
