from handlers import menu
from menu_options import add_cpu
from menu_options import edit_cpu
from menu_options import find_cpu
from menu_options import remove_cpu


MENU_OPTIONS = ["Add new CPU", "Edit previous CPU", "Find previous CPU", "Remove previous CPU", "Exit"]


def send_menu(conn):
    # Retrieves response
    response = menu.create_menu_option("MAIN MENU", MENU_OPTIONS, False)

    if response == 1:
        add_cpu.send_menu(conn)
    elif response == 2:
        edit_cpu.send_menu(conn)
    elif response == 3:
        find_cpu.send_menu(conn)
    elif response == 4:
        remove_cpu.send_menu(conn)
    elif response == 5:
        print("Closing...")
        exit()

    # Creates default menu once finished.
    send_menu(conn)

