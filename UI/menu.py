import sys
from rich.panel import Panel

def menu(option, layout):
        position = 0
            
    #choice = menu()
        
        while True:
            #print("\x1b[2J\x1b[H")
            
                
            key = sys.stdin.read(1)
            
            if key == 'q':
                break
            if key == '\x1b':
                key += sys.stdin.read(2)
                if key == '\x1b[A':
                    position = max(0, position - 1)

                elif key == '\x1b[B':
                    position = min(len(option) - 1, position + 1)
                layout["menue"].update(
                    draw_menu(option, position)
                )
            if key == '\n':
                return option[position]

def draw_menu(options, position):
    menu_text = ""

    for i, item in enumerate(options):
        if i == position:
            menu_text += "> " + item + "\n"
        else:
            menu_text += "  " + item + "\n"

    return Panel(menu_text, title="Actions")
