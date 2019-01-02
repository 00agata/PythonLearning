'''
write a function called sum_all
that takes any number of arguments and returns their sum
'''


def sum_all(*args):
    sum = 0
    for item in args:
        if type(item) == int or type(item) == float:
            sum += item
    return sum


print(sum_all(2, 3, 4, 'ala'))
print(sum_all(2.9, 3, 4, 'ala'))
