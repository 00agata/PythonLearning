'''


'''


# inventory

stuff = {'arrow': 12, 'gold coin': 42, 'rope': 1, 'torch': 6, 'dagger': '1'}


def display_inventory(inventory):
    print('Inventory: ')
    item_total = 0
    for k, v in inventory.items():
        print('{}: {}'.format(k, v))
        item_total = item_total + int(v)
    print('Total number of items: {}'.format(item_total))


display_inventory(stuff)


dragonLoot = {'gold coin', 'dagger', 'gold coin', 'ruby'}


def add_to_inventory(inventory, added_items):
    for item in added_items:
        if item in inventory.keys():
            inventory[item] = int(inventory[item]) + 1
        else:
            inventory.setdefault(item, 1)
    print inventory


print('Added inventory: {}'.format(dragonLoot))
add_to_inventory(stuff, dragonLoot)
