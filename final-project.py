import random
import time

left_door_choice = ''
first_room_door_choice = ''

def intro():
    print("Welcome traveler!")
    print("You are about to embark on a long journey, one filled with peril and danger!")
    print("I will be your guide through this adventure.")
intro()
time.sleep(2)
def first_room():
    print("You wake up in a dark room.")
    print("The walls are wooden, and you assume you are in a wood cabin.")
    print("There are three doors, one to your left, one to your right, and one in front of you.")
first_room()
room_1 = True
room_1_left = True
room_1_right = True
first_room_door = ["left" , "right" , "forward"]
field_choice = ["north" , "south"]
while room_1:
    while first_room_door_choice.lower() not in first_room_door:
        first_room_door_choice = input("Will you go left, right, or forward?")
    if first_room_door_choice.lower() not in first_room_door:
        print("Sorry, that's not a possible choice. Pick again!")
    else:
        print(f"You chose {first_room_door_choice}.")
        break
while room_1_left:
    if first_room_door_choice.lower() == "left":
        print("You walk to the door and open it to see a long, dark corridor.")
        print("Are you sure you want to take this path?")
        left_door_exit = input("Yes/No")
    if left_door_exit.lower() in ['no','nope','n']:
        print("Choose again!")
        first_room_door_choice = input("Will you go left, right, or forward?")
    elif left_door_exit.lower() in ['yes', 'y' , 'yup']:
        print("You start walking down the dark corridor.")
        print("You feel your foot hit something.")
        print("Do you want to risk picking it up?")
        room_1 = False
while room_1_right:
    if first_room_door_choice.lower() in ['right','r']:
        print("You walk to the door and open it to see a large open field.")
        print("Are you sure you want to take this path?")
        right_door_exit = input("Yes/No")
    if right_door_exit.lower in ['no','nope', 'n']:
        print("Choose again!")
        first_room_door_choice = input("Will you go left, right, or forward?")
    elif right_door_exit.lower in ['yes','y','yup']:
        print("You walk into the large field and look around.")
        print("To the north you see mountains, and to the south you see a forest.")
        field_choice = input("Will you go north or south?")


left_corridor = True
while left_corridor:
    dark_choice = input("Yes/No")
    if dark_choice.lower() in ['yes','y','yup']:
        print("You picked up a flashlight! You can now see where you are.")
    elif dark_choice.lower() in ['no','n','n']:
        print("You continue to wander in the long corridor and you get hopelessly lost.")
        print("Game over. Try again!")
        left_corridor = False




