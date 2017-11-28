def grid_maker(h, w):
    '''This function is called make a map.'''
    grid = [["-" for i in range(w)] for i in range(h)]
    grid[0][0] = "o"
    return grid

def print_grid(grid):
    """To display the map"""
    for row in grid:
        for e in row:
            print(e)
        print

def pickItem(item, itemList):
    '''Once an item is obtained, this function can be called to select it from a menu.'''
    itemList.append(item)
    print(item, "has been added to your inventory!")
    #return 0

def restartAfterDeath(answer):
    '''After the character dies, this function is called to
    ask the user if he wants to restart or quit the game.'''
    if answer=="y":
        print('Start at the beginning')
    else:
        print("Quit the game")
    #return 0

def checkStats():
    return 0

francis=["francis"]
items=[]#At the start, the item is empty
enemy1=["enemy1"]
'''Francis Magilicutty, private eye, receives a case of a missing girl said to be spotted near an 
abandoned college, Sammy Systems University. Arriving on campus, the calm, Fall climate was nothing by 
eerie. After paying the Uber driver,with no tip, he arrives on the campus "Just Talk" area and cleans up
his mess.
'''

