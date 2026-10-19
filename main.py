import sys
import tty
import termios

from rich.console import Console, Group
from rich.panel import Panel
from rich.layout import Layout
from rich.align import Align
from rich.progress import Progress, BarColumn, TextColumn
from rich.live import Live

from UI.menu import menu, draw_menu
from UI.name import get_player_name

from systems.save_system import save_game, load_game, temp
from systems.inventory import add_item, inventory
from systems.shop import shop
from systems.battle import battle

from UI.interface import battle_ui, choice_ui, draw_menu, get_player_name, interface_ui, inventory_ui, main_ui, shop_ui, village_ui  
from data.variables import screen, potion_amount, kunai_amount, balance
console = Console()


old_settings = termios.tcgetattr(sys.stdin)

try:
    tty.setcbreak(sys.stdin.fileno())

    console.print(
        Align.center(
            "[bold cyan]→ Shinobi Quest ←[/bold cyan]"
        )
    )


    with Live(
        "",
        console=console,
        auto_refresh=False
    ) as live:


        screen = "main"
        potion_amount = 0
        kunai_amount = 0
        balance = 0

        while True:
            if screen == "main":
                choice = main_ui(live)
                if choice == "New Game":
                    screen = "village"
                elif choice == "Load Game":
                    try:
                        player = load_game()
                        screen = "interface"
                    except FileNotFoundError:
                        console.print("[red]No save file found![/red]")
                        screen = "main"
                elif choice == "Exit":
                    break
                    
            elif screen == "village":
                name = get_player_name(live)
                village = village_ui(live)
                screen = "choice"
                
            elif screen == "choice":
                choice = choice_ui(live)
                
                if choice == "No":
                    screen = "main"
                
                elif choice == "Yes":
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
                
                    add_item(player, "potion", 3)
                    add_item(player, "kunai", 2)
                
                    save_game(player)
                
                    screen = "interface"
                                    
            elif screen == "interface":
                choice = interface_ui(live)
            
                if choice == "Search":
                    if player["hp"] <= 0:
                        console.print("[red]Your HP is zero! Recover first.[/red]")
                    else:
                        battle(
                            player,
                            lambda p, name, hp, maximum:
                                battle_ui(live, p, name, hp, maximum)
                        )
            
                    screen = "interface"
            
                elif choice == "Inventory":
                    screen = "inventory"
            
                elif choice == "Shop":
                    screen = "shop"
            
                elif choice == "Back":
                    screen = "main"
                elif choice == "Inventory":
                    screen = "inventory"
                elif choice == "Shop":
                    screen = "shop"
                elif choice == "Back":
                    screen = "main"
                    
            # elif screen == "battle":
            #     choice = battle_ui(live)
                
            elif screen == "inventory":
                choice = inventory_ui(live, potion_amount, kunai_amount)
                if choice == "Back":
                    screen = "interface"

            elif screen == "shop":
                choice = shop_ui(live, balance)
                if choice == "Back":
                    screen = "interface"
finally:

        termios.tcsetattr(
            sys.stdin,
            termios.TCSADRAIN,
            old_settings
        )
        
                


#=========================================================

# print(
#     "====SHINOBI QUEST===="
#     "\n1. New Game"
#     "\n2. Load Game"
#     "\n3. Exit"
# )

# while True:

#     choice = input("Choose: ")

#     if choice == "showstats":
#         temp()

#     # if choice == "1":
#     #     name = input("Enter Your Name: ")
#     #     print(
#     #         "\nChoose Village"
#     #         "\n1. Leaf"
#     #         "\n2. Sand"
#     #         "\n3. Mist\n"
#     #     )
        
#         # while True:
#         #     choice_village = input("Choose: ")

#         #     if choice_village == "1":
#         #         village = "Leaf"
#         #         break
                
#         #     elif choice_village == "2":
#         #         village = "Sand"
#         #         break

#         #     elif choice_village == "3":
#         #         village = "Mist"
#         #         break
                
#         #     else:
#         #         print("Invalid Village input!")

#         print("Village selected:", village)
#         player = {
#             "name": name,
#             "village": village,
#             "level": 1,
#             "hp": 100,
#             "max_hp": 100,
#             "chakra": 50,
#             "xp": 0,
#             "ryo": 0,
#             "enemy_defeated": 0,
#             "boss_defeated": 0,
#             "inventory": {}
#         }
#         print(
#             "\nWelcome to Shinobiquest! "
#             "Heres your startup rewards "
#             "for your exciting journey!"
#         )
#         add_item(player, "potion", 3)
#         add_item(player, "kunai", 2)
#         save_game(player)
#         break

#     elif choice == "2":
#         player = load_game()

#         print(f"\nWelcome Back {player['name']}")
#         print(f"Current Village: {player['village']}")
#         print(f"Level: {player['level']}")
#         print(f"HP: {player['hp']}")
#         print(f"Chakra: {player['chakra']}")
#         print(f"XP: {player['xp']}")
#         print(f"Ryo: {player['ryo']}")
#         print(
#             f"Enemy Defeated: "
#             f"{player['enemy_defeated']}"
#         )
#         print(
#             f"Boss Defeated: "
#             f"{player['boss_defeated']}"
#         )
#         break

#     elif choice == "3":
#         print("Thanks for playing Shinobi Quest!")
#         exit()

# print(
#     "\nYou are Good to go, "
#     "Start/Continue the Journey?"
#     "\n1. Yes"
#     "\n2. No"
# )

# while True:
#     choice_journey = input("Choose: ")

#     if choice_journey == "2":
#         break

#     elif choice_journey == "1":
#         while True:
#             print(
#                 "\n1. Search"
#                 "\n2. Inventory"
#                 "\n3. Shop"
#                 "\n4. Exit"
#             )

#             choice_search = input("Choose: ")

#             if choice_search == "showstats":
#                 temp()

#             if choice_search == "1":
#                 if player["hp"] <= 0:
#                     print(
#                         "You can't fight anymore "
#                         "Your hp is 0!\n"
#                         "Please recover health "
#                         "to continue fight."
#                     )
#                     continue
#                 battle(player)

#             elif choice_search == "2":
#                 inventory(player)

#             elif choice_search == "3":
#                 shop(player)
                
#             elif choice_search == "4":
#                 break

#     break