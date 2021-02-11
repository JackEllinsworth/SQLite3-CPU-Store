from handlers import validation


def create_menu_option(title, options):
    print("---> " + title + " <---")
    for i in range(len(options)):
        print(str(i+1) + ") " + options[i])

    validated = False
    while not validated:
        response = input("Enter your choice: ")

        valid = validation.check_real(response)
        if valid:
            if len(options) >= valid >= 1:
                return valid
            else:
                print("[ERR] Validation Error")
        else:
            print("[ERR] Validation Error")


def create_menu_reply(title, desc, str_type):
    print("---> " + title + " <---")
    print(desc)

    validated = False
    while not validated:
        response = input("Enter your choice: ")
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
