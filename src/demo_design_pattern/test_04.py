from typing import Dict
import test_05
import pprint


class Model:
    """Data Store Class"""
    def __init__(self, _file):
        self.first_file = test_05.FileFactory().file_referencer(_file)
        self.data = self.first_file.read()

    # def __get__(self, obj, klas):
    #     return [item for item in self.data['data']]


class BusinessLogic:
    """Business logic holding data store instances"""
    def __init__(self, filetype):
        self.filetype = filetype
        self.model = Model(self.filetype)
        # self.model.first_file = self.model.first_file

    def user_list(self) -> list[Dict]:
        return [item for item in self.model.data["data"]]

    def user_information(self, name: str) -> list[Dict]:
        _list = self.model.data["data"]
        return [item for item in _list if item['name'] == name]

    def add(self, item):
        return self.model.first_file.write(item)

    def convert(self, filetype_to):
        read_handle = self.model.first_file.read()
        second_file = test_05.FileFactory().file_referencer(filetype_to)
        return second_file.read(read_handle)

    def display(self):
        return self.model.first_file.read()

    def filter(self, search_string=None):
        read_handle = self.model.first_file.read()
        # remove wild character from search_string
        _str = ''.join(letter for letter in search_string if letter.isalnum())
        filtered_list = [dictionary for dictionary in read_handle if _str in dictionary['name']]
        return filtered_list

    def list_of_file_types(self):
        _file_factory = test_05.FileFactory()
        return _file_factory.ALL_TYPES

class Ui:
    """UI interaction class"""

    def __init__(self, filetype) -> None:
        self.filetype = filetype
        self.business_logic = BusinessLogic(self.filetype)

    def get_user_list(self) -> None:
        print("USER LIST:")
        for user in self.business_logic.user_list():
            print(user)
        print("")

    def get_item_information(self, user: str) -> None:
        user_info = self.business_logic.user_information(user)
        if user_info:
            print("USER INFORMATION:")
            if isinstance(user_info, list):
                for user in user_info:
                    print(
                        f"Name: {user.get('name')}, "
                        + f"Phone: {user.get('phone')}, "
                        + f"Address: {user.get('address')}"
                    )
        else:
            print(f"That user '{user}' does not exist in the items")

    def call_add(self, item: Dict) -> None:
        new_data = self.business_logic.add(item)
        if new_data:
            print(f'ADDED INFORMATION: ')
            for user in new_data['data']:
                print(
                    f"Name: {user.get('name')}, "
                    + f"Phone: {user.get('phone')}, "
                    + f"Address: {user.get('address')}"
                )

    def call_convert(self, filetype_to: str) -> None:
        filetype_from = self.business_logic.model.first_file.name
        converted_file = self.business_logic.convert(filetype_to)
        if converted_file:
            print(f'FROM {filetype_from} :\n')
            if isinstance(converted_file, Dict) and isinstance(converted_file['data'], list):
                for user in converted_file['data']:
                    print(
                        f"Name: {user.get('name')}, "
                        + f"Phone: {user.get('phone')}, "
                        + f"Address: {user.get('address')}"
                    )
        else:
            print(f"That file '{filetype_to}' does not exist in the items")

    def call_filter(self, search_string: str) -> None:
        filtered_list = self.business_logic.filter(search_string)
        if filtered_list:
            print('FILTERED INFORMATION: ')
            if isinstance(filtered_list, list):
                for item in filtered_list:
                    print(
                        f"Name: {item.get('name')}, "
                        + f"Phone: {item.get('phone')}, "
                        + f"Address: {item.get('address')}"
                    )
        else:
            print(f"That criteria {search_string} did not match")

    def call_display(self, filetype_from) -> None:
        # TODO add html format to display
        print(f'FROM {filetype_from} :\n')
        display_data = self.business_logic.display()
        if display_data:
            print('DISPLAYED DATA: ')
            if isinstance(display_data, Dict):
                display_data = [display_data]
                for item in display_data:
                    print(
                        f"Name: {item.get('name')}, "
                        + f"Phone: {item.get('phone')}, "
                        + f"Address: {item.get('address')}"
                    )
        else:
            print(f"That file type {filetype_from} does not exist")

    def call_list_of_all_types(self):
        print(f'ALL FILE TYPES: ')
        all_types = self.business_logic.list_of_file_types()
        if all_types:
            for each in all_types:
                print(f"{each}")
        else:
            print(f"Error reading object {test_05.FileFactory}")


def main():
    filetype = 'Yaml'
    ui = Ui(filetype)
    # ui.get_user_list()
    # ui.get_item_information('A')
    # ui.get_item_information("C")
    data = {'name': 'C', 'phone': 23463467443414, 'address': 'a\\b building no Y, floor Y, landmark, city, state pincode '}
    ui.call_add(data)


if __name__ == "__main__":
    main()
