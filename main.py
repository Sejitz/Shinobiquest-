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
from systems.battle import battle, battle_log

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
                        log_updater = [lambda: None]
                        
                        def action_ui(p, enemy_name, enemy_hp, enemy_max, current_log):
                            action, update_log = battle_ui(
                                live,
                                p,
                                enemy_name,
                                enemy_hp,
                                enemy_max,
                                current_log
                            )
                    
                            log_updater[0] = update_log
                            return action
                    
                        def log_ui():
                            log_updater[0]()
                    
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
                    
            elif screen == "battle":
                # choice = battle_ui(live)
                pass
                
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
        
           