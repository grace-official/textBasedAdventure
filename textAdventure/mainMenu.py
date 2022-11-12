# Main adventure menu
# from gameCreation import newGame
from saveData import loadGame


menuInput = int(input("Welcome to: PLACEHOLDER_NAME! please select an option below! \n "
+ "press 1 for a new game \n press 2 to load a game \n press 3 to quit\n"))

if menuInput <= 0 or menuInput >= 4:
    print("Not a valid input, please try again!")

elif menuInput == 1:
    print("e")

elif menuInput == 2:
    loadGame()

elif menuInput == 3:
    print("Bye!")
    exit()


validInput = False

while not validInput:

    try:
        menuInput = int(input("Welcome to: PLACEHOLDER_NAME! please select an option below! \n "
        + "press 1 for a new game \n press 2 to quit\n"))

        if menuInput == 1:
            # newGame()
            validInput = True

        elif menuInput == 2:
            print("See you later!")
            validInput = True

        else:
            print("That is not an option, please try again.\n")
    except:
        print("Please Enter a number\n")

