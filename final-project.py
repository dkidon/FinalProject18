print (f"Welcome traveler! You are about to embark on a long journey, one filled with peril and danger! I will be your guide through this adventure. But, before we begin...")
name = input("What is your name?")
print (f"Welcome", name,"! You have three options to start this adventure. You can either start as an elf, troll, or human.")
character_class= {"elf" , "troll", "human"}
while true:
    user = input("What is your choice. Elf, troll, or human?")
    if user not in character_class:
        print("Sorry, that's not a character choice.")
