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
room_1 = True
room_1_left = False
left_corridor = False
room_1_right = False
bear_choice = False

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
first_room_door = ["left" , "right" , "forward"]
field_choice = ["north" , "south"]
while room_1:
    while first_room_door_choice.lower() not in first_room_door:
        first_room_door_choice = input("Will you go left, right, or forward?")

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
        print("Are you sure you want to take this path?")
        left_door_exit = input("Yes/No")
    if left_door_exit.lower() in ['no','nope','n']:
        print("Choose again!")
        first_room_door_choice = input("Will you go left, right, or forward?")
    elif left_door_exit.lower() in ['yes', 'y' , 'yup']:
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
        bear_choice = input('Will you run or try to get by the bear?')
    if bear_choice.lower() in ['get by','by']:
        print("Come on player!")
        print("The bear heard you from a mile away and woke up.")
        print("Game over!")
        left_corridor = False
    if bear_choice.lower() in ['run','r','escape']:
        print("The bear wakes up and chases you.")
        print("You have a split second to make a decision.")
        bear_runner = input("Will you fight, or continue to run.")
    if bear_runner.lower() in ['run', 'escape']:
        print("You run out of stamina and start to slow down.")
        print("The bear catches up to you and rips you to shreds.")
        print("Game Over!")
        left_corridor = False
    if bear_runner.lower() in ['fight','f','battle']:
        print("Right as you start slowing down, you turn around and wack the bear in the nose with your flashlight.")
        print("The bear faints.")


    elif dark_choice.lower() in ['no','n','n']:
        print("You continue to wander in the long corridor and you get hopelessly lost.")
        print("Game over. Try again!")
        left_corridor = False

while room_1_right:
    if first_room_door_choice.lower() in ['right','r']:
        print("You walk to the door and open it to see a large open field.")
        time.sleep(1)
        print("Are you sure you want to take this path?")
        right_door_exit = input("Yes/No")
    if right_door_exit.lower() in ['no','nope', 'n']:
        print("Choose again!")
        first_room_door_choice = input("Will you go left, right, or forward?")
    elif right_door_exit.lower() in ['yes','y','yup']:
        print("You walk into the large field and look around.")
        print("To the north you see mountains, and to the south you see a forest.")
        field_choice = input("Will you go north or south?")
    if field_choice.lower() in ['north','n']:
        print("You start to head to the mountains.")
        print("All of a sudden, a huge meteor crashes right in front of you!")
        alien_choice = input("Do you want to run or stay and meet them?")
    if alien_choice.lower() in ['run','run away','r']:
        print("While running away, another meteor completely crushes you.")
        print("Game Over!")
        room_1_right = False
    if alien_choice.lower() in ['stay','meet them']:
        print("The meteor opens up and you see a figure standing in the doorway.")
        print("The figure beckons for you to come forward.")
        forward = input("Will you go forward or try to escape?")
    if forward.lower() in ['escape','run']:
        print("The alien takes offense to you running away.")
        print("He pulls out his blaster and shoots you in the back!")
        time.sleep(1)
        print("Game Over!")
        room_1_right = False






