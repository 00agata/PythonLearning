'''
Given an integer n, produce a two-dimensional array of size (nn)
and complete it according to the following rules,
and print with a single space between characters:

    On the main diagonal write 0.
    On the diagonals adjacent to the main, write 1.
    On the next adjacent diagonals write 2 and so forth.

Print the elements of the resulting array.
'''


def produce_diagonal(n):
    table = [['.'] * n for k in range(n)]
    for row in range(n):
        for col in range(n):
            for p in range(0, n):
                if col == row - p or col == row + p:
                    table[row][col] = str(0 + p) + ' '

    for x in range(len(table)):
        print(table[x])
    return table


produce_diagonal(5)
