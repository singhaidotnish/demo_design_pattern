"""
http://code.activestate.com/recipes/131499-observer-pattern/

*TL;DR
Maintains a list of dependents and notifies them of any state changes.

*Examples in Python ecosystem:
Django Signals: https://docs.djangoproject.com/en/3.1/topics/signals/
Flask Signals: https://flask.palletsprojects.com/en/1.1.x/signals/
"""

from __future__ import annotations

import json
import yaml
from contextlib import suppress
from typing import Protocol


# define a generic observer type
class Observer(Protocol):
    def update(self, subject: Subject) -> None:
        pass


class Subject:
    def __init__(self) -> None:
        self._observers: list[Observer] = []

    def attach(self, observer: Observer) -> None:
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        with suppress(ValueError):
            self._observers.remove(observer)

    def notify(self, modifier: Observer | None = None) -> None:
        for observer in self._observers:
            if modifier != observer:
                observer.update(self)

class Data(Subject):
    def __init__(self) -> None:
        super().__init__()
        self._data = dict()

    @property
    def data(self) -> dict:
        return self._data

    @data.setter
    def data(self, value: dict) -> None:
        self._data = value
        self.notify()


class JsonViewer:
    def update(self, subject: Data) -> None:
        json_object = json.dumps(subject.data, indent=4)
        print(f"JsonViewer: \n\n{json_object}\n")


class YamlViewer:
    def update(self, subject: Data) -> None:
        yaml_object = yaml.dump(subject.data, indent=4)
        print(f"YamlViewer: \n\n{yaml_object}\n")


def main():
    data1 = Data()
    view1 = JsonViewer()
    data1.attach(view1)
    # TODO set dictionary here
    data1.data = {'name': 'A', 'phone': 1234567890}
    # DecimalViewer: Subject Data 1 has data 10
    # JsonViewer: Subject Data 1 has data 0xa

    # Detach JsonViewer from data1 and data2
    data1.detach(view1)

    data2 = Data()
    view2 = YamlViewer()
    data2.attach(view2)
    data2.data = {'name': 'B', 'phone': 232323232323, 'address': 'a\\b building no Y, floor Y, landmark, city, state pincode '}
    data2.detach(view2)

if __name__ == "__main__":
    main()
