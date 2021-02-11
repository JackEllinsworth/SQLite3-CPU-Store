from handlers import menu
from menu_options import add_cpu
from menu_options import edit_cpu
from menu_options import find_cpu
from menu_options import remove_cpu


MENU_OPTIONS = ["Add new CPU", "Edit previous CPU", "Find previous CPU", "Remove previous CPU"]


def send_menu(conn):
    response = menu.create_menu_option("MAIN MENU", MENU_OPTIONS)

    if response == 1:
        add_cpu.send_menu(conn)
    elif response == 2:
        edit_cpu.send_menu(conn)
    elif response == 3:
        find_cpu.send_menu(conn)
    elif response == 4:
        remove_cpu.send_menu(conn)

    send_menu(conn)

