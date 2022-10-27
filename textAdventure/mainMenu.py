# Main adventure menu
from gameCreation import newGame
from saveData import loadGame

validInput = False

while not validInput:
    menuInput = int(input("Welcome to: PLACEHOLDER_NAME! please select an option below! \n "
    + "press 1 for a new game \n press 2 to load a game \n press 3 to quit"))

    if menuInput == 1:
        newGame()
        validInput = True

    elif menuInput == 2:
        loadGame()
        validInput = True

    elif menuInput == 3:
        print("See you later!")
        validInput = True

    else:
        print("That is not an option, please try again.")
