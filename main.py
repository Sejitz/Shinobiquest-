import json # Import JSON module for saving game data

print("====SHINOBI QUEST====\n1. New Game\n2. Load Game\n3. Exit") # Display the main menu

# ===== CHARACTER CREATION =====
player_hp = 100
chakra = 50
while True:
    choice = input("Choose: ") # Get the player's menu choice
    if choice == '1': # Start a new game
        name = input("Enter Your Name: ")
        print("\nChoose Village\n1. Leaf\n2. Sand\n3. Mist\n")
        while True:
            choice2 = input("Choose: ")
            
            if choice2 == '1': # Assign the selected village
                village = "Leaf"
                break
            elif choice2 == '2':
                village = "Sand"
                break
            elif choice2 == '3':
                village = "Mist"
                break 
            else:
                print("Invalid Village input!")
        print("Village selected:", village)
        break
    
# ===== SAVE SYSTEM =====
# Create a dictionary containing player data
player = {
    "name": name,
    "village": village,
    "level": 1,
    "hp": player_hp,
    "chakra": chakra
}

with open("save.json","w") as file: # Save player data to a JSON file
    json.dump(player, file)
    
# ===== BATTLE SYSTEM =====
print("\nYou are Good to go, Start the Journey?\n1. Yes\n2. No")
while True:     # Main game exploration loop
    choice = input("Choose: ")
    if choice == "2":
        break
    elif choice == "1":
        while True:     # Exploration menu
            print("\n1. Search\n2. Exit")
            choice = input("Choose: ")
            
            if choice == "1":    # Start a random encounter
                bandit_hp = 50
                print(f"\nA Bandit Appeared!\nYour Hp: {player_hp}\nBandit Hp: {bandit_hp}")
                    
                while player_hp >0 and bandit_hp >0: # Battle loop continues
                while both fighters are alive
                    print("\n1. Attack\n2. Run")
                    choice = input("Choose: ")
                    if choice == '1':
                        bandit_hp = bandit_hp - 10
                        player_hp = player_hp - 5
                        print("You dealt 10 damage!")
                        print("Bandit dealt 5 damage!")
                        print(f"Your Hp: {player_hp}\nBandit Hp: {bandit_hp}")
                        
                        if player_hp <= 0:
                            print("You were defeated!")
                            break
                        if bandit_hp <= 0:
                            print("You defeated the Bandit!!")
                            break
                        # Update saved HP after battle progress
                        player["hp"] = player_hp
                        with open("save.json","w") as file:
                            json.dump(player, file)
                            
                    elif choice == '2':
                        print("You escaped the battle!")
                        break
            elif choice == "2":
                break
    break