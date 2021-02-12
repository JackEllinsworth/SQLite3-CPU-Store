from handlers import validation


def create_menu_option(title, options, back_menu):
    print("---> " + title + " <---")
    for i in range(len(options)):
        print(str(i+1) + ") " + options[i])

    if back_menu:
        print(str(len(options)+1) + ") " + "Back to main menu")

    validated = False
    while not validated:
        response = input("Enter your choice: ")

        valid = validation.check_real(response)
        if valid:
            if back_menu:
                if valid == len(options)+1:
                    return "menu"
            if len(options) >= valid >= 1:
                return valid
            else:
                print("[ERR] Validation Error")
        else:
            print("[ERR] Validation Error")


def create_menu_reply(title, desc, str_type, back_menu):
    print("---> " + title + " <---")
    print(desc)

    if back_menu:
        print("- Reply with 'menu' to go back to the main menu")

    validated = False
    while not validated:
        response = input("Enter your choice: ")

        if response == "menu" and back_menu:
            return "menu"

        if str_type == "string":
            if len(response) > 0:
                return response
            else:
                print("[ERR] Validation Error")
        elif str_type == "real":
            valid = validation.check_real(response)
            if valid:
                return response
            else:
                print("[ERR] Validation Error")
