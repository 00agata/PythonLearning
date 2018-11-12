'''
The sequence consists of distinct positive integer
numbers and ends with the number 0.
Determine the value of the second largest element in this sequence.
It is guaranteed that the sequence has at least two elements.
'''


listOfNumbers = []
while True:
    listOfNumbers.append((list(int(i) for i in [int(input("Please "
                "provide positive integer: "))] if i >= 0))[0])

    if 0 in listOfNumbers:
        break

listOfNumbers.remove(max(listOfNumbers))
print('Second max: {}'.format(max(listOfNumbers)))




def closest_to_zero(input_list):
    return sorted(input_list, lambda x,y: abs(x)- abs(y))