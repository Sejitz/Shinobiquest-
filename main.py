import json # Import JSON module for saving game data
import random

print("====SHINOBI QUEST====\n1. New Game\n2. Load Game\n3. Exit") # Display the main menu

# ===== CHARACTER CREATION =====
def save_game():
    with open("save.json","w") as file:
        json.dump(player, file)
    
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
            "chakra": 50,
            "xp" : 0
        }
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
            break
        
        
    

    
# ===== BATTLE SYSTEM =====
print("\nYou are Good to go, Start/Continue the Journey?\n1. Yes\n2. No")
while True:     # Main game exploration loop
    choice_journey = input("Choose: ")
    if choice_journey == "2":
        break
    elif choice_journey == "1":
        while True:     # Exploration menu
            print("\n1. Search\n2. Exit")
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
                            print("You defeated the Bandit!!")
                            # ===== EXPERIENCE REWARD SYSTEM =====
                            # Grant XP reward for a successful battle
                            xp_gain = random.randrange(70, 155)
                            player["xp"] += xp_gain
                            # Display progression update
                            print(f"You gained {xp_gain} XP!!")
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
                break
    break #while searching if player exit search ,this 'break' end the whole game

  