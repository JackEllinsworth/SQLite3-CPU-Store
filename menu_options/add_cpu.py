from handlers import menu

CPU_OPTIONS = ["Name", "Clock Speed", "Cores", "Cache Size", "Price"]
CPU_REAL_ONLY = ["Clock Speed", "Cores", "Cache Size", "Price"]


def send_menu(conn):
    responses = []

    for i in range(len(CPU_OPTIONS)):
        str_type = "string"

        if CPU_OPTIONS[i] in CPU_REAL_ONLY:
            str_type = "real"

        response = menu.create_menu_reply("STEP " + str(i + 1) + ": " +
                                          CPU_OPTIONS[i], "Please reply with the value: " + CPU_OPTIONS[i], str_type, True)
        if response == "menu": return

        responses.append(response)

    conn.execute("INSERT INTO TYPES (NAME,CLOCK_SPEED,CORES,CACHE_SIZE,PRICE) \
                 VALUES (?,?,?,?,?)", (responses[0:5]))
    conn.commit()

    print("[SUCCESS] Added to database successfully.")
    return
