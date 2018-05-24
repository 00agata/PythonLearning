'''

Alice and Bob like to play with colored cubes. Each child has its
own set of cubes and each cube has a distinct color,
but they want to know how many unique colors exist
if they combine their block sets. To determine this,
the kids enumerated each distinct color with
a random number from 0 to 10^8
N - lines contain the numerical color value for each cube in Alice's set
M - lines contain the numerical color value for each cube in Bob's set

Find three sets: the numerical colors of cubes in both sets,
the numerical colors of cubes only in Alice's set,
and the numerical colors of cubes only in Bob's set.
For each set, print the number of elements in the set,
followed by the numerical color elements, sorted in ascending order.
'''


import random

# Alice cubes:

N = int(input('Please setup Alice cubes amount: '))

# Bob cubes:

M = int(input('Please setup Bob cubes amount: '))


def setup_cubes_set(amount):
    cubes_set = set()
    for i in range(amount):
        cubes_set.add(random.randint(0, 10e8))
    return cubes_set


print('Alice set has {} elements, which are as follows: '.format(N))
alice_set = setup_cubes_set(N)

for cube in alice_set:
    print(cube)

print('Bob set has {} elements, which are as follows: '.format(M))
bob_set = setup_cubes_set(M)

for cube in setup_cubes_set(M):
    print(cube)

common_set = alice_set.union(bob_set)

print('Common set has {} elements, which are as follows: '.format(len(common_set)))

for cube in common_set:
    print(cube)
