'''
Given two numbers n and m.
Create a two-dimensional array of size (nm)
and populate it with the characters "." and "*"
in a checkerboard pattern.
The top left corner should have the character "." .
'''


def populate_chess_board(n):
    table = [['.'] * n for k in range(n)]
    # print table
    # print type(table)
    for i in range(n):
        for j in range(n):
            if i % 2 == 0:
                if j % 2 != 0:
                    table[i][j] = '*'
            else:
                if j % 2 == 0:
                    table[i][j] = '*'
    return table


sample_table = populate_chess_board(5)
for x in range(len(sample_table)):
    print(sample_table[x])
