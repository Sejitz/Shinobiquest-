from systems.inventory import add_item


def shop_potion(player):
    # print(f"Your Ryo: {player['ryo']}")

    if player["ryo"] >= 70:
        player["ryo"] -= 70
        add_item(player, "potion", 1)
        # print(f"Ryo left: {player['ryo']}")
    else:
        print("You do not have enough Ryo.")

def shop_kunai(player):

    if player["ryo"] >= 40:
        player["ryo"] -= 40
        add_item(player, "kunai", 1)
        print(f"Ryo left: {player['ryo']}")
    else:
        print("You do not have enough Ryo.")

    