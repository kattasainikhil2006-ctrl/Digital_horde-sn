inventory = {}

for fruit in fruit_list:
    inventory[fruit] = inventory.get(fruit, 0) + 1

return inventory
