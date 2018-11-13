sample_list = [1, 2, 5, 6, 8]


def swap_min_and_max(list):
    if list is not None:
        min_elem = min(list)
        min_elem_id = list.index(min_elem)
        max_elem = max(list)
        max_elem_id = list.index(max_elem)
        list[min_elem_id] = max_elem
        list[max_elem_id] = min_elem
        return list
    return None


print(swap_min_and_max(sample_list))
