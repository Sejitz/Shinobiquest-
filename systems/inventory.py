from systems.save_system import save_game


def add_item(player, item, amount=1):
    if item in player["inventory"]:
        player["inventory"][item] += amount
    else:
        player["inventory"][item] = amount

    print(f"{amount}x {item} added to your Inventory.")
    save_game(player)


def inventory(player):
    print("\n--===Inventory===--")

    if player["inventory"] == {}:
        print("Your Inventory Is Empty")
    else:
        for item in player["inventory"]:
            print(f"{item}: x{player['inventory'][item]}")

    while True:
        print("\nUse item's 1st letter to choose.\nEg. [p] for 'Potion'")
        print("1. Exit Inventory\n")

        choice_inventory = input("Choose i: ").lower()

        if choice_inventory == "p":
            if player["inventory"]["potion"] <= 0:
                print("You do not have any potion!")
                continue

            if player["hp"] >= player["max_hp"]:
                print("Your Hp is full!")
                continue

            player["hp"] += 60
            player["inventory"]["potion"] -= 1

            print("60 Hp has been healed!")
            print(f"Potion left {player['inventory']['potion']}")

            if player["hp"] > player["max_hp"]:
                player["hp"] = player["max_hp"]

            print(f"Current HP: {player['hp']}")

            save_game(player)

        elif choice_inventory == "1":
            break