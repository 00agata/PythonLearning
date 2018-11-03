
first_vertical = int(input('Please provide first vertical: '))
first_horizontal = int(input('Please provide first horizontal: '))
second_vertical = int(input('Please provide second vertical: '))
second_horizontal = int(input('Please provide second horizontal: '))


if (abs(first_horizontal - second_horizontal) == abs(first_vertical - second_vertical)):
    print('Yes, it can move')
else:
    print('No it cannot move')
