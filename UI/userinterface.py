import sys
import tty
import termios
from rich.console import Console, Group
from rich.panel import Panel
from rich.layout import Layout
from rich.align import Align
from rich.progress import Progress , BarColumn, TextColumn
from rich.live import Live

from menu import menu, draw_menu



options = [
    "Attack",
    "Defend",
    "Items",
    "Run"
]

#rich
#___________________

console = Console()
layout = Layout()

def ui():

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
    
    player_hpbar.add_task("HP ", total=100, completed=100)
    player_chbar.add_task("Chakra ", total=100, completed=100)
    enemy_bar.add_task("HP ", total=100, completed=100)
    
    
    layout.split_column(
        Layout(name="info", ratio=3),
        Layout(name="log", ratio=2),
        Layout(name="menue", ratio=4)
    )
    
    layout["info"].split_row(
        Layout(name="player"),
        Layout(name="enemy")
    )
    
    player_panel = Group(
        player_hpbar,
        player_chbar,
        "",
        "Ryo: 100 HP"
    )
    
    enemy_panel = Group(
        "Name: Bandit",
        enemy_bar
    )
    
    layout["player"].update(
        Panel(player_panel, title="Player")
    )
    
    layout["enemy"].update(
        Panel(enemy_panel, title="Enemy")
    )
    
    layout["log"].update(
        Panel("Choose your action...")
    )
    
    position = 0
    layout["menue"].update(
        draw_menu(options, position)
    )
    
    #game
    #________________
    
    
    
    old_settings = termios.tcgetattr(sys.stdin)
    
    try:
        tty.setcbreak(sys.stdin.fileno())
    
        console.print(
            Align.center("[bold cyan]→ Shinobi Quest ←[/bold cyan]")
        )
    
        with Live(layout, console=console):
            choice = menu(options, layout)
    
        # Test what the menu returned
        console.print(f"\nYou selected: [bold yellow]{choice}[/bold yellow]")
    
    finally:
        termios.tcsetattr(
            sys.stdin,
            termios.TCSADRAIN,
            old_settings
        )
        