import json # Import JSON module for saving game data
import random

print("====SHINOBI QUEST====\n1. New Game\n2. Load Game\n3. Exit") # Display the main menu

# ===== CHARACTER CREATION =====
def save_game():# ===== SAVE GAME FUNCTION =====
    with open("save.json","w") as file:
        json.dump(player, file)
def add_item(item, amount=1):
    if item in player["inventory"]:
        player["inventory"][item] += amount
    else:
        player["inventory"][item] = amount
    print(f"{amount}x {item} added to your Inventory.")

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
            "bandit_defeated": 0,
            "boss_defeated": 0,
            "inventory": {}
        }        
        print("\nWelcome to Shinobiquest! Heres your startup rewards for your exciting journey!")
        add_item("potion", 5)
        
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
        
        
    

    
# ===== BATTLE SYSTEM =====
print("\nYou are Good to go, Start/Continue the Journey?\n1. Yes\n2. No")
while True:     # Main game exploration loop
    choice_journey = input("Choose: ")
    if choice_journey == "2":
        break
    elif choice_journey == "1":
        while True:     # Exploration menu
            print("\n1. Search\n2. Inventory\n3. Exit")
            choice_search = input("Choose: ")
            
            if choice_search == "1":    # Start a random encounter
                if player["hp"] <= 0:
                    print("You can't fight anymore Your hp is 0!\nPlease recover health to continue fight.")
                    continue
                bandit_hp = 50
                print(f"\nA Bandit Appeared!\nYour Hp: {player['hp']}\nBandit Hp: {bandit_hp}")
                    
                while player["hp"] >0 and bandit_hp >0: # Battle loop continueswhile both fighters are alive
                    print("\n1. Attack\n2. Run")
                    choice_attack = input("Choose: ")
                    if choice_attack == '1':
                        bandit_hp = bandit_hp - 10
                        player["hp"] -= 5
                        print("\nYou dealt 10 damage!")
                        print("Bandit dealt 5 damage!\n")
                        print(f"Your Hp: {player['hp']}\nBandit Hp: {bandit_hp}")
                        
                        if player["hp"] <= 0:
                            print("You were defeated!")
                            save_game()
                            break

                        elif bandit_hp <= 0:
                            print("\nYou defeated the Bandit!!")
                            # ===== EXPERIENCE REWARD SYSTEM =====
                            # Grant XP, Ryo reward for a successful battle
                            xp_gain = random.randint(70, 111)
                            player["xp"] += xp_gain
                            ryo_gain = random.randint(30, 52)
                            player["ryo"] += ryo_gain
                            player["bandit_defeated"] += 1
                            potion_gain = random.randint(1, 2)
                            
                            # Display progression update
                            print(f"You gained {xp_gain} XP!!")
                            print(f"You earned {ryo_gain} Ryo!")
                            if random.randint(1, 100) <= 30:
                                print("You found a Healing potion!")
                                add_item("potion", potion_gain)
                                
                            while player["xp"] >= 500:
                                player["level"] += 1
                                player["xp"] -= 500  #stores the remaining xp after levelling up
                                print("\n--==Level Up==--")
                                print(f"You reached Level {player['level']} !!")
                                
                            save_game()
                            break
                        # Update saved HP Level and xp after battle progress
                            
                    elif choice_attack == '2':
                        print("You escaped the battle!")
                        save_game()
                        break
                    
            elif choice_search == "2":
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
                        if player["hp"] > 100:
                            player["hp"] = player["max_hp"]
                        print(f"Current HP: {player['hp']}")
                    elif choice_inventory == "1":
                        break
                        
                    
            elif choice_search == "3":
                break
    break #while searching if player exit search ,this 'break' end the whole game

