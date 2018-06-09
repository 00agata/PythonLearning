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
    colWidths = [0] * len(tableData)
    idColWidths = len(colWidths) +1
    max_str = []
    for i in range(1, (len(tableData[0])+1)):
        for k in range(1, idColWidths):
            max_str.append([tableData[k-1][i-1]])
        colWidths.append(max([len(item) for item in max_str]))
        max_str = []

    for i in range(1, len(tableData[0])+1):
        for j in range(1, idColWidths):
            val = tableData[j-1][i-1]
            if(j == 1):
                val = val.ljust((colWidths[j-1] - len(val)), ' ')
                print(val, end=" ")
            elif(j == idColWidths + 1):
                val = val.rjust((colWidths[j-1] - len(val)), ' ')
                print(val)
            else:
                val = val.center((colWidths[j-1] - len(val)), ' ')
                print(val, end=" ")


print_table(tableData)
