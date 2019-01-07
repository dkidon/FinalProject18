import random
import time

def intro():
    print("Welcome traveler!")
    print("You are about to embark on a long journey, one filled with peril and danger!")
    print("I will be your guide through this adventure.")
intro()
time.sleep(3)
def first_room():
    print("You wake up in a dark room.")
    print("The walls are wooden, and you assume you are in a wood cabin.")
    print("There are three doors, one to your left, one to your right, and one in front of you.")
first_room()
first_room_door = ["left" , "right" , "front"]
while True:
    first_room_door_choice = input("Which way will you go?")
    if first_room_door_choice not in first_room_door:
        print("Sorry, that's not a possible choice. Pick again!")
    else:
        print(f"You chose {first_room_door_choice}.")
        break
if first_room_door_choice == "left":
    print("You walk to the door and open it to see a long, dark corridor.")
    print("Are you sure you want to take this path?")
    left_door_exit = input("Yes/No")
    if left_door_exit == "No":
        print("Okay.")
    elif left_door_exit == "Yes":
        print("Okay.")