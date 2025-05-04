#THE ROAD ADVENTURE PATH
import STATCHK
import BANDIT01
import BANDIT02
import BANDIT03
import BATTLE
import time
import os
import roadStory
thisOS=os.name

def clearME():
    if(thisOS=="posix"):
        commandOS='clear'
    else:
        commandOS='cls'
    os.system(commandOS)

#DO BATTLE
def doBattle(attacker,defender):
    newBattle=BATTLE
    resArray=newBattle.makeBattle(attacker, defender)
    if(resArray=="X"):
        return False
    else:
        return resArray
    
#START PATH
def startPath(character):
    char=character
    gotoROAD1(char)
    return

#GOTO ROAD 1
def gotoROAD1(character):
    char=character
    showStory(1)
    #MAKE CHOICE
    choiceMade=False
    while(choiceMade==False):
        
        print("WHAT DO YOU DO?")
        print('''1- OBSERVE THE TRAVELER
2- TALK TO THE TRAVELER
3- IGNORE THE TRAVELER''')
        try:
            makeChoice = input('>')
            if(makeChoice=="1"):
                choiceMade=True
                statCheck=STATCHK
                if(statCheck.checkSTAT(char.prr,2)==True):
                    showStory(2)
                    char.legacy[1]=1
                    char.items.append('p')
                else:
                    showStory(3)
                    char.legacy[1]=1
            elif(makeChoice=="2"):
                choiceMade=True
                showStory(3)
                char.legacy[1]=1
            elif(makeChoice=="3"):
                choiceMade=True
                showStory(4)
                char.legacy[1]=2
            else:
                print("not a choice")
                time.sleep(2)
            gotoROAD2(char)
        except NameError:
            print("not a choice")
            time.sleep(2)
        except SyntaxError:
            print("not a choice")
            time.sleep(2)
    return

#GOTO ROAD 2
def gotoROAD2(character):
    char=character
    lifeMAX=char.life
    statCheck=STATCHK
    if(char.legacy[1]==1):
        showStory(5)
        choiceMade=False
        while(choiceMade==False):
                
                print("WHAT DO YOU DO?")
                print('''1- HELP COUNCILMAN GORFE AND HIS COACHMAN
2- REMAIN HIDDEN''')
                try:
                        makeChoice = input('>')
                        if(makeChoice=="1"):
                                bandits=[BANDIT01,BANDIT02]
                                choiceMade=True
                                if(statCheck.checkSTAT(char.dxx,2)==True):
                                        showStory(6)
                                        battleRES=doBattle(char,bandits)
                                        if(battleRES is not False):
                                                char.life=battleRES[0]
                                                char.items=battleRES[1]
                                                print("YOU'VE DEFEATED THE BANDITS!")
                                                press2continue = input(">>>PRESS ENTER TO CONTINUE")
                                                winBattle(char,lifeMAX)
                                else:
                                        showStory(7)
                                        battleRES=doBattle(bandits,char)
                                        if(battleRES is not False):
                                                char.life=battleRES[0]
                                                char.items=battleRES[1]
                                                print("YOU'VE DEFEATED THE BANDITS!")
                                                press2continue = input(">>>PRESS ENTER TO CONTINUE")
                                                winBattle(char,lifeMAX)
                        elif(makeChoice=="2"):
                                if(statCheck.checkSTAT(char.dxx,2)==True):
                                     showStory(8)
                                     char.legacy[2]=2
                                     gotoROAD3(char)
                                else:
                                     showStory(9)
                                     bandits=[BANDIT01,BANDIT02]
                                     battleRES=doBattle(bandits,char)
                                     if(battleRES is not False):
                                        char.life=battleRES[0]
                                        char.items=battleRES[1]
                                        print("YOU'VE DEFEATED THE BANDITS!")
                                        press2continue = input(">>>PRESS ENTER TO CONTINUE")
                                        winBattle(char,lifeMAX)
                                choiceMade=True
                        else:
                                print("not a choice")
                                time.sleep(2)
                except NameError:
                        print("not a choice")
                        time.sleep(2)
                except SyntaxError:
                        print("not a choice")
                        time.sleep(2)
    elif(char.legacy[1]==2):
         showStory(10)
         choiceMade=False
         while(choiceMade==False):
                
                print("WHAT DO YOU DO?")
                print('''1- GET THE BANDITS' ATTENTION
2- HELP COUNCILMAN GORFE AND HIS COACHMAN''')
                try:
                        makeChoice = input('>')
                        if(makeChoice=="1"):
                                choiceMade=True
                                showStory(11)
                                bandits=[BANDIT01,BANDIT02]
                                clearME()
                                battleRES=doBattle(char,bandits)
                                if(battleRES is not False):
                                        char.life=battleRES[0]
                                        char.items=battleRES[1]
                                        print("YOU'VE DEFEATED THE BANDITS!")
                                        press2continue = input(">>>PRESS ENTER TO CONTINUE")
                                        winBattle(char,lifeMAX)
                        elif(makeChoice=="2"):
                                choiceMade=True
                                showStory(12)
                                bandits=[BANDIT01,BANDIT02,BANDIT03]
                                battleRES=doBattle(bandits,char)
                                if(battleRES is not False):
                                        char.life=battleRES[0]
                                        char.items=battleRES[1]
                                        print("YOU'VE DEFEATED THE BANDITS!")
                                        press2continue = input(">>>PRESS ENTER TO CONTINUE")
                                        winBattle(char,lifeMAX)
                        else:
                                print("not a choice")
                                time.sleep(2)
                except NameError:
                        print("not a choice")
                        time.sleep(2)
                except SyntaxError:
                        print("not a choice")
                        time.sleep(2)
    return


#WIN BATTLE
def winBattle(character,lifeMAX):
     char=character
     half=(lifeMAX/2)
     if(char.life >= half):
          showStory(14)
          char.legacy[2]=3
     else:
          showStory(13)
          char.legacy[2]=1
     gotoROAD3(char)
     return

#GOTO ROAD 3
def gotoROAD3(char):
     if(char.legacy[2]==1):
          showStory(17)
     elif(char.legacy[2]==2):
          showStory(15)
     elif(char.legacy[2]==3):
          showStory(16)
     else:
          print("THERE'S AN ISSUE AT THE END")
     return

#SHOW STORY
def showStory(part):
    story=roadStory
    story.showStory(part)
    return