import random
import time

def intro():
    print("Welcome traveler!")
    print("You are about to embark on a long journey, one filled with peril and danger!")
    print("I will be your guide through this adventure.")

git add final-project.py
git status
git commit -m "Redone introduction for easy reading."
git push origin master

def first_room():
    print("You wake up in a dark room.")
    print("The walls are wooden, and you assume you are in a wood cabin.")
    print("There are three doors, one to your left, one to your right, and one in front of you.")
first_room_door = ["left" , "right" , "front"]
first_room_door_choice = input(f"What is your choice")
if first_room_door_choice not in first_room_door:
    print(
choice = input
intro()