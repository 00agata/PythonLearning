'''

'''

import math


def distance (x1, y1, x2, y2):
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)


x1 = float(input('x1: '))
x2 = float(input('x2: '))
y1 = float(input('y1: '))
y2 = float(input('y2: '))

print('{0:4.2f}'.format(distance(x1, x2, y1, y2), ))
