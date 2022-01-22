from __future__ import annotations
from typing import Callable


class Menu:
    def __init__(self, start_at_one=False, separator=":", parent: Menu = None):
        """Simple Menu Implementation

        start_at_one -- Menu starts count at 1.\n
        separator -- separator to use (default ":") example: "1: item"
        """
        self.items = []
        self.start_at_one = start_at_one
        self.separator = separator

        self.__parent = parent

    def add_item(self, desc: str, callback: Callable):
        """Add item to menu

        desc -- text to show\n
        callback -- function to call on choice
        """
        self.items.append({"desc": desc, "callback": callback})

    def add_submenu(self, desc: str, start_at_one=None, allow_back=True) -> Menu:
        """Add submenu as item

        desc -- text to show\n
        start_at_one -- count from 1 (default topmenu.start_at_one)
        """
        if start_at_one is None:
            start_at_one = self.start_at_one

        if allow_back:
            submen = Menu(start_at_one, parent=self)
        else:
            submen = Menu(start_at_one)
        self.items.append({"desc": desc, "callback": submen.run})
        return submen

    def __show(self):
        """Print menu."""
        for idx, item in enumerate(self.items):
            print(f"{idx+self.start_at_one}{self.separator} {item.get('desc')}")

    def run(self):
        if self.__parent is not None:
            self.add_item("back", self.__parent.run)

        self.__show()

        while True:
            try:
                choice = int(input("> ")) - self.start_at_one
            except ValueError:
                choice = -1

            if choice in range(0, len(self.items)):
                break
            print("Not an option")

        self.items[choice].get("callback")()
