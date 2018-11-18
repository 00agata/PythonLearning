'''
Given an integer n, produce a two-dimensional
array of size (n×n) and complete it according
to the following rules, and print with a single
space between characters:

    On the main diagonal write 0 .
    On the diagonals adjacent to the main, write 1 .
    On the next adjacent diagonals write 2 and so forth.

Print the elements of the resulting array.
'''


def produce_parallel_diagonals(n):
    if n <= 0:
        raise ValueError('Value should be greater than 0')
    table = [[0] * n for i in range(n)]
    for i in range(n):
        for j in range(n):
            table[i][j] = n - abs(i-j)
    return table


n = int(input('Provide value: '))
for item in produce_parallel_diagonals(n):
    print(item)
