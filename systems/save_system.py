import json


def save_game(player):
    with open("save.json", "w") as file:
        json.dump(player, file)

def load_game():
    with open("save.json", "r") as file:
        return json.load(file)

def temp():
    player = load_game()

    print(f"\nName: {player['name']}")
    print(f"Level: {player['level']}")
    print(f"HP: {player['hp']}")
    print(f"Chakra: {player['chakra']}")
    print(f"XP: {player['xp']}")
    print(f"Ryo: {player['ryo']}")
    print(f"Enemy Defeated: {player['enemy_defeated']}")
    print(f"Boss Defeated: {player['boss_defeated']}")