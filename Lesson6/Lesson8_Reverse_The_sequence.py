'''
print reversed sequence of integers
sequence ends with a 0
use recursion instread of data structures
'''


int_sequence = (9, 8, 7, 6, 5, 4, 3, 2, 1, 0)


def rev(l):
    if len(l) == 0:
        return []
    return [l[-1]] + rev(l[:-1])


new_seq = rev(int_sequence)
print(new_seq)
