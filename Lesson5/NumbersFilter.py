'''
Numbers filter - using list comprehensions write a function
that casts list of strings to list of integers and filters
numbers within supplied range. Example data:

list_of_strings = ['2', '0', '8', '3']
to_filter_range = range(3)
expected_output = [8, 3]
'''


def filter_numbers(string_list, filter):
    int_list = [int(element) for element in string_list if type(element) == str]
    filtered_list = [element for element in int_list if element >= filter ]
    print filtered_list


filter_numbers(['-2', '3', '5', '6'], 3)