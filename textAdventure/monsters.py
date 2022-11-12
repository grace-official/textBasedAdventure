
'''
import diceRoller

class Monster:

    def __init__(self, health):
        self.health = health

    def hurt(self, damagetotal):
        print(self.health - damagetotal)

        if(self.health =< 0)
            print("The monster has been defeated")

class SmallMonster(Monster):

    def __init__(self, health):
        super().__init__(health)


monster = Monster(5)

smallMonster = SmallMonster(2)

'''
