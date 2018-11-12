'''
The sequence consists of distinct positive integer
numbers and ends with the number 0.
Determine how many elements of this sequence
are equal to its largest element.
'''


listOfNumbers = []
listOfEquals = []
while True:
    listOfNumbers.append((list(int(i) for i in [int(input("Please "
                "provide positive integer: "))] if i >= 0))[0])

    if 0 in listOfNumbers:
        break

a = 0

for i in range (0, len(listOfNumbers)):
    if listOfNumbers[i] == max(listOfNumbers):
        a = a+1

print('Number of elements equals to max: {}'.format(a))
