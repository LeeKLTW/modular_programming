import json
import os


def _load_items():
    global _items
    if os.path.exists('items.json'):
        f = open('item.json', 'r')
        _items = json.load(f.read())
        f.close()
    else:
        _items = []


def _save_items():
    global _items
    f = open('item.json', 'w')
    f.write(json.dump(_items))
    f.close()


def init():
    _load_items()


def items():
    global _items
    return _items


def products():
    pass


def locations():
    pass


def add_item(product_code, location_code):
    pass


def remove_item(product_code, location_code):
    pass


def set_product(product):
    pass


def set_location(locations):
    pass
