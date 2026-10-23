from systems.save_system import save_game


def add_item(player, item, amount=1):
    if item in player["inventory"]:
        player["inventory"][item] += amount
    else:
        player["inventory"][item] = amount

    # print(f"{amount}x {item} added to your Inventory.")
    save_game(player)


def heal(player):

    if player["inventory"]["potion"] <= 0:
        print("You do not have any potion!")
        

    elif player["hp"] >= player["max_hp"]:
        print("Your Hp is full!")
        
    else:
        player["hp"] += 60
        player["inventory"]["potion"] -= 1
    
        print("60 Hp has been healed!")

    if player["hp"] > player["max_hp"]:
        player["hp"] = player["max_hp"]


    save_game(player)

