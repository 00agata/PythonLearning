'''
Given a list of numbers, determine and print the quantity of elements
that are greater than both of their neighbors.

The first and the last items of the list shouldn't be considered
because they don't have two neighbors
'''

sample_list = [1, 2, 5, 3, 4, 6, 5]


def print_greater_than_neighbours(sample_list):
    n = len(sample_list)
    for i in range(0, n):
        if 0 < i < n:
            if sample_list[i-1] < sample_list[i] > sample_list[i+1]:
                print(sample_list[i])


print_greater_than_neighbours(sample_list)
