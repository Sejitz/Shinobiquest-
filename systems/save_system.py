import json
from pathlib import Path

SAVE_FILE = Path(__file__).resolve().parent.parent / "save.json"


def save_game(player):
    with open(SAVE_FILE, "w") as file:
        json.dump(player, file, indent=4)


def load_game():
    with open(SAVE_FILE, "r") as file:
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