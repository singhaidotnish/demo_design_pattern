from typing import List, Protocol


class Item(Protocol):
    name: str
    phone: str
    address: str


class Product:
    def __init__(self, name: str, phone: str, address: str):
        self.name = name
        self.phone = phone
        self.address = address


def calculate_total(items: List[Item]) -> List:
    return [item.get('name') for item in items]


# calculate total a product list
total = calculate_total([
        {
            "name": "A",
            "phone": 1234567890,
            "address": "a\\b building no X, floor X, landmark, city, state pincode "
        },
        {
            "name": "A",
            "phone": 1234567890,
            "address": "a\\b building no X, floor X, landmark, city, state pincode "
        },
        {
            "name": "A",
            "phone": 1234567890,
            "address": "a\\b building no X, floor X, landmark, city, state pincode "
        },
        {
            "name": "B",
            "phone": 1234567890,
            "address": "a\\b building no X, floor X, landmark, city, state pincode "
        },
        {
            "name": "C",
            "phone": 23463467443414,
            "address": "a\\b building no Y, floor Y, landmark, city, state pincode "
        },
        {
            "name": "C",
            "phone": 23463467443414,
            "address": "a\\b building no Y, floor Y, landmark, city, state pincode "
        }
    ])

print(total)