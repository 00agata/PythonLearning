'''
Write a function named printTable()
that takes a list of lists of strings
and displays it in a well-organized
table with each column right-justified.
'''


table_data = [['apples', 'oranges', 'cherries', 'bobs'],
              ['Alice', 'Bob', 'David', 'Mark'],
              ['dogs', 'cats', 'goose', 'birds']]


def print_table(table_data):
    row_amount = []
    new_row = []
    for n in range(1, len(table_data)+1):
        row_amount.append((max([len(str(item)) for item in tableData[n-1]])))

    for i in range(1, (len(table_data[0])+1)):
        for k in range(1, len(table_data)+1):
            new_row.append([table_data[k-1][i-1]])
        for j in range(1, len(new_row)+1):
            for item in new_row[j-1]:
                val = item
            if (j == 1):
                val = val.rjust((row_amount[j - 1]), ' ')
                print(val, end=" ")
            elif (j == len(new_row)+1):
                val = val.rjust((row_amount[j - 1]), ' ')
                print(val)
            else:
                val = val.center((row_amount[j - 1]), ' ')
                print(val, end=" ")
        print()
        new_row = []


print_table(table_data)
