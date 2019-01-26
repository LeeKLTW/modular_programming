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
    global _products
    return _products


def locations():
    global _locations
    return _locations


def add_item(product_code, location_code):
    global _items
    _items.append((product_code, location_code))
    _save_items()


def remove_item(product_code, location_code):
    global _items
    for i in range(len(_items)):
        p_code, l_code = _items[i]
        if p_code == product_code and l_code == location_code:
            del items[i]
            _save_items()
            return True
    return False


def set_product(products):
    global _products
    _products = products
    pass


def set_location(locations):
    global _locations
    _locations = locations
