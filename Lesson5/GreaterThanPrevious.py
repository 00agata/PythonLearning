list = [1, 3, 5, 6, 4, 8]


def greater_than_neighbours(sample_list):
    if sample_list is not None:
        new_list = [number for number in sample_list
                    if number > sample_list[sample_list.index(number) - 1]]
    return new_list


print(greater_than_neighbours(list))
