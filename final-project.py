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
        self.new_game()
    def check_answer(self, question, answers):
        answer = " "
        while answer not in answers:
            answer = input(question).lower()
        return answer
    def new_game(self):
        self.create_char()
        self.outside()
    def create_char(self):
        name = input("Please enter a name for your character: ")
        self.pc = Character(name)
    def outside(self):
        print("You are a slave. Your master has brought you to the dark cave.")
        print("Many people have died here before.")
        print("You master commands that you enter the cave to collect the Evil book of spells.")

        self.check_answer("Do you enter the cave?", ["yes" , "no"])


new_game = Story()
