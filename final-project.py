import random

class Character():

    def __init__(self, name = "none", hp = 100, ap = 10):
        self.name = name
        self.hp = hp
        self.ap = ap
        self.items = ["Sword","health potion"]

    def take_dmg(self, dmg):
        self.hp = self.hp - dmg

    def is_dead(self):
        if self.hp < 1:
            return True
        else:
            return False

    def get_atk(self):
        atk = random.randint(0, self.ap)
        return atk

class Story():
    def __init__(self):
        print("Welcome to the Dark Cave")

new_game = Story()



