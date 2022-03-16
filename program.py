import random
import json
import pprint

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
quantity_special = [(75000,150000),(1,2)]

# Prices
price = {0 : 20508, 1 : 29461, 2 : 38410, 3 : 37754,
         4 : 37858, 5 : 37612, 6 : 18682, 7 : 123,
	     8 : 189, 9 : 140, 10 : 60, 11 : 190,
	     12 : 304, 13 : 5, 14 : 26, 15 : 55,
	     16 : 1292, 17 : 368, 18 : 572, 19 : 1135,
	     20 : 2796, 21 : 8098}
price_special = {22 : 1, 23 : 148936}

# Generates a list of random number rolls (1 to 48) to be used in ID finding
# 0-indexed as [0, 1, 2]
def get_roll():
    random_rolls = []
    for i in range(0,3):
        n = random.randint(1,48)
        random_rolls.append(n)
    return random_rolls

# Generates the quantity of a specific item with item_id
# Integer value
def get_quantity(item_id):
    if item_id == 22:
        q = random.randint(quantity_special[0][0], quantity_special[0][1])
    elif item_id == 23:
        q = random.randint(quantity_special[1][0], quantity_special[1][1])
    else:
        q = random.randint(quantity[item_id][0], quantity[item_id][1])
    return q

# Generates the price of a specific item with item_id and quantity
# Integer value
def get_profit(item_id, quantity):
    if item_id == 22 or item_id == 23:
        p = quantity * price_special.get(item_id)
    else:
        p = quantity * price.get(item_id)
    return p
    
# Generates a dictionary object based on the rolls (regular drop)
def get_object(numlist):
    for x in range(0,3,1):
        if 1 <= numlist[x] <= 44:
            roll_value = numlist[x]
            id_value = random.randint(0,21)
            name_value = regdrops.get(id_value)
            quantity_value = get_quantity(id_value)
            profit_value = get_profit(id_value, quantity_value)
        elif 45 <= numlist[x] <= 47:
            roll_value = numlist[x]
            id_value = 22
            name_value = otherdrops.get(id_value)
            quantity_value = get_quantity(id_value)
            profit_value = get_profit(id_value, quantity_value)
        else:
            roll_value = numlist[x]
            id_value = 23
            name_value = otherdrops.get(id_value)
            quantity_value = get_quantity(id_value)
            profit_value = get_profit(id_value, quantity_value)
    return {"id": id_value, "name": name_value, 
            "quantity": quantity_value, "profit": profit_value, "roll": roll_value}    

# Generates a dictionary object based on the rolls (uniques)
def get_tertiary():
    temp = {}
    tertiary = random.randint(1,800)
    if 1 <= tertiary <= 759:
        roll_t = tertiary
        name_t = "None"
        quantity_t = 1
        profit_t = 0
    elif 760 <= tertiary <= 783:
        roll_t = tertiary
        name_t = "Clue scroll (elite)"
        quantity_t = 1
        profit_t = 0
    elif 784 <= tertiary <= 797:
        if random.randint(1,2) == 1:
            roll_t = tertiary
            name_t = "Crystal weapon seed"
            quantity_t = 1
            profit_t = 337976
        else:
            roll_t = tertiary
            name_t = "Crystal armour seed"
            quantity_t = 1
            profit_t = 6825541
    elif 798 <= tertiary <= 799:
        roll_t = tertiary
        name_t = "Enhanced crystal weapon seed"
        quantity_t = 1
        profit_t = 162804290
    else:
        roll_t = tertiary
        name_t = "Yungllef"
        quantity_t = 1
        profit_t = 0
    temp.update({"name_t": name_t, "quantity_t": quantity_t,
            "profit_t": profit_t, "roll_t": roll_t})
    return temp

# Compiles the program and runs it in order to generate reward chest loot + potential tertiary loot
def run():
    result = {}
    temp_list = get_roll()
    
    result.update(get_object(temp_list))
    result.update({"crystals": random.randint(5,9)})
    
    tertiary = get_tertiary()
    result["tertiary"] = tertiary
    
    return result

# Main program
completions = []
for x in range(3):
    completions.append(run())
# print_as_json(completions)
# print_simply(completions)
    
# Prints the list of dictionaries (completions) as JSON   
def print_as_json(completions_list):
    json_obj = json.dumps(completions_list, indent = 4)
    print(json_obj)

# Prints the list of dictionaries (completions) in a simple format
# Missing profit formatting (decimals x..k and x..m)
def print_simply(my_list):
    profit = 0
    for c in completions:
        if c['tertiary']['profit_t'] == 0:
            print(f'{c["name"]} (x{c["quantity"]}): {c["profit"]}')
            # print(f'{c['name']} ({c['quantity']}): {c['profit']}')
            profit += c["profit"]
        else:
            print(f'{c["name"]} (x{c["quantity"]}): {c["profit"]}')
            print(f'{c["tertiary"]["name_t"]} (x{c["tertiary"]["quantity_t"]}): {c["tertiary"]["profit_t"]}')
            profit += (c["profit"] + c["tertiary"]["profit_t"])
    
    print("\nTotal profit: ", profit)
