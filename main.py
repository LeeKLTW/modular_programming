import data_storage
import user_interface
import report_generator


def main():
    data_storage.init()
    data_storage.set_product([
        ("SKU123", "4 mm flat-head wood screw", 50),
        ("SKU145", "6 mm flat-head wood screw", 50),
        ("SKU167", "4 mm countersunk head wood screw", 10),
        ("SKU169", "6 mm countersunk head wood screw", 10),
        ("SKU172", "4 mm metal self-tapping screw", 20),
        ("SKU185", "8 mm metal self-tapping screw", 20),
    ])

    data_storage.set_location([
        ("S1A1", "Shelf 1, Aisle 1"),
        ("S2A1", "Shelf 2, Aisle 1"),
        ("S3A1", "Shelf 3, Aisle 1"),
        ("S1A2", "Shelf 1, Aisle 2"),
        ("S2A2", "Shelf 2, Aisle 2"),
        ("S3A2", "Shelf 3, Aisle 2"),
        ("BIN1", "Storage Bin 1"),
        ("BIN2", "Storage Bin 2"),
    ])

    while True:
        action = user_interface.prompt_for_action()
        if action == "QUIT":
            break
        elif action == "ADD":
            product = user_interface.prompt_for_product()
            if product != None:
                location = user_interface.prompt_for_location()
                if location != None:
                    data_storage.add_item(product, location)
        elif action == "REMOVE":
            product = user_interface.prompt_for_product()
            if product != None:
                location = user_interface.prompt_for_location()
                if location != None:
                    if not data_storage.remove_item(product, location):
                        user_interface.show_error("There is no product that code at that location.")
        elif action == "INVENTORY_REPORT":
            report = report_generator.generate_inventory_report()
            user_interface.show_report(report)

        elif action == "REORDER_REPORT":
            report = report_generator.generate_reorder_report()
            user_interface.show_report(report)


if __name__ == '__main__':
    main()
