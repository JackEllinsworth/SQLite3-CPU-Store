from handlers import menu

CPU_OPTIONS = ["Name", "Clock Speed", "Cores", "Cache Size", "Price"]
CPU_REAL_ONLY = ["Clock Speed", "Cores", "Cache Size", "Price"]


def send_menu(conn):
    # Collects responses for CPU_OPTIONS.
    responses = []

    # Creates a menu for every option input.
    for i in range(len(CPU_OPTIONS)):
        str_type = "string"

        if CPU_OPTIONS[i] in CPU_REAL_ONLY:
            str_type = "real"

        response = menu.create_menu_reply("STEP " + str(i + 1) + ": " +
                                          CPU_OPTIONS[i], "Please reply with the value: " + CPU_OPTIONS[i], str_type, True)
        if response == "menu": return

        # Appends collected response to responses variable.
        responses.append(response)

    # Executes instructions on database
    conn.execute("INSERT INTO TYPES (NAME,CLOCK_SPEED,CORES,CACHE_SIZE,PRICE) \
                 VALUES (?,?,?,?,?)", (responses[0:5]))
    # Commits to database
    conn.commit()

    print("[SUCCESS] Added to database successfully.")
    return
