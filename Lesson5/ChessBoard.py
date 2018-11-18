'''
Given two numbers n and m. Create a two-dimensional
array of size (n×m) and populate it with the
characters "." and "*" in a checkerboard pattern.
The top left corner should have the character "." .
'''


def generate_table_of_zeros(n, m):
    if 10 < n <= 0 or 10 < m <= 0 or n != m:
        raise ValueError('Value {} and {} ''should fit '
                         '0 < value < 10 and be equal'.format(n, m))
    table = [[0] * m for i in range(n)]
    return table


def populate_table_as_chess_board(table):
    for i in range(len(table[0])):
        for j in range(len(table)):
            if i % 2 == 0:
                if j % 2 == 0:
                    table[i][j] = '*'
                else:
                    table[i][j] = ' '
            if i % 2 != 0:
                if j % 2 == 0:
                    table[i][j] = ' '
                else:
                    table[i][j] = '*'
    return table


n = int(input('n: '))
m = int(input('m: '))
sample_table = generate_table_of_zeros(n, m)
sample_table = populate_table_as_chess_board(sample_table)
for item in sample_table:
    print(item)
