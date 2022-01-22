from menu import Menu


def hello_world():
    print("Hello World!")


def foo():
    print("foo")


def bar():
    print("bar")


menu = Menu(True)
menu.add_item("Hello", hello_world)
submenu = menu.add_submenu("More", allow_back=False)
submenu.add_item("foo", foo)
submenu.add_item("bar", bar)

menu.run()
