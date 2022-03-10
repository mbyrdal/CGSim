# Simulates a corrupted gauntlet run and its resulting rewards
# Reward chest contains three regular drop rolls, including shards and a roll on the unique table

import random

# Item IDs
regdrops = {0 : "Rune full helm", 1 : "Rune chainbody", 2 : "Rune platebody", 
            3 : "Rune platelegs", 4 : "Rune plateskirt", 5 : "Rune halberd",
            6 : "Rune pickaxe", 7 : "Cosmic rune", 8 : "Nature rune",
            9 : "Law rune", 10 : "Chaos rune", 11 : "Death rune",
            12 : "Blood rune", 13 : "Mithril arrow", 14 : "Adamant arrow",
            15 : "Rune arrow", 16 : "Dragon arrow", 17 : "Uncut sapphire",
            18 : "Uncut emerald", 19 : "Uncut ruby", 20 : "Uncut diamond", 21 : "Battlestaff"}
otherdrops = {22 : "Coins", 23 : "Dragon halberd"}

# Quantity ranges
quantity = [(3,5),(2,3),(2,2),(2,3),(2,3),(2,3),(2,3),
                (175,250),(125,150),(100,150),(200,350),
                (125,175),(100,150),(1000,1500),(500,725),
                (250,450),(50,100),(25,65),(15,60),(10,40),(5,15),(8,12)]
quantityspecial = [(75000,150000),(1,2)]

def randomizeamount(item_id):
    if item_id == 22:
        q = random.randint(quantityspecial[0][0], quantityspecial[0][1])
    elif item_id == 23:
        q = random.randint(quantityspecial[1][0], quantityspecial[1][1])
    else:
        q = random.randint(quantity[item_id][0], quantity[item_id][1])
    return q


def droptable():
    randomlist = []
    for i in range(0, 3):
        n = random.randint(1, 48)
        randomlist.append(n)

    # Name (Quantity): Roll number

    for x in range(0, 3, 1):
        if 1 <= randomlist[x] <= 44:
            rand = random.randint(0,21)
            print(f"{regdrops.get(rand)} ({randomizeamount(rand)}): {randomlist[x]}")
        elif 45 <= randomlist[x] <= 47:
            print(f"{otherdrops.get(22)} ({randomizeamount(22)}): {randomlist[x]}")
        else:
            print(f"{otherdrops.get(23)} ({randomizeamount(23)}): {randomlist[x]}")
    
    crystals = random.randint(5,9)
    print(f"Crystal shards ({crystals})")

    tertiary = random.randint(1, 800)
    if 1 <= tertiary <= 759:
        print(f"None: {tertiary}")
    elif 760 <= tertiary <= 783:
        print(f"Clue scroll (elite): {tertiary}")
    elif 784 <= tertiary <= 797:
        q = random.randint(1,2)
        if(q == 1):
            print(f"Crystal weapon seed: {tertiary}")
        else:
            print(f"Crystal armour seed: {tertiary}")
    elif 798 <= tertiary <= 799:
        print(f"Enhanced crystal weapon seed: {tertiary}")
    else:
        print(f"Yungllef: {tertiary}")

for z in range(3):
    droptable()
    print("\n")