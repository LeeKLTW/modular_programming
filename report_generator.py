import data_storage


def generate_inventory_report():
    product_name = {}
    for product_code, name, desired_number in data_storage.products():
        product_name[product_code] = name
    location_name = {}

    for location_code, name in data_storage.locations():
        location_name[location_code] = name

    grouped_items = {}
    for product_code, location_code in data_storage.items():
        if product_code not in grouped_items:
            grouped_items[product_code] = {}

        if location_code not in grouped_items[product_code]:
            grouped_items[product_code][location_code] = 1
        else:
            grouped_items[product_code][location_code] += 1

    report = []
    report.append("INVENTORY REPORT")
    report.append("")

    for product_code in sorted(grouped_items.keys()):
        product_name = product_name[product_code]
        report.append(f"Inventory for product:{product_code} - {product_name}")
        report.append("")
        for location_code in sorted(grouped_items[product_code].keys()):
            location_name = location_name[location_code]
            num_items = grouped_items[product_code][location_code]
            report.append(f"{num_items} at { location_code} - {location_name}")
        report.append("")
    return report


def generate_reorder_report():
    pass
