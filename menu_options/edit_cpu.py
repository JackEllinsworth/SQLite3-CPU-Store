from handlers import menu

CPU_OPTIONS = ["Name", "Clock Speed", "Cores", "Cache Size", "Price"]
CPU_REAL_ONLY = ["Clock Speed", "Cores", "Cache Size", "Price"]
DEFINED_OPTIONS = ["name", "clock_speed", "cores", "cache_size", "price"]


def send_menu(conn):
    response = menu.create_menu_reply("EDIT CPU MENU", "Please reply with the CPU name you want to edit", "string")

    choice = menu.create_menu_option("OPTION TO CHANGE", CPU_OPTIONS)

    str_type = "string"

    if CPU_OPTIONS[int(choice-1)] in CPU_REAL_ONLY:
        str_type = "real"

    new_value = menu.create_menu_reply("UPDATED VALUE", "Please reply with the new value for " + CPU_OPTIONS[int(choice-1)], str_type)

    cursor = conn.execute("""UPDATE TYPES SET """ + DEFINED_OPTIONS[int(choice-1)] + """ = ? WHERE NAME = ?""", (new_value, response))

    if cursor.rowcount < 1:
        print("Error finding CPU's matching the name specified.")
    else:
        conn.commit()
        print("Updated any CPU's matching that name with the new value.")


    return
