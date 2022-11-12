import random
import time

# calculates the damage
def damage():
    print("calculating damage...")
    time.sleep(1)
    print(random.randint(3, 20))

# these control the various parts of the story
def end1():
    print("You go in the completely wrong direction and get lost, oh well, better luck next time!")

def part3():
    print("as you go further into the cave, a larger monster appears, guarding the treasure, what do you do?\n")

    # while loops
    goodInput = False
    while not goodInput:

        # exception handling
        try:

            menuInput = int(input("1 for attack \n2 for run\n"))

            if menuInput == 1:
                print("You attack!\n")
                damage()
                print("The monster is defeated! you take the treasure for yourself and win!")
                goodInput = True

            elif menuInput == 2:
                print("You run\n")
                end1()
                goodInput = True

            else:
                print("Not a valid number, please try again")

        except:
            print("Please enter a number")

def part2():
    time.sleep(2)
    print("you find the cave entrance! but as you go inside a small monster jumps out! \n what do you do?")

    goodInput = False
    while not goodInput:

        try:

            menuInput = int(input("1 for attack \n2 for run\n"))

            if menuInput == 1:
                print("You attack!\n")
                damage()
                print("The monster is defeated! you continue into the cave...")
                part3()
                goodInput = True

            elif menuInput == 2:
                print("You run\n")
                end1()
                goodInput = True

            else:
                print("Not a valid number, please try again")

        except:
            print("Please enter a number")


def newGame():

    print("Game starting.\n")
    time.sleep(1)
    print("Game starting..\n")
    time.sleep(1)
    print("Game starting...\n")
    time.sleep(1)
    print("Game starting....\n")

    print("Hello! You are an Adventurer travelling through the mountains, looking for treasure!\n"
            + "You are looking for a cave entrance, and are walking on a trail. theres a fork in the road, \n "
            "which way do you go?")

    goodInput = False
    while not goodInput:

        try:

            menuInput = int(input("1 for left \n2 for right\n"))

            if menuInput == 1:
                print("You go left")
                part2()
                goodInput = True

            elif menuInput == 2:
                print("You go right")
                end1()
                goodInput = True

            else:
                print("Not a valid number, please try again")

        except:
            print("Please enter a number")


