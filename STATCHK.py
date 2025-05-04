#CALCULATE THE SUCCESS OR FAILURE OF A STATISTIC CHECK
import random

def checkSTAT(stat,mod):
    dice=random.randint(1, 6) #dice roll for modifier
    checkResult=(dice + mod) #add dice roll to mod
    #print(str(stat) + "    " + str(dice) + "    " + str(checkResult))
    if(checkResult<=stat):
        return True
    else:
        return False
    
#if the value of checkResult is less than or equal to the stat, the check succeeds
#use mod as a difficulty level