'''
Write a function named printTable()
that takes a list of lists of strings
and displays it in a well-organized
table with each column right-justified.
'''


tableData = [['apples', 'oranges', 'cherries', 'bobs'],
             ['Alice', 'Bob', 'David', 'Mark'],
             ['dogs', 'cats', 'goose', 'birds']]



def print_table(tableData):
    rowAmount = []
    newRow = []
    for n in range(1, len(tableData)+1):
        rowAmount.append((max([len(str(item)) for item in tableData[n-1]])))

    for i in range(1, (len(tableData[0])+1)):
        for k in range(1, len(tableData)+1):
            newRow.append([tableData[k-1][i-1]])
        for j in range(1, len(newRow)+1):
            for item in newRow[j-1]:
                val = item
            if (j == 1):
                val = val.rjust((rowAmount[j - 1]), ' ')
                print(val, end=" ")
            elif (j == len(newRow)+1):
                val = val.rjust((rowAmount[j - 1]), ' ')
                print(val)
            else:
                val = val.center((rowAmount[j - 1]), ' ')
                print(val, end=" ")
        print()
        newRow = []


print_table(tableData)
