import BATTLE
import JORGEN
import INTRO
import ROAD
import FOREST
import os


char=JORGEN
thisOS=os.name

def clearME():
    if(thisOS=="posix"):
        commandOS='clear'
    else:
        commandOS='cls'
    os.system(commandOS)

def doBattle(attacker,defender):
    newBattle=BATTLE
    resArray=newBattle.haveBattle(attacker, defender)
    if(resArray=="X"):
        return False
    else:
        char.life=resArray[0]
        char.items=resArray[1]
        return True

def gotoIntro():
    intro=INTRO
    resVar=intro.tellStory()
    if(resVar==1):
        char.legacy[0]=1
        newPath=ROAD
    else:
        char.legacy[0]=2
        newPath=FOREST
    newPath.startPath(char)
    return
        


########################################################

def playGame():
    clearME()
    print('''
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
XXXX  XXXX  XXXX  XX     X  X  XXXX   XXXX   XXXX  XXXX
X  X  X  X  X     XX     X  X  X  XX  X       XX   X  X
XXXX  XXX   XXX   XX     X  X  X   X  XXX     XX   X  X
X     X XX  X     XX  X  X  X  X   X  X       XX   X  X
X     X  X  XXXX  XXXXX  XXXX  XXXX   XXXX    XX   XXXX 

 /####\    |#   ##|    /####\    |#####\    |######|   |######|
|######|   |##  ##    |##  ##|   |##  ###   |######|   |##   #|  
 ##   #|   |### ##     ##  ##     ##  ###        ##     ##     
 ##         ######     ######     ######/       ##      ######|
 ## ###|    ######     ######     ######       ##       ##
|##  ##|    ## ###     ##  ##     ##  ##      ##        ##  
|######|    ##  ##|   |##  ##|   |##  ##|   |######|   |##  ##|
 \####/    |##   #|   |##  ##|   |##  ##|   |######|   |######|

 v1.0 - 2025
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
created by mrcrypt{
    @mrcrypt.bsky.social
    defcon.social/@mrcrypt
    mrcrypt.deviantart.com
    selfsploitationpress.net
}
important_contributions(thanks){
    dotfortun3
    dulcedemon
    collectordisorder
    geebee101010
}
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
''')
    press2continue = input(">>>PRESS ENTER TO CONTINUE")
    gotoIntro()
    return

playGame()

########################################################
