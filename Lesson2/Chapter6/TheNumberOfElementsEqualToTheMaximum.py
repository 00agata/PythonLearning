'''
A sequence consists of integer numbers and ends with the number 0.
Determine how many elements of this sequence are equal to
its largest element.
'''


# provide sequence of numbers


int_sequence = raw_input('provide integer numbers sequence: ')
int_sequence = str(int_sequence)
char_num = len(int_sequence)
int_table = []
for chars in range(0, char_num):
    int_table.append(int(int_sequence[chars]))
int_table.append(0)


# find maximum value


amount_of_max_equal = 0
maximum_number = max(int_table)
for num in int_table:
    if num == maximum_number:
        amount_of_max_equal += 1
print('There is {} numbers equal to MAX including MAX, which is {}'
      ''.format(amount_of_max_equal,maximum_number))
