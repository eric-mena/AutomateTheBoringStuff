#inventory.py

stuff = {'rope':1, 'torch':6, 'gold coin':42, 'dagger':1, 'arrow':12}

def displayInventory(inv):
    print("Inventory:")
    item_total = 0
    for i,j in inv.items():
        print(str(j) + ' ' + i)
        item_total += j
    print('Total number of items: ' + str(item_total))

displayInventory(stuff)

#inventoryUpdate.py

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def addToInventory(inventory, addedItems):
    for item in addedItems:
        #creates a key entry in INV for keys not there and assigns 0 value.
        inventory.setdefault(item,0)
        #increments the value for each key found in dragonLoot.
        inventory[item] += 1
    return inventory
    
invent = addToInventory(inv, dragonLoot)  
itemList(invent)
