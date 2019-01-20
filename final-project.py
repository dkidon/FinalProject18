import random
check_answer = ''
book_choice = ''
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

    def sneak(self):
        rnd = random.randint(0,1)
        if rnd == 0:
            return True
        else:
            return False

    def rnd_attack(self):
        atk = random.choice(["attack", "defend"])
        return atk
class Combat_manager():
    def check_attack(self, pc, npc):
        while not pc.is_dead() and not npc.is_dead():
            atk = self.check_answer("Will you attack or defend?", ["attack" , "defend"])
            print("Player " + atk)
            npc_atk = npc.rnd_attack()
            print("npc " + npc_atk)

            if atk == "attack":
                if npc_atk == "attack":
                    pc.take_dmg(npc.get_atk())
                    npc.take_dmg(pc.get_atk())
                else:
                    pc.take_dmg(npc.get_atk()/2)
                    npc.take_dmg(pc.get_atk()/3)
            else:
                if npc_atk == "attack":
                    npc.take_dmg(pc.get_atk()/2)
                    pc.take_dmg(npc.get_atk()/3)
                else:
                    print("No damage")
            print("Player has " + str(pc.hp) + " hitpoints ")
            print("NPC has " + str(npc.hp) + " hitpoints ")
    def check_answer(self, question, answers):
        answer = " "
        while answer not in answers:
            answer = input(question).lower()
        return answer


class Story():
    def __init__(self):
        self.cm = Combat_manager()
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

    def dead(self):
        print("You are dead.")
        answer = check_answer("Do you want to start again?", ["yes" , "no"])

        if answer == "yes":
            self.new_game()
        else:
            print("Game Over!")

    def outside(self):
        print("You are a slave. Your master has brought you to the dark cave.")
        print("Many people have died here before.")
        print("You master commands that you enter the cave to collect the Evil book of spells.")

        answer = self.check_answer("Do you enter the cave?", ["yes" , "no"])

        if answer == "yes":
            self.cave()
        else:
            print("When you say no, your master draws his sword and kills you.")
            self.dead()

    def cave(self):
        skel = Character(hp = 50, ap = 8)

        print("You enter the cave. Inside, there is a skeleton with a key on its neck on an alter. Across the room there is a chest.")
        options = ["Leave the cave", "take the key", "sneak to the chest", "walk to the chest"]
        print("You can:")

        for item in options:
            print(item)

        answer = self.check_answer("What will you do?", options)

        if answer.lower() in ['leave the cave','leave']:
            print("You don't have the book so your master kills you.")
            self.dead()
        elif answer == "take the key":
            print("You take the key but the skeleton wakes up and attacks you")
            self.cm.check_attack(self.pc, skel)
            if self.pc.is_dead():
                print("The skeleton wins the fight! You are dead.")
                self.dead()
            else:
                self.chest()

        elif answer == "sneak to the chest":
            print("You attempt to sneak to the chest.")
            if self.pc.sneak():
                print("You managed to sneak to the chest")
                print("You obtained the Evil Spell Book.")
                book_choice

            else:
                print("When you try to sneak past the skeleton wakes up and attacks you.")
                self.cm.check_attack(self.pc, skel)
                if self.pc.is_dead():
                    print("The skeleton wins the fight! You are dead.")
                    self.dead()
                else:
                    self.chest()
        else:
            print("You walk to the chest, but the skeleton wakes up and attacks you.")
            self.cm.check_attack(self.pc, skel)
            if self.pc.is_dead():
                print("The skeleton wins the fight! You are dead.")
                self.dead()
            else:
                self.chest()

    def chest(self):
        print("You get to the chest")
        print("You obtained the Evil Spell Book.")
        book_choice = input("Will you return the book to your master, or try to escape?").lower()
        if book_choice in ['return the book','return the book to your master','return','return to your master']:
            print("You leave the cave and return the book to your master.")
            print("He no longer needs you so he disposes of you.")
            print("Game Over!")


new_game = Story()
