from handlers import validation


# Creates Menu Option Menu
def create_menu_option(title, options, back_menu):
    # Prints out options.
    print("---> " + title + " <---")
    for i in range(len(options)):
        print(str(i+1) + ") " + options[i])

    # If back menu enabled, it adds an extra option
    if back_menu:
        print(str(len(options)+1) + ") " + "Back to main menu")

    # Validates response as integer
    validated = False
    while not validated:
        response = input("Enter your choice: ")

        # Uses validation handler to make sure it's a real or not.
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
    # Prints out title and description
    print("---> " + title + " <---")
    print(desc)

    # Prints out extra option
    if back_menu:
        print("- Reply with 'menu' to go back to the main menu")

    # Validates string option
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
