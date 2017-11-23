'''Francis Magilicutty, private eye, receives a case of a missing girl said to be spotted near an 
abandoned college, Sammy Systems University. Arriving on campus, the calm, Fall climate was nothing by 
eerie. After paying the Uber driver,with no tip, he arrives on the campus "Just Talk" area and cleans up
his mess.
'''
#for now, we'll make character stat distribution in list as follows:
#[Name, description/hint, HP, baseATK, attack1Name, attack1Uses, attack1Multiplier, attack2Name, attack2Uses, attack2Multiplier, baseDEF, dropID(int that determine's type of loot awarded on death)
#attacker and defender objects are lists with their stats, preassigned from character status


#separating into two combats for attack1 and attack2
def combat1(attacker, defender):
#check if attacker has at least 1 charge for the attack
    if(attacker[5] > 0):
#lowers defender's hp based on attacker's base attack and particular attack multiplier minus the defender's def
        defender[2]= defender[2]-((attacker[3]*attacker[6])-defender[10])
        attacker[5] = attacker[5]-1
    else:
        print("Attacker does not have any charge left for that move!")

def combat2(attacker, defender):
    
