'''
Given four real numbers representing cartesian coordinates:
(x1,y1),(x2,y2).
Write a function distance(x1, y1, x2, y2)
to compute the distance between the points (x1,y1) and (x2,y2).
Read four real numbers and print the resulting
distance calculated by the function.
'''

import math


def distance_between_points(x_1, x_2, y_1, y_2):
    distance_square = ((x_2-x_1)**2 + (y_2-y_1)**2)
    distance = math.sqrt(distance_square)
    return distance


try:
    x1 = input('Input x1: ')
    y1 = input('Input y1: ')
    x2 = input('Input x2: ')
    y2 = input('Input y2: ')
    distance_between_two_points = distance_between_points(x1, x2, y1, y2)
    print('Distance between points equals: {}'
          .format(distance_between_two_points))
except NameError:
    print ('Incorrect Input Value. Program finished')
