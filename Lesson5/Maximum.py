'''

Given two integers representing the rows and columns (m×n),
and subsequent m rows of n elements,
find the index position of the maximum element and print
two numbers representing the index (i×j) or the row number
and the column number. If there exist multiple such elements
in different rows, print the one with smaller row number.
If there multiple such elements occur on the same row,
output the smallest column number.

'''

import random


def generate_table(n, m):
    if 10 < n <= 0 or 10 < m <= 0:
        raise ValueError('Value {} and {} '
                         'should fit 0 < value < 10'.format(n, m))
    table = [[0] * m for i in range(n)]

    for j in range(n):
        for k in range(m):
            table[k][j] = random.randint(0,10)
    return table


def find_max_in_table(table):
    max_rows = [[max(row), row.index(max(row))] for row in table]
    max_int = max([item[0] for item in max_rows])
    idx = [item[0] for item in max_rows].index(max_int)

    return [idx, max_rows[idx][1]]


n = int(input('n: '))
m = int(input('m: '))
sample_table = generate_table(n, m)
for item in sample_table:
    print(item)

print(find_max_in_table(sample_table))
