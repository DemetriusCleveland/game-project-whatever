import random

#The grid that only shows where the character is (5x5), char is denoted by an "X"
gpsGrid=[['-','-','-','-','-'],['-','-','-','-','-'],['-','-','-','-','-'],['-','-','-','-','-'],['-','-','-','X','-']]

#prints map (doesn't change so it'll just be a print function)
def mapPrinter():
    print("_______________________________________")
    print("|Museum------T--------------Field     |")
    print("|______|___|_1_|___________|__________|")
    print("|      |   | 1 |Engineering|          |")
    print("|______|___|_1_|____1______|__________|")
    print("|      |   | L-|----+-------Sneed Hall|")
    print("|______|___|___|____1______|__________|")
    print("|      |Rec---------J      |          |")
    print("|______|___|___|____1______|__________|")
    print("|      |   |   |           |          |")
    print("|______|___|___|__Entrance_|__________|")


def gpsPrinter(list):
    # Shows location
    x = 0
    y = 0
    while y < list.len():
        y += 1
        for i in lists:
            print(i, end='\t')
        print()

# Character lists. Each character has a list of profile data as:
# [Name, description/hint, HP, baseATK, attack1Name, attack1Uses, attack1Multiplier, attack2Name, attack2Uses, attack2Multiplier, baseDEF, luck(multiplier 0->1), gold]
francis=["francis", "the hero", 100, 10, "Punch", 5, 2, "Kick", 10, 4, 50, 'luck(multiplier 0->1)', 20]
crackhead=['crackhead', 'he needs his fix', 20, 5, "Injection", 2, 4, 'Scratch', 100, 1.5, 30, 'luck(multiplier 0->1)', 5]

if  crackhead[2]<15:
    crackhead[6]=8
    print("The crackhead attackmultiplier is now 8.")
elif crackhead[2]<10:
    crackhead[6]=12
    print("")
elif crackhead[2]<5:
    crackhead[6]=16

def pickItem(item, itemList):
    '''Once an item is obtained, this function can be called to select it from a menu.'''
    itemList.append(item)
    print(item, "has been added to your inventory!")

def restartAfterDeath(answer):
    '''After the character dies, this function is called to
    ask the user if he wants to restart or quit the game.'''
    if answer=="y":
        print('Start at the beginning')
    else:
        print("Quit the game")

def checkStats(): #fix this
    [Name, description / hint, HP, baseATK, attack1Name, attack1Uses, attack1Multiplier, attack2Name, attack2Uses,
     attack2Multiplier, baseDEF, luck(multiplier 0->1), gold]
    print("Name: ", francis[0])

# attacker and defender objects are lists with their stats, preassigned from character status

# separating into two combats for attack1 and attack2
def combat1(attacker, defender):
    # check if attacker has at least 1 charge for the attack
    if (attacker[5] > 0):
        # lowers defender's hp based on attacker's base attack and particular attack multiplier minus the defender's def
        defender[2] = defender[2] - ((attacker[3] * attacker[6]) - defender[10])
        attacker[5] = attacker[5] - 1
    else:
        print("Attacker does not have any charge left for that move!")
        combat1(attacker, defender)

def combat2(attacker, defender):
    if (attacker[8] > 0):
        defender[2] = defender[2] - ((attacker[3] * attacker[9]) - defender[10])
        attacker[5] = attacker[5] - 1
        if defender[2] < 1:
            doomsday(defender)
    else:
        print("Attacker does not have any charge left for that move!")
        combat2(attacker, defender)

# doomsday() is a function that handles the procedure when a char's HP drops to zero or below zero. Luck multiplier is
# used to see if he survives with 1hp
def doomsday(attacker, defender):
    print("The defender is badly wounded and at the doors of death. In his last efforts, he hopes his luck will give him a second breath...")
    # random.randint(0,100) makes a random number including 0 to including 100. attacker/defender[11] is the luck multiplier
    deathNumA = ((random.randint(0, 100)) * attacker[11]) / 1  # "/1" to round to nearest whole number
    deathNumB = ((random.randint(0, 100)) * defender[11]) / 1
    if deathNumA > deathNumB:
        print("Battered and bruised, the defender is unable to recover before the attacker throws his killing blow.")
        print(defender[0] + " has died.")
    elif deathNumB > deathNumA:
        print("Despite all odds, a miracle of luck recovers the fallen defender, reviving him with 1HP")
        print(defender[0] + " has been revived with 1HP.")

'''Francis Magilicutty, private eye, receives a case of a missing girl said to be spotted near an 
abandoned college, Sammy Systems University. Arriving on campus, the calm, Fall climate was nothing by 
eerie. After paying the Uber driver,with no tip, he arrives on the campus "Just Talk" area (with his map and gps) and cleans up
his mess.
'''

"Make a function called map move, moves the x where its suppsed to go, and allow the user, inside the function; end of function, " \
"have a request to access a full_game function, has 25 ifs to check place at 00 is x or 01 is x, that part of story is going through" \
"with flavor text explaining what is going on and going to happen"

checkStats()

print("")
print("*This is a text-based adventure game using a grid of 'squares'. If you're ever lost, type 'help' for a list of commands*")
#we've gotta have a do while in global that just prompts the user over and over and only quits if the user enters "quit game"
#and program says "quitting will reset the game, are you sure?(y/n)" to do last check
while True:
    userInput = ""
    userInput = input("")
    if userInput == "help":
        print(" COMMAND:                       EFFECT:")
        print("'move north/south/east/west'...moves character to the square above/below/left/right of the square they're on")
        print("'map'..........................pulls up the map that shows buildings, paths, and intersections")
        print("'map info'.....................helps explain how to read map")
        print("'gps'..........................pulls up the square you are at in the college, shown as an 'X'")
        print("'[insert name] stats'..........displays known stats of person selected. unknown stats will show up as '???'")

    elif userInput == "move north" and gpsGrid[2][3]:
        #all the engineering building stuff (he enters)
