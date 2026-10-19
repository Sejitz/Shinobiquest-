import termios, tty
from rich.live import Live
from rich.panel import Panel
import sys

def get_player_name(live):
    typed = ""
    fd = sys.stdin.fileno()

    # Show the panel immediately
    live.update(
        Panel("Enter your Name: "),
        refresh=True
    )

    while True:
        key = sys.stdin.read(1)

        if key == '\n':
            break

        elif key == '\x7f':
            typed = typed[:-1]

        else:
            typed += key

        live.update(
            Panel(f"Enter your Name: {typed}"),
            refresh=True
        )

    return typed