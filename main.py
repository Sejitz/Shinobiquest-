from systems.save_system import save_game, load_game, temp
from systems.inventory import add_item, inventory
from systems.shop import shop
from systems.battle import battle


print(
    "====SHINOBI QUEST===="
    "\n1. New Game"
    "\n2. Load Game"
    "\n3. Exit"
)

while True:

    choice = input("Choose: ")

    if choice == "showstats":
        temp()

    if choice == "1":
        name = input("Enter Your Name: ")
        print(
            "\nChoose Village"
            "\n1. Leaf"
            "\n2. Sand"
            "\n3. Mist\n"
        )
        
        while True:
            choice_village = input("Choose: ")

            if choice_village == "1":
                village = "Leaf"
                break
                
            elif choice_village == "2":
                village = "Sand"
                break

            elif choice_village == "3":
                village = "Mist"
                break
                
            else:
                print("Invalid Village input!")

        print("Village selected:", village)
        player = {
            "name": name,
            "village": village,
            "level": 1,
            "hp": 100,
            "max_hp": 100,
            "chakra": 50,
            "xp": 0,
            "ryo": 0,
            "enemy_defeated": 0,
            "boss_defeated": 0,
            "inventory": {}
        }
        print(
            "\nWelcome to Shinobiquest! "
            "Heres your startup rewards "
            "for your exciting journey!"
        )
        add_item(player, "potion", 3)
        add_item(player, "kunai", 2)
        save_game(player)
        break

    elif choice == "2":
        player = load_game()

        print(f"\nWelcome Back {player['name']}")
        print(f"Current Village: {player['village']}")
        print(f"Level: {player['level']}")
        print(f"HP: {player['hp']}")
        print(f"Chakra: {player['chakra']}")
        print(f"XP: {player['xp']}")
        print(f"Ryo: {player['ryo']}")
        print(
            f"Enemy Defeated: "
            f"{player['enemy_defeated']}"
        )
        print(
            f"Boss Defeated: "
            f"{player['boss_defeated']}"
        )
        break

    elif choice == "3":
        print("Thanks for playing Shinobi Quest!")
        exit()

print(
    "\nYou are Good to go, "
    "Start/Continue the Journey?"
    "\n1. Yes"
    "\n2. No"
)

while True:
    choice_journey = input("Choose: ")

    if choice_journey == "2":
        break

    elif choice_journey == "1":
        while True:
            print(
                "\n1. Search"
                "\n2. Inventory"
                "\n3. Shop"
                "\n4. Exit"
            )

            choice_search = input("Choose: ")

            if choice_search == "showstats":
                temp()

            if choice_search == "1":
                if player["hp"] <= 0:
                    print(
                        "You can't fight anymore "
                        "Your hp is 0!\n"
                        "Please recover health "
                        "to continue fight."
                    )
                    continue
                battle(player)

            elif choice_search == "2":
                inventory(player)

            elif choice_search == "3":
                shop(player)
                
            elif choice_search == "4":
                break

    break