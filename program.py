# Simulates a corrupted gauntlet run and its resulting rewards
# Reward chest contains three regular drop rolls, including shards and a roll on the unique table

import random

# 'Regular' drops
regdrops = {1 : "Rune full helm", 2 : "Rune chainbody", 3 : "Rune platebody", 
            4 : "Rune platelegs", 5 : "Rune plateskirt", 6 : "Rune halberd",
            7 : "Rune pickaxe", 8 : "Cosmic rune", 9 : "Nature rune",
            10 : "Law rune", 11 : "Chaos rune", 12 : "Death rune",
            13 : "Blood rune", 14 : "Mithril arrow", 15 : "Adamant arrow",
            16 : "Rune arrow", 17 : "Dragon arrow", 18 : "Uncut sapphire",
            19 : "Uncut emerald", 20 : "Uncut ruby", 21 : "Uncut diamond", 22 : "Battlestaff"}

def droptable():
    randomlist = []
    for i in range(0, 3):
        n = random.randint(1, 48)
        randomlist.append(n)

    for x in range(0, 3, 1):
        if 1 <= randomlist[x] <= 44:
            print(f"{regdrops.get(random.randint(1,22))}: {randomlist[x]}")
        elif 45 <= randomlist[x] <= 47:
            print(f"Coins: {randomlist[x]}")
        else:
            print(f"Dragon halberd: {randomlist[x]}")
    
    crystals = random.randint(5,9)
    print(f"Crystal shards: {crystals}")

    tertiary = random.randint(1, 800)
    if 1 <= tertiary <= 759:
        print(f"None ({tertiary})")
    elif 760 <= tertiary <= 783:
        print(f"Clue scroll (elite) ({tertiary})")
    elif 784 <= tertiary <= 797:
        q = random.randint(1,2)
        if(q == 1):
            print(f"Crystal weapon seed ({tertiary})")
        else:
            print(f"Crystal armour seed ({tertiary})")
    elif 798 <= tertiary <= 799:
        print(f"Enhanced crystal weapon seed ({tertiary})")
    else:
        print(f"Yungllef ({tertiary})")

    # def findEnhanced():
        # while True:
            # tertiary = random.randint(1, 800)
            # print(tertiary)
            # if rand in (798, 799):
                # break

    # def findYungllef():
        # while True:
            # tertiary = random.randint(1, 800)
            # print(tertiary)
            # if rand == 800:
                # break

    # findEnhanced()
    # findYungllef()

for z in range(3):
    droptable()
    print("\n")