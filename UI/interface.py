import sys
import tty
import termios
import os

from rich.console import Console, Group
from rich.panel import Panel
from rich.layout import Layout
from rich.align import Align
from rich.progress import Progress, BarColumn, TextColumn
from rich.live import Live

from UI.menu import menu, draw_menu
from UI.name import get_player_name
from systems.save_system import save_game, load_game, temp
# from main import potion_amount, kunai_amount
from data.variables import screen, balance, player
from systems.inventory import add_item
from systems.battle import battle_log, MAX_BATTLE_LOG_ENTRIES
console = Console()



def main_ui(live):
    options = [
        "New Game",
        "Load Game",
        "Exit"
    ]

    # Main menu layout
    
    live.update(draw_menu(options, 0), refresh=True)

    return menu(options, live)

#Village Ui ---------------------------------------------------
def village_ui(live):
    options = [
        "Leaf",
        "Rain",
        "Sand"
    ]

    live.update(draw_menu(options, 0), refresh=True)

    return menu(options, live)

#Choice Ui ---------------------------------------------------
def choice_ui(live):
    options = [
        "Yes",
        "No"
    ]

    layout = Layout()

    layout.split_column(
        Layout(name="story", ratio=3),
        Layout(name="choice", ratio=2)
    )

    layout["story"].update(
        Panel(Group(
            "Welcome to Shinobiquest! \n Here's your startup rewards for your exciting journey!\n",
            f"3x added to your Inventory",
            f"2x added to your Inventory"    
            )
        )
    )

    layout["choice"].update(
        draw_menu(options, 0)
    )

    live.update(layout, refresh=True)

    return menu(
        options,
        live,
        target=layout["choice"]
    )

#Interface Ui ---------------------------------------------------
def interface_ui(live):
    options = [
        "Search",
        "Inventory",
        "Shop",
        "Back"
    ]

    # Interface menu layout
    live.update(draw_menu(options, 0), refresh=True)

    return menu(options, live)

#Inventory Ui ---------------------------------------------------
def inventory_ui(live, potion, kunai):
    # potion_amount = f"Potion: {potion}"
    # kunai_amount = f"Kunai: {kunai}"
    
    options = [
        f"Potion: {player['inventory']['potion']}",
        f"Kunai: {player['inventory']['kunai']}",
        "Back"
    ]

    layout = Layout()
    layout.split_column(
        Layout(name="header", size=1),
        Layout(name="items")
    )

    layout["header"].update(
        Align.center("[italic green]← Inventory →[/italic green]")
    )
    layout["items"].update(draw_menu(options, 0))

    live.update(layout, refresh=True)

    return menu(options, live, target=layout["items"])

    
#Shop Ui ---------------------------------------------------
def shop_ui(live, balance):
    potion_price = 70
    kunai_price = 40

    options = [
        f"Potion: {potion_price}",
        f"Kunai: {kunai_price}\n",
        "Back"
    ]

    layout = Layout()
    layout.split_column(
        Layout(name="info", size=3),
        Layout(name="shop")
    )

    layout["info"].update(
        Panel(f"Balance: {balance}", title="[italic green]← Shop →[/italic green]")
    )
    layout["shop"].update(draw_menu(options, 0))

    live.update(layout, refresh=True)

    return menu(options, live, target=layout["shop"])


    
#Battle Ui ---------------------------------------------------
def battle_ui(live, player, enemy_name, enemy_hp, enemy_max, battle_log):

    options = [
        "Attack",
        "Kunai",
        "Run"
    ]

    # HP / CHAKRA BARS

    player_hpbar = Progress(
        TextColumn("[bold]HP [/bold]"),
        BarColumn(),
        TextColumn("{task.percentage:>3.0f}%")
    )

    player_chbar = Progress(
        TextColumn("[bold]Chakra [/bold]"),
        BarColumn(),
        TextColumn("{task.percentage:>3.0f}%")
    )

    enemy_bar = Progress(
        TextColumn("[bold]HP [/bold]"),
        BarColumn(),
        TextColumn("{task.percentage:>3.0f}%")
    )

    player_hpbar.add_task(
        "HP",
        total=player.get("max_hp", 100),
        completed=player["hp"]
    )
    
    player_chbar.add_task(
        "Chakra",
        total=100,
        completed=player["chakra"]
    )
    
    enemy_bar.add_task(
        "HP",
        total=enemy_max,
        completed=enemy_hp
    )

    # -----------------------------------------------------
    # MAIN BATTLE LAYOUT
    # -----------------------------------------------------

    layout = Layout()

    def update_log():
        layout["log"].update(
            Panel(
                "\n".join(battle_log[-MAX_BATTLE_LOG_ENTRIES:]) or "Battle begins...",
                title="Battle Log"
            )
        )
        live.refresh()

    layout.split_column(
        Layout(name="info", ratio=3),
        Layout(name="log", ratio=2),
        Layout(name="battleui", ratio=2)
    )

    # -----------------------------------------------------
    # PLAYER / ENEMY
    # -----------------------------------------------------

    layout["info"].split_row(
        Layout(name="player"),
        Layout(name="enemy")
    )

    player_panel = Group(
        player_hpbar,
        player_chbar,
        "",
        f"Ryo: {player['ryo']}"
    )
    
    enemy_panel = Group(
        f"Name: {enemy_name}",
        enemy_bar
    )
    

    layout["player"].update(
        Panel(
            player_panel,
            title="Player"
        )
    )

    layout["enemy"].update(
        Panel(
            enemy_panel,
            title="Enemy"
        )
    )

    # -----------------------------------------------------
    # BATTLE LOG
    # -----------------------------------------------------

    layout["log"].update(
        Panel(
            "\n".join(battle_log[-MAX_BATTLE_LOG_ENTRIES:]) or "Battle begins...",
            title="Battle Log"
        )
    )

    # -----------------------------------------------------
    # BATTLE MENU
    # -----------------------------------------------------

    layout["battleui"].update(
        draw_menu(options, 0),
    )

    # -----------------------------------------------------
    # UPDATE LIVE SCREEN
    # -----------------------------------------------------

    live.update(
        layout,
        refresh=True
    )

    # -----------------------------------------------------
    # GET PLAYER CHOICE
    # -----------------------------------------------------

    action = menu(
        options,
        live,
        target=layout["battleui"]
    )
    return action, update_log


