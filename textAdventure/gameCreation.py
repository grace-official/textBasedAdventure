import random
import time

#def newGame():

print("Game starting.\n")
time.sleep(2)
print("Game starting..\n")
time.sleep(2)
print("Game starting...\n")
time.sleep(2)
print("Game starting....\n")

print("Hello! You are an Adventurer travelling through the mountains, looking for treasure!\n"
        + "You are looking for a cave entrance, and are walking on a trail. theres a fork in the road, \n "
        "which way do you go?")

goodInput = False
while not goodInput:

    try:

        menuInput = int(input("1 for left \n 2 for right"))

        if menuInput == 1:
            print("You go left")

        elif menuInput == 2:
            print("You go right")

        else:
            print("Not a valid number, please try again")

    except:
        print("Please enter a number")
