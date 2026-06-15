import json # Import JSON module for saving game data

print("====SHINOBI QUEST====\n1. New Game\n2. Load Game\n3. Exit") # Display the main menu

while True:
    choice = input("Choose: ") # Get the player's menu choice
    if choice == '1': # Start a new game
        name = input("Enter Your Name: ")
        choice2 = input("\nChoose Village\n1. Leaf\n2. Sand\n3. Mist\nChoose: ")
        
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
        
        
# Create a dictionary containing player data
player = {
    "name": name,
    "village": village,
    "level": 1,
    "hp": 100,
    "chakra": 50
}

with open("save.json","w") as file: # Save player data to a JSON file
    json.dump(player, file)