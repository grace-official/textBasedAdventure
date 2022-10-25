# Main adventure menu
from gameCreation import newGame

menuInput = int(input("Welcome to: PLACEHOLDER_NAME! please select an option below! \n "
+ "press 1 for a new game \n press 2 to load a game \n press 3 to quit"))

if menuInput == 1:
    newGame()
