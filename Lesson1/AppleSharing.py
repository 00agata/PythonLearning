'''
N students take K apples and distribute them among each other evenly.
he remaining (the undivisible) part remains in the basket.
How many apples will each single student get?
How many apples will remain in the basket?
'''


students = int(input('Please provide number of students: '))
apples = int(input('Please provide number of apples: '))

print('Each student will receive {} apples'.format((apples//students)))
print('In the basket there will be {} apples left then'.format((apples%students)))
