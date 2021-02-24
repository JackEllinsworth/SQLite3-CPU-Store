from handlers import menu

CPU_OPTIONS = ["Name", "Clock Speed", "Cores", "Cache Size", "Price"]
CPU_REAL_ONLY = ["Clock Speed", "Cores", "Cache Size", "Price"]
DEFINED_OPTIONS = ["name", "clock_speed", "cores", "cache_size", "price"]


def send_menu(conn):
    # Creates menu to collect CPU name
    response = menu.create_menu_reply("EDIT CPU MENU", "Please reply with the CPU name you want to edit", "string", True)
    if response == "menu": return

    # Asks for what option to change.
    choice = menu.create_menu_option("OPTION TO CHANGE", CPU_OPTIONS, True)
    if choice == "menu": return

    str_type = "string"

    # Checks to see if the input requires a real not string
    if CPU_OPTIONS[int(choice-1)] in CPU_REAL_ONLY:
        str_type = "real"

    # Asks for the value
    new_value = menu.create_menu_reply("UPDATED VALUE", "Please reply with the new value for " + CPU_OPTIONS[int(choice-1)], str_type, True)
    if new_value == "menu": return

    cursor = conn.execute("""UPDATE TYPES SET """ + DEFINED_OPTIONS[int(choice-1)] + """ = ? WHERE NAME = ?""", (new_value, response))
    conn.commit()

    # Outputs success or failure of execution.
    if cursor.rowcount < 1:
        print("Error finding CPU's matching the name specified.")
    else:
        conn.commit()
        print("Updated any CPU's matching that name with the new value.")


    return
