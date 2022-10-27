
import random

# def skillRoller():
'''
print("Rolling your skill check......")
print(random.randint(1, 20))
'''

# def damageRoller():

print("Rolling to hit......")
hit = random.randint(1, 20)
print(hit)

if hit >= 1 or hit <= 9:
    print("That's a miss!")

elif hit >= 10 or hit <= 15:
    print("That's a HIT!")
    print("Rolling Damage......")
    print(random.randint(1, 10))

elif hit >= 16 or hit <= 19:
    print("That's a hard HIT!")
    print("Rolling Damage......")
    print(random.randint(5, 15))

elif hit == 20:
    print("That's a CRITICAL HIT!")
    print("Rolling Damage......")
    print(random.randint(10, 20))

