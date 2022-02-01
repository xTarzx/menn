from menu import Menu


class Player:
    def __init__(self):
        self.hp = 10

    def take_dmg(self, v):
        self.hp -= v

    def show_hp(self):
        print(self.hp)


player = Player()

menu = Menu(True)
menu.add_item("damage", player.take_dmg, (3,))
menu.add_item("show", player.show_hp)
menu.add_exit()
menu.run(True)
