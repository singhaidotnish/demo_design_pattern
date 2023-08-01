"""
*TL;DR
Separates presentation, application processing, and data management functions.
"""

import os
import glob
from typing import Dict, KeysView, Optional, Union
from .test_05 import FileFactory
import pprint


class Data:
    """Data Store Class"""
    def __init__(self, _file):
        first_file = FileFactory().file_referencer(_file)
        self._data = first_file.read()
    # products = {
    #     "milk": {"price": 1.50, "quantity": 10},
    #     "eggs": {"price": 0.20, "quantity": 100},
    #     "cheese": {"price": 2.00, "quantity": 10},
    # }
    # TODO products to come from read file
    #     products = {
    #         123321231: {
    #             "name": "A",
    #             "address": "a\\b building no X, floor X, landmark, city, state pincode "
    #         },
    #         1234567890: {
    #             "name": "A",
    #             "address": "a\\b building no X, floor X, landmark, city, state pincode "
    #         }
    # }

    def __get__(self, obj, klas):

        print("(Fetching from Data Store)")
        return {"data": self._data}


class BusinessLogic:
    """Business logic holding data store instances"""
    def __init__(self, filetype_from, filetype_to):
        self.filetype_from = filetype_from
        self.filetype_to = filetype_to
        self.data = Data(self.filetype_from)

    def product_list(self) -> KeysView[int]:
        return self.data["data"].keys()

    def product_information(self, product: int) -> Optional[Dict[str, Union[str, str]]]:
        return self.data["data"].get(product, None)

    def add(self):
        # TODO call write from test_05
        pass

    def convert(self, filetype_from, filetype_to):
        first_file = FileFactory().file_referencer(filetype_from)
        read_handle = first_file.read()

    def display(self, filetype):
        first_file = FileFactory().file_referencer(filetype)
        read_handle = first_file.read()
        pprint.pprint(read_handle)

    def filter(self, filetype, search_string=None):
        first_file = FileFactory().file_referencer(filetype)
        read_handle = first_file.read()
        # remove wild character from search_string
        _str = ''.join(letter for letter in search_string if letter.isalnum())
        filtered_list = [dictionary for dictionary in read_handle if _str in dictionary['name']]
        pprint.pprint(filtered_list)



class Ui:
    """UI interaction class"""

    def __init__(self) -> None:
        self.business_logic = BusinessLogic()

    def get_product_list(self) -> None:
        # TODO call filter with filetype
        print("PRODUCT LIST:")
        for product in self.business_logic.product_list():
            print(product)
        print("")

    def get_product_information(self, product: int) -> None:
        product_info = self.business_logic.product_information(product)
        if product_info:
            print("PRODUCT INFORMATION:")
            print(
                f"Name: {product_info.get('name')}, "
                + f"Phone: {product}, "
                + f"Quantity: {product_info.get('address')}"
            )
        else:
            print(f"That product '{product}' does not exist in the records")


def main():
    ui = Ui()
    ui.get_product_list()
    # PRODUCT LIST:
    # (Fetching from Data Store)
    # milk
    # eggs
    # cheese
    # <BLANKLINE>

    ui.get_product_information(123321231)
    # (Fetching from Data Store)
    # PRODUCT INFORMATION:
    # Name: Cheese, Price: 2.00, Quantity: 10

    # ui.get_product_information("eggs")
    # # (Fetching from Data Store)
    # # PRODUCT INFORMATION:
    # # Name: Eggs, Price: 0.20, Quantity: 100
    #
    # ui.get_product_information("milk")
    # # (Fetching from Data Store)
    # # PRODUCT INFORMATION:
    # # Name: Milk, Price: 1.50, Quantity: 10

    ui.get_product_information("arepas")
    # (Fetching from Data Store)
    # That product 'arepas' does not exist in the records


if __name__ == "__main__":
    main()
