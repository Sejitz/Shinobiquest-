import sys
from rich.panel import Panel


def menu(options, live, target=None):
    position = 0

    while True:
        key = sys.stdin.read(1)

        if key == 'q':
            break

        if key == '\x1b':
            key += sys.stdin.read(2)
            if key == '\x1b[A':
                position = max(0, position - 1)
            elif key == '\x1b[B':
                position = min(len(options) - 1, position + 1)

            updater = target if target is not None else live
            updater.update(draw_menu(options, position))
            live.refresh()

        if key in ('\n', '\r'):
            return options[position]


def draw_menu(options, position):
    menu_text = ""

    for i, item in enumerate(options):
        if i == position:
            menu_text += "> " + item + "\n"
        else:
            menu_text += "  " + item + "\n"

    return Panel(menu_text, title="Actions")