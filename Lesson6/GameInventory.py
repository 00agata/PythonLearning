'''
Printing gamer inventory and adding some items to this inventory
'''

sample_inventory = {'rope': 1, 'torch': 6,
                    'gold coin': 42, 'dagger': 1, 'arrow': 12}


def print_inventory(inventory):
    for k, v in inventory.items():
        print('{} : {}'.format(k, v))


def add_inventory(inventory, item):
    if item in inventory.keys():
        inventory[item] += 1


print_inventory(sample_inventory)
add_inventory(sample_inventory, 'rope')
add_inventory(sample_inventory, 'bottle')
print()
print_inventory(sample_inventory)
