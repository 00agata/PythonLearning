'''
Number's filter
'''


def filter_list_for_required_range(list, range):
    list_of_ints = [int(item) for item in list]
    filtered_list = [numb for numb in list_of_ints if numb >= range]
    return filtered_list


sample_list = ['1', '2', '3', '5', '8']
print(filter_list_for_required_range(sample_list, 5))
