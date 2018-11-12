def firstCond(first_vertical, first_horizontal, second_vertical, second_horizontal):
    return abs(second_vertical - first_vertical) == 2


def secondCond(first_vertical, first_horizontal, second_vertical, second_horizontal):
    return abs(second_horizontal - first_horizontal) == 1


first_vertical = int(input('Please provide first vertical: '))
first_horizontal = int(input('Please provide first horizontal: '))
second_vertical = int(input('Please provide second vertical: '))
second_horizontal = int(input('Please provide second horizontal: '))


check = lambda foo: foo(first_vertical, first_horizontal, second_vertical, second_horizontal)


if all(map(check, [firstCond, secondCond])):
    print('YEEES')
