def firstCond(first_vertical, first_horizontal, second_vertical, second_horizontal):
    return first_vertical == second_vertical


def secondCond(first_vertical, first_horizontal, second_vertical, second_horizontal):
    return first_horizontal == second_horizontal


def thirdCond(first_vertical, first_horizontal, second_vertical, second_horizontal):
    if (abs(first_horizontal - second_horizontal) == abs(first_vertical - second_vertical)):
        return True


first_vertical = int(input('Please provide first vertical: '))
first_horizontal = int(input('Please provide first horizontal: '))
second_vertical = int(input('Please provide second vertical: '))
second_horizontal = int(input('Please provide second horizontal: '))


check = lambda foo: foo(first_vertical, first_horizontal, second_vertical, second_horizontal)


if any(map(check, [firstCond, secondCond, thirdCond])):
    print('YEEES')
