'''
Given two integers representing the rows and columns (mn),
and subsequent m rows of n elements, find the index position
of the maximum element and print two numbers representing
the index (ij) or the row number and the column number.
If there exist multiple such elements in different rows,
print the one with smaller row number. If there multiple such
elements occur on the same row, output the smallest column number.
'''

sample_table = [[1, 2, 3], [4, 5, 6]]


def max_sample_table(sample_table):
    id_i = 0
    id_j = 0
    max_value = 0

    for i in range(0, len(sample_table)):
        max_value = max(sample_table[i])
        if sample_table[id_i][id_j] < max_value:
            for j in range(0, len(sample_table[i])):
                if sample_table[i][j] == max_value:
                    id_i = i
                    id_j = j
                    break

    return (max_value, id_i, id_j)


def max_sample_table2(sample_table):
    max_row = 0
    max_col = 0
    max_value = sample_table[max_row][max_col]

    for row in range(len(sample_table)):
        for col in range(len(sample_table[row])):
            value = sample_table[row][col]
            if value > max_value:
                max_col, max_row, max_value = col, row, value

    return (max_value, max_row, max_col)


(max_val, id_i, id_j) = max_sample_table2(sample_table)
print(('Max value is: {}, at index: {}, {}').format(max_val, id_i, id_j))
