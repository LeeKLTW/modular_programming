import data_storage


def prompt_for_action():
    while True:
        print()
        print("What would you like to do?")
        print()
        print(" A = Add an item to inventory.")
        print(" R = Remove an item from inventory.")
        print(" C = Generate a report of the current inventory level.")
        print(" O = Generate a report of the inventory items to reorder.")
        print(" Q = Quit.")
        print()
        action = input("> ").strip().upper()
        if action == "A":
            return "ADD"
        elif action == "R":
            return "REMOE"
        elif action == "C":
            return "INVENTORY_REPORT"
        elif action == "O":
            return "REORDER_REPORT"
        elif action == "Q":
            return "QUIT"
        else:
            print("Unknown action.")


def prompt_for_product():
    while True:
        print()
        print("Select a product:")
        print()
        n = 1
        for code, description, desired_number in data_storage:
            print(f'{n}. {code} -{description}')
            n += 1
        s = input("> ").strip()
        if s == "": return None

        try:
            n = int(s)
        except ValueError:
            n = -1

        if n < 1 or n > len(data_storage.products()):
            print(f"Invalid option:{s}")
            continue

        product_code = data_storage.products()[n - 1][0]

        return product_code


def prompt_for_location():
    while True:
        print()
        print("Select a location:")
        print()
        n = 1
        for code, description in data_storage.locations():
            print(f"{n}. {code} - {description}")
            n += 1
        s = input("> ").strip()
        if s == "": return None

        try:
            n = int(s)
        except ValueError:
            n = -1

        if n < 1 or n > len(data_storage.locations()):
            print(f"Invalid option: {s}")
            continue

        location_code = data_storage.locations()[n - 1][0]
        return location_code


def show_report(report):
    print()
    for line in report:
        print(line)
    print()
