from handlers import menu


MENU_OPTIONS = ["Send all", "Find one by name"]


def send_menu(conn):
    # Retrieves response for how they want to search for CPU's
    response = menu.create_menu_option("FIND CPU MENU", MENU_OPTIONS, True)

    if response == "menu": return

    if response == 1:
        # Returns all CPU's and prints out.
        cursor = conn.execute("SELECT id, name, clock_speed, cores, cache_size, price from TYPES")

        for row in cursor:
            print("---> ID: " + str(row[0]) + " <---")
            print("NAME -", row[1])
            print("CLOCK_SPEED -", row[2])
            print("CORES -", row[3])
            print("CACHE_SIZE -", row[4])
            print("PRICE -", row[5])

    elif response == 2:
        # Retrieves certain CPU via name and prints how many there are with that same name inputted.
        response = menu.create_menu_reply("FIND CPU BY NAME", "Send the name of the CPU you want to find", "string", True)

        cursor = conn.execute("""SELECT id, name, clock_speed, cores, cache_size, price from TYPES WHERE name = ?""", (response,))
        found = False
        for row in cursor:
            found = True
            print("--> FOUND ID: " + str(row[0]) + " <---")
            print("NAME -", row[1])
            print("CLOCK_SPEED -", row[2])
            print("CORES -", row[3])
            print("CACHE_SIZE -", row[4])
            print("PRICE -", row[5])

        if not found:
            print("Searched database, no matches found")
    return
