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
from systems.inventory import add_item, heal
from systems.shop import shop
from systems.battle import battle

from UI.interface import battle_ui, choice_ui, draw_menu, get_player_name, interface_ui, inventory_ui, main_ui, shop_ui, village_ui  
from data.variables import screen, balance, player

console = Console()


def create_battle_callbacks(live):
    log_refresh = [lambda: None]

    def action_ui(player, enemy_name, enemy_hp, enemy_max, battle_log):
        action, update_log = battle_ui(
            live, player, enemy_name, enemy_hp, enemy_max, battle_log
        )
        log_refresh[0] = update_log
        return action

    def log_ui():
        log_refresh[0]()

    return action_ui, log_ui


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
                    #################
                    player["name"] = name
                    player["village"] = village
                
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
                        action_ui, log_ui = create_battle_callbacks(live)
                        battle(player, action_ui, log_ui)
            
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
                choice = inventory_ui(live, player['inventory']['potion'], player['inventory']['kunai'])
                # console.print(repr(choice))
                
                if choice == "Back":
                    screen = "interface"
                elif choice == f"Potion: {player['inventory']['potion']}":
                    # print("healed")
                    heal(player)

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
        