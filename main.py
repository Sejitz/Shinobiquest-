import json # Import JSON module for saving game data
import random

opponent = [
    {
        "name": "Bandit",
        "hp": 50,
        "damage": random.randint(5, 7),
        "xp": random.randint(70, 111),
        "ryo": random.randint(30, 52)
    },
    {
        "name": "Rogue Ninja",
        "hp": 80,
        "damage": random.randint(8, 15),
        "xp": random.randint(120, 180),
        "ryo": random.randint(60, 150)
    },
    {
        "name": "Wolf",
        "hp": 35,
        "damage": random.randint(3, 6),
        "xp": random.randint(40, 60),
        "ryo": random.randint(15, 26)
    }
]

print("====SHINOBI QUEST====\n1. New Game\n2. Load Game\n3. Exit") # Display the main menu

# ===== CHARACTER CREATION =====
def save_game():# ===== SAVE GAME FUNCTION =====
    with open("save.json","w") as file:
        json.dump(player, file)

# ===== INVENTORY ITEM ADDER =====
def add_item(item, amount=1):
    if item in player["inventory"]:
        player["inventory"][item] += amount
    else:
        player["inventory"][item] = amount
    print(f"{amount}x {item} added to your Inventory.")
    save_game()

def deal_dmg(target_hp, dmg):
    return max(0, target_hp - dmg)

def battle_reward():
    xp_gain = random.randint(70, 111)
    player["xp"] += xp_gain
    ryo_gain = random.randint(30, 52)
    player["ryo"] += ryo_gain
    player["enemy_defeated"] += 1
    potion_gain = random.randint(1, 2)
    if random.randint(1, 100) <= 30:
        print("\nYou found a Healing potion!")
        add_item("potion", potion_gain)
        
    while player["xp"] >= 500:
        player["level"] += 1
        player["xp"] -= 500  #stores the remaining xp after levelling up
        print("\n--==Level Up==--")
        print(f"You reached Level {player['level']} !!")
        
    print(f"You gained {xp_gain} XP!!")
    print(f"You earned {ryo_gain} Ryo!")
    save_game()
    
def battle():

    enemy = random.choice(opponent)
    enemy_name = enemy["name"]
    enemy_hp = enemy["hp"]
    enemy_dmg = enemy["damage"]
    enemy_xp = enemy["xp"]
    enemy_ryo = enemy["ryo"]
    def result():
        if player["hp"] <= 0:
            print("You were defeated!")
            save_game()          
        elif enemy_hp <= 0:
            print(f"\nYou defeated the {enemy_name}!!")
            player["enemy_defeated"] += 1
            battle_reward()
    print(f"\nA {enemy['name']} Appeared!\nYour Hp: {player['hp']}\n{enemy_name} Hp: {enemy_hp}")
        
    while player["hp"] >0 and enemy_hp >0: # Battle loop continueswhile both fighters are alive
        print("\n1. Attack\n2. Kunai\n3. Run")
        choice_attack = input("Choose: ")
        if choice_attack == '1':
            if random.randint(1, 100) <= 40:
                enemy_hp = deal_dmg(enemy_hp, 25)
                player["hp"] = deal_dmg(player["hp"], enemy_dmg)
                print("\nCritical Hit!!")
                print(f"\nYou dealt 25 damage!")
                print(f"{enemy_name} dealt {enemy_dmg} damage!\n")
                print(f"Your Hp: {player['hp']}\n{enemy_name} Hp: {enemy_hp}")
                result()
                continue
                
            enemy_hp = deal_dmg(enemy_hp, 10)
            player["hp"] = deal_dmg(player["hp"], enemy_dmg)
            print(f"\nYou dealt 10 damage!")
            print(f"{enemy_name} dealt {enemy_dmg} damage!\n")
            print(f"Your Hp: {player['hp']}\n{enemy_name} Hp: {enemy_hp}")
            result()
        elif choice_attack == "2":
            if player["inventory"]["kunai"] > 0:
                player["inventory"]["kunai"] -= 1
                enemy_hp = deal_dmg(enemy_hp, 20)
                print("\nYou dealt 20 damage!")
                print(f"{enemy_name} dealt {enemy_dmg} damage!\n")
                print(f"Your Hp: {player['hp']}\n{enemy_name} Hp: {enemy_hp}")
            else:
                print("You do not have any kunai!")
                print(f"Your Hp: {player['hp']}\nBandit Hp: {enemy_hp}")
            result()
        elif choice_attack == '3':
            print("You escaped the battle!")
            save_game()
            break

def inventory():
    
    print("\n--===Inventory===--")
    if player["inventory"] == {}:
        print("Your Inventory Is Empty")
    else:
        for item in player["inventory"]: # ===== DISPLAY INVENTORY ITEMS =====
            print(f"{item}: x{player['inventory'][item]}")
    while True:
        print("\nUse item's 1st letter to choose.\nEg. [p] for 'Potion'")
        print("1. Exit Inventory\n")
        choice_inventory = input("Choose i: ").lower()
        if choice_inventory == "p":
            if player["inventory"]["potion"] <= 0:# Prevent potion use when inventory is empty
                print("You do not have any potion!")
                continue
            if player["hp"] >= player["max_hp"]:# Prevent potion use at full HP
                print("Your Hp is full!")
                continue
            player["hp"] += 60
            player["inventory"]["potion"] -= 1
            print("60 Hp has been healed!")
            print(f"Potion left {player['inventory']['potion']}")
            if player["hp"] > player["max_hp"]:
                player["hp"] = player["max_hp"]
            print(f"Current HP: {player['hp']}")
            save_game()
        elif choice_inventory == "1":
            break

def shop():

    while True: #Logic for shop
        print("\n--===Shop===--")
        print(f"Your Ryo: {player['ryo']}")
        print("1. Potion: 70")
        print("2. Kunai: 40")
        print("3. Exit Shop")
        choice_shop = input("Choose: ")
        if choice_shop == "1":
            if player["ryo"] >= 70:
                player["ryo"] -= 70
                add_item("potion", 1)
                print(f"Ryo left: {player['ryo']}")                       
            else:
                print("You do not have enough Ryo.")
        elif choice_shop == "2":
            if player["ryo"] >= 40:
                player["ryo"] -= 40
                add_item("kunai", 1)
                print(f"Ryo left: {player['ryo']}")                           
            else:
                print("You do not have enough Ryo.")
        elif choice_shop == "3":
            break
    
while True:
    choice = input("Choose: ") # Get the player's menu choice
    if choice == '1': # Start a new game
        name = input("Enter Your Name: ")
        print("\nChoose Village\n1. Leaf\n2. Sand\n3. Mist\n")
        while True:
            choice_village = input("Choose: ")
            
            if choice_village == '1': # Assign the selected village
                village = "Leaf"
                break
            elif choice_village == '2':
                village = "Sand"
                break
            elif choice_village == '3':
                village = "Mist"
                break 
            else:
                print("Invalid Village input!")
        print("Village selected:", village)
        
        # ===== SAVE SYSTEM =====
        # Create a dictionary containing player data
        player = {
            "name": name,
            "village": village,
            "level": 1,
            "hp": 100,
            "max_hp": 100,
            "chakra": 50,
            "xp" : 0,
            "ryo": 0,
            "enemy_defeated": 0,
            "boss_defeated": 0,
            "inventory": {}
        }        
        print("\nWelcome to Shinobiquest! Heres your startup rewards for your exciting journey!")
        add_item("potion", 3)
        add_item("kunai", 2)
        
        save_game()  # Save player data to a JSON file                   
        break
        
    elif choice == '2':
        with open("save.json","r") as file:
            player = json.load(file)
            print(f"\nWelcome Back {player['name']}")
            print(f"Current Village: {player['village']}")
            print(f"Level: {player['level']}")
            print(f"HP: {player['hp']}")
            print(f"Chakra: {player['chakra']}")
            print(f"XP: {player['xp']}")
            print(f"Ryo: {player['ryo']}")
            print(f"Bandit Defeated: {player['bandit_defeated']}")
            print(f"Boss Defeated: {player['boss_defeated']}")
            break
    elif choice == '3':
        print("Thanks for playing Shinobi Quest!")
        exit()
        

    

    
# ===== BATTLE SYSTEM =====
print("\nYou are Good to go, Start/Continue the Journey?\n1. Yes\n2. No")
while True:     # Main game exploration loop
    choice_journey = input("Choose: ")
    if choice_journey == "2":
        break
    elif choice_journey == "1":
        while True:     # Exploration menu
            print("\n1. Search\n2. Inventory\n3. Shop\n4. Exit")
            choice_search = input("Choose: ")
            
            if choice_search == "1":    # Start a random encounter
                if player["hp"] <= 0:
                    print("You can't fight anymore Your hp is 0!\nPlease recover health to continue fight.")
                    continue
                battle()

            elif choice_search == "2":
                inventory()
            
            elif choice_search == "3":
                shop()

            elif choice_search == "4":
                break
    break #while searching if player exit search ,this 'break' end the whole game

