'''
Given a list of unique numbers, swap the minimal and maximal elements
of this list. Print the resulting list.
'''


sample_list = [0, 1, 2, 3, 4, 5, 6]


def swap_min_and_max_from_the_list(sample_list):
    min_value = min(sample_list)
    min_index = sample_list.index(min_value)
    max_value = max(sample_list)
    max_index = sample_list.index(max_value)
    sample_list[min_index] = max_value
    sample_list[max_index] = min_value
    print sample_list


swap_min_and_max_from_the_list(sample_list)
sample_list = [0, 0, 0, 0, 0, 0, 0]
swap_min_and_max_from_the_list(sample_list)