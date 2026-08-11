from systems.inventory import add_item


def shop(player):
    while True:
        print("\n--===Shop===--")
        print(f"Your Ryo: {player['ryo']}")

        print("1. Potion: 70")
        print("2. Kunai: 40")
        print("3. Exit Shop")
        choice_shop = input("Choose: ")

        if choice_shop == "1":
            if player["ryo"] >= 70:
                player["ryo"] -= 70
                add_item(player, "potion", 1)
                print(f"Ryo left: {player['ryo']}")
            else:
                print("You do not have enough Ryo.")

        elif choice_shop == "2":
            if player["ryo"] >= 40:
                player["ryo"] -= 40
                add_item(player, "kunai", 1)
                print(f"Ryo left: {player['ryo']}")
            else:
                print("You do not have enough Ryo.")

        elif choice_shop == "3":
            break