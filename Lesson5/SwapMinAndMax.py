import unittest

sample_list = [1, 2, 5, 6, 8]
sample_list_1 = [1, 1, 5, 8, 8]
sample_list_2 = [1, 2, 5, 8, 8]
sample_list_3 = [1, 1, 5, 6, 8]


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


class TestCollatz(unittest.TestCase):

    def test_if_expected_value(self):
        print(self.assertEqual(
            swap_min_and_max(sample_list_1),
            [1, 8, 5, 1, 8],
            '{}'.format(swap_min_and_max(sample_list_1))))
        print(self.assertEqual(
            swap_min_and_max(sample_list_2),
            [1, 2, 5, 8, 8],
            '{}'.format(swap_min_and_max(sample_list_2))))
        print(self.assertEqual(
            [1, 8, 5, 6, 1],
            swap_min_and_max(sample_list_3),
            '{}'.format(swap_min_and_max(sample_list_3))))
