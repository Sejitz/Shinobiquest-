import random

from data.enemies import opponent
from utils.helpers import deal_dmg
from systems.save_system import save_game
from systems.inventory import add_item
from systems.save_system import temp

MAX_BATTLE_LOG_ENTRIES = 6
battle_log = []

def _append_battle_log(message):
    battle_log.append(message.strip())
    del battle_log[:-MAX_BATTLE_LOG_ENTRIES]

def battle(player, action_ui, log_ui):
    battle_log.clear()

    def append_battle_log(message):
        _append_battle_log(message)
        log_ui()
    enemy = random.choice(opponent)

    enemy_name = enemy["name"]
    enemy_hp = enemy["hp"]
    enemy_max = enemy["max"]

    enemy_xp = random.randint(
        enemy["xp"][0],
        enemy["xp"][1]
    )
    enemy_ryo = random.randint(
        enemy["ryo"][0],
        enemy["ryo"][1]
    )
    def heal():
        nonlocal enemy_hp

        if enemy_hp < (enemy_max * 40 / 100):
            h_min, h_max = enemy["heal"]
            heal_amt = random.randint(h_min, h_max)
            enemy_hp = min(
                enemy_hp + heal_amt,
                enemy_max
            )
            append_battle_log(f"{enemy_name} healed {heal_amt} HP")
            

    def battle_reward():

        xp_gain = enemy_xp
        player["xp"] += xp_gain

        ryo_gain = enemy_ryo
        player["ryo"] += ryo_gain

        potion_gain = random.randint(1, 2)

        if random.randint(1, 100) <= 7:
            append_battle_log("\nYou found a Healing potion!")
            add_item(
                player,
                "potion",
                potion_gain
            )

        while player["xp"] >= 500:
            player["level"] += 1
            player["xp"] -= 500
            append_battle_log("\n--==Level Up==--")
            append_battle_log(
                f"You reached Level "
                f"{player['level']} !!"
            )
        append_battle_log(f"You gained {xp_gain} XP!!")
        append_battle_log(f"You earned {ryo_gain} Ryo!")
        save_game(player)

    def result():
        if player["hp"] <= 0:
            append_battle_log("You were defeated!")
            save_game(player)
            
        elif enemy_hp <= 0:
            append_battle_log(
                f"\nYou defeated the "
                f"{enemy_name}!!"
            )
            player["enemy_defeated"] += 1
            battle_reward()
    append_battle_log(
        f"\nA {enemy['name']} Appeared!"
        # f"\nYour Hp: {player['hp']}"
        # f"\n{enemy_name} Hp: {enemy_hp}"
    )

    while player["hp"] > 0 and enemy_hp > 0:
        choice_attack = action_ui(
            player,
            enemy_name,
            enemy_hp,
            enemy_max,
            battle_log
        )

        if choice_attack == "Attack":
            # Enemy AI
            ai_react = random.randint(1, 100)
            if ai_react <= 25:
                append_battle_log(
                    f"{enemy_name} Raises His guard."
                )
                enemy_hp = deal_dmg(
                    enemy_hp,
                    5
                )
                enemy_dmg = random.randint(
                    enemy["damage"][0],
                    enemy["damage"][1]
                )
                player["hp"] = deal_dmg(
                    player["hp"],
                    enemy_dmg
                )
                append_battle_log("\nYou dealt 5 damage!")
                #battle_log.append(
                #    f"Your Hp: {player['hp']}"
                #    f"\n{enemy_name} Hp: {enemy_hp}"
                #)
                result()
                continue

            if ai_react <= 50:
                heal_chance = random.randint(1, 100)
                if heal_chance <= 50:
                    if enemy_name == "Bandit":
                        heal()
                    elif enemy_name == "Rogue Ninja":
                        heal()

            if random.randint(1, 100) <= 5:
                enemy_hp = deal_dmg(
                    enemy_hp,
                    25
                )
                enemy_dmg = random.randint(
                    enemy["damage"][0],
                    enemy["damage"][1]
                )
                player["hp"] = deal_dmg(
                    player["hp"],
                    enemy_dmg
                )
                append_battle_log("\nCritical Hit!!")
                append_battle_log("\nYou dealt 25 damage!")
                # battle_log.append(
                #     f"Your Hp: {player['hp']}"
                #     f"\n{enemy_name} Hp: {enemy_hp}"
                # )
                result()
                continue

            enemy_hp = deal_dmg(
                enemy_hp,
                10
            )
            enemy_dmg = random.randint(
                enemy["damage"][0],
                enemy["damage"][1]
            )
            player["hp"] = deal_dmg(
                player["hp"],
                enemy_dmg
            )
            append_battle_log("\nYou dealt 10 damage!")
            append_battle_log(
                f"{enemy_name} dealt "
                f"{enemy_dmg} damage!\n"
            )
            # battle_log.append(
            #     f"Your Hp: {player['hp']}"
            #     f"\n{enemy_name} Hp: {enemy_hp}"
            # )
            result()

        elif choice_attack == "Kunai":
            kunai_count = player["inventory"].get("kunai", 0)
            if kunai_count > 0:
                player["inventory"]["kunai"] -= 1
                enemy_hp = deal_dmg(enemy_hp, 20
                )
                
                append_battle_log("\nYou dealt 20 damage!")
                # battle_log.append(
                #     f" Hp: {player['hp']}"
                #     f"\n{enemy_name} Hp: {enemy_hp}"
                # )

                save_game(player)
            else:
                append_battle_log("You do not have any kunai!")
                # battle_log.append(
                #     f"Your Hp: {player['hp']}"
                #     f"\n{enemy_name} Hp: {enemy_hp}"
                # )
            result()

        elif choice_attack == "Run":
            append_battle_log("You escaped the battle!")
            save_game(player)
            break
