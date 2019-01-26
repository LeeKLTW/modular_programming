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
    pass


def prompt_for_location():
    pass
