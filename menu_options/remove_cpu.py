from handlers import menu


def send_menu(conn):
    response = menu.create_menu_reply("REMOVE CPU QUESTION", "Please reply with the CPU name you want to delete", "string")

    conn.execute("""DELETE FROM TYPES WHERE NAME = ?""", (response,))
    conn.commit()

    print("Deleted/Removed any CPU's matching that name.")
    return
