import random
check_answer = ''
book_choice = ''
class Character():

    def __init__(self, name = "none", hp = 100, ap = 30):
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
        print("Welcome to The Cave!")
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
        print("You are a slave. Your evil master has brought you to a dark cave.")
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
        options = ["leave the cave", "take the key", "sneak to the chest", "walk to the chest"]
        print("You can:")

        for item in options:
            print(item)

        answer = self.check_answer("What will you do?", options).lower()

        if answer in ["leave the cave"]:
            print("You don't have the book so your master kills you.")
            self.dead()
        if answer == "take the key":
            print("You take the key but the skeleton wakes up and attacks you")
            self.cm.check_attack(self.pc, skel)
            if self.pc.is_dead():
                print("The skeleton wins the fight! You are dead.")
                print("Game Over!")
                self.dead()
            else:
                self.chest()

        elif answer == "sneak to the chest":
            print("You attempt to sneak to the chest.")
            if self.pc.sneak():
                print("You managed to sneak to the chest")
                self.chest()

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
        print("You get to the chest and open it.")
        print("You obtained the Evil Spell Book.")
        book_choice = input("Will you return the book to your master, or try to escape?").lower()
        if book_choice in ['return the book','return the book to your master','return','return to your master']:
            print("You leave the cave and return the book to your master.")
            print("He no longer needs you so he disposes of you.")
            print("Game Over!")
        if book_choice in ["try to escape","escape","run"]:
            print("You run deep into the cave.")

        import time
        left_door_choice = ''
        first_room_door_choice = ''
        left_door_exit = ''
        right_door_exit = ''
        candy = ''
        bear_choice = ''
        bear_runner = ''
        field_choice = ''
        alien_choice = ''
        forward = ''
        alien_kill = ''
        alien_ship = ''
        kill_bear = ''
        follow_bear = ''
        bow = ''
        deer = ''
        forward_wait = ''
        room_1 = True
        room_1_left = False
        left_corridor = False
        room_1_right = False
        bear_choice = False
        field_choice = False
        room_1_forward = False

        time.sleep(2)
        def first_room():
            print("You stumble through the dark and somehow find yourself in a small room.")
            print("The walls are wooden, and you assume you are in a wood cabin.")
            print("There are two doors, one to your left, and one to your right")
        first_room()
        first_room_door = ["left" , "right"]
        field_choice = ["north" , "south"]

        while True:
            while room_1:
                while first_room_door_choice.lower() not in first_room_door:
                    first_room_door_choice = input("Will you go left or right?")

                if first_room_door_choice.lower() in ['left','l']:
                    room_1_left = True
                    left_corridor = True
                if first_room_door_choice.lower() in ['right','r']:
                    room_1_right = True

                print(f"You chose {first_room_door_choice}.")
                room_1 = False

            while room_1_left:
                if first_room_door_choice.lower() in ['left','l']:
                    print("You walk to the door and open it to see a long, dark corridor.")
                    time.sleep(1)
                    print("You start walking down the dark corridor.")
                    print("You feel your foot hit something.")
                    time.sleep(1)
                    print("Do you want to risk picking it up?")
                    room_1_left = False

            while left_corridor:
                dark_choice = input("Yes/No")
                if dark_choice.lower() in ['yes','y','yup']:
                    print("You picked up a flashlight! You can now see where you are.")
                    print("You start to walk forward.")
                    print("You see a piece of candy on the ground.")
                    time.sleep(1)
                    print("Will you eat it?")
                    candy = input('Yes/No')
                if candy.lower() in ['yes','yeah','y']:
                    print("The candy was poisoned and you died!")
                    print("Game Over! Try again!")
                    left_corridor = False
                elif candy.lower() in ['no','nope','n']:
                    print('You walk away from the candy.')
                    print('All of a sudden, you see a bear!')
                    bear_choice = input('Will you run or try to get by the bear?').lower()
                if bear_choice in ['get by','by','try to get by','try']:
                    print("Come on! The bear heard you from a mile away.")
                    print("It rips you apart.")
                    print("Game over!")
                    left_corridor = False
                if bear_choice in ['run','r','escape']:
                    print("The bear wakes up and chases you.")
                    print("You have a split second to make a decision.")
                    bear_runner = input("Will you fight, or continue to run.")
                if bear_runner.lower() in ['run', 'escape', 'continue to run']:
                    print("You run out of stamina and start to slow down.")
                    print("The bear catches up to you and rips you to shreds.")
                    print("Game Over!")
                    left_corridor = False
                if bear_runner.lower() in ['fight','f','battle']:
                    print("Right as you start slowing down, you turn around and wack the bear in the nose with your flashlight.")
                    print("The bear faints.")
                    kill_bear = input("Will you kill the bear, or be merciful and spare him?").lower()
                if kill_bear in ['kill the bear','kill']:
                    print("You finish the bear off with your flashlight, but as you do so the flashlight snaps in half!")
                    print("Since you have no light, you get hopelessly lost and starve.")
                    print("Game Over!")
                    left_corridor = False
                if kill_bear in ['merciful','mercy','spare','spare him','be merciful']:
                    print("As the bear comes to, he looks up at you with respect.")
                    print("He starts to walk away from you, and looks back at you, as if for you to follow.")
                    follow_bear = input("Will you follow the bear?").lower()
                if follow_bear in ['follow the bear','follow','yes']:
                    print("The bear leads you out of the maze of corridors.")
                    print("Congratulations you found the way out!")
                    print("Play again to discover the other endings!")
                if dark_choice.lower() in ['no','n','n']:
                    print("You continue to wander in the long corridor and you get hopelessly lost.")
                    print("Game over. Try again!")
                    left_corridor = False

            while room_1_right:
                if first_room_door_choice.lower() in ['right','r']:
                    print("You walk to the door and open it to see a large open field.")
                    time.sleep(1)
                    print("You walk into the large field and look around.")
                    print("To the north you see mountains, and to the south you see a forest.")
                    field_choice = input("Will you go north or south?").lower()
                if field_choice in ['south','s']:
                    print("You start to head towards the forest.")
                    print("Along the way, you come across a bow and arrow on the ground.")
                    print("Do you want to pick it up?")
                    bow = input("Yes/No").lower()
                if bow in ['yes','y']:
                    print("You obtained a bow and arrow!")
                    print("You continue into the forest.")
                    print("You come up to a clearing and see a deer.")
                    print("Do you want to try to shoot it?")
                    deer = input("Yes/No").lower()
                if deer in ['yes','y','yeah']:
                    print("As you shoot, the deer is suddenly pulled away by some invisible force.")
                    print("You stop in confusion and the force turns onto you.")
                    print("Game Over!")
                    room_1_right = False
                if deer in ['no','nah','n']:
                    print("The deer is suddenly pulled away by some invisible force.")
                    forward_wait = input("Do you want to continue forward or wait.")
                if forward_wait in ['wait','w']:
                    print("You wait too long and the force catches onto you.")
                    print("You get ripped apart by the force.")
                    print("Game Over!")
                    room_1_right = False
                if forward_wait in ['go forward','continue','continue forward','go','forward']:
                    print("You run past the force and manage to get out of the woods.")
                    print("Congratulations you escaped your evil master.")
                    print("PLay again to discover the other paths.")
                    room_1_right = False
                if bow in ['no','nah','n']:
                    print("You walk past the bow and continue into the forest.")
                    print("You hear a cool breeze behind you and see your worst fear in the world.")
                    print("You run to the nearest cliff and jump off of it.")
                    print("Game Over!")
                    room_1_right = False

                if field_choice in ['north','n']:
                    print("You start to head to the mountains.")
                    print("All of a sudden, a huge meteor crashes right in front of you!")
                    alien_choice = input("Do you want to run away or stay?")
                if alien_choice.lower() in ['run','run away','r']:
                    print("While running away, another meteor completely crushes you.")
                    print("Game Over!")
                    room_1_right = False
                if alien_choice.lower() in ['stay','meet them']:
                    print("The meteor opens up and you see a figure standing in the doorway.")
                    print("The figure beckons for you to come forward.")
                    forward = input("Will you go forward or try to escape?")
                if forward.lower() in ['escape','run','try to escape','try to']:
                    print("The alien takes offense to you running away.")
                    print("He pulls out his blaster and shoots you in the back!")
                    time.sleep(1)
                    print("Game Over!")
                    room_1_right = False
                if forward.lower() in ['go forward','go','forward']:
                    print("The alien welcomes you with open arms.")
                    print("He shows you around his ship and ends up giving you his blaster.")
                    alien_kill = input("Will you be ruthless and kill the alien, or be friendly and shake his hand?").lower()
                if alien_kill in ['shake','shake his hand','be friendly','friendly']:
                    print("The alien takes your hand and rips it off!")
                    print("He shoots you in the chest and bites your head off.")
                    print("Game Over!")
                    room_1_right = False
                if alien_kill in ['be ruthless','kill','ruthless','kill the alien']:
                    print("Good job!")
                    print("The alien was going to take over the world.")
                    print("Congratulations for defeating him!")
                    alien_ship = input("Do you want to take the ship for a ride, or do you want to step outside?").lower()
                if alien_ship in ['take the ship for a ride','ride','take the ship','fly']:
                    print("The meteorite is actually a spaceship.")
                    print("You step to the control panel and slowly start to figure out how to fly the ship.")
                    print("You fly off into deep space, leaving Earth behind to continue your adventure.")
                    print("Congratulations! You escaped from your evil master and saved the world!")
                    print("Play again to discover the other paths!")
                    room_1_right = False
                if alien_ship in ['step outside','step','outside','leave']:
                    print("While running away, another meteor completely crushes you.")
                    time.sleep(1)
                    print("You escaped from your evil master, but couldn't escape the universe.")
                    print("Game Over!")
                    room_1_right = False


new_game = Story()



