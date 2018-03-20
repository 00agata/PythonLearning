'''

The sequence consists of distinct positive integer numbers 
and ends with the number 0.
Determine the value of the second largest element in this sequence.
It is guaranteed that the sequence has at least two elements.

'''


# provide sequence of numbers


int_sequence = raw_input('provide integer numbers sequence: ')
int_sequence = str(int_sequence)
char_num = len(int_sequence)
int_table = []
for chars in range(0,char_num):
    int_table.append(int(int_sequence[chars]))
int_table.append(0)

print('Numbers sequence:')
for num in int_table:
    print(num)


# find second maximum


int_table.remove(max(int_table))
print('Second maximum: {}'.format(max(int_table)))
