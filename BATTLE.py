import random
import time
import JORGEN
import os

chkCHAR=JORGEN
lifeMAX=chkCHAR.life
thisOS=os.name

def clearME():
    if(thisOS=="posix"):
        commandOS='clear'
    else:
        commandOS='cls'
    os.system(commandOS)

def makeBattle(ATT,DFF):
    #DECIDE CHAR
    if(isinstance(ATT,list)):
        opponents=ATT
        char=DFF
        for opponent in opponents:
            battleResult=haveBattle(opponent,char)
            press2continue = input(">>>PRESS ENTER TO CONTINUE")
            if(battleResult=="X"):
                char.deathText(opponent.name)
                break
            else:
                opponent.deathText()
                press2continue = input(">>>PRESS ENTER TO CONTINUE")
    else:
        char=ATT
        opponents=DFF
        for opponent in opponents:
            battleResult=haveBattle(char,opponent)
            press2continue = input(">>>PRESS ENTER TO CONTINUE")
            if(battleResult=="X"):
                char.deathText(opponent.name)
                break
            else:
                opponent.deathText()
                press2continue = input(">>>PRESS ENTER TO CONTINUE")
    return battleResult

def haveBattle(ATT,DFF):
    charDead=0
    brint=1
    while(ATT.life>0 and DFF.life>0):
        clearME()
        print('''
|#####\   /####\  |######| |######| |##|     |######|
|##   #   ##  ##  |######| |######| |##      |##
 ##   ##  ##  ##     ##       ##     ##       ##
 #####<   ######     ##       ##     ##       #####|
 #    ##  #    #     ##       ##     ##       ##
|######  |##  ##|   |##|     |##|   |##  ##| |##  ##|
|#####/  |##  ##|  |####|   |####|  |######| |######|
''')
        print(">>>>>>>>BATTLE ROUND " + str(brint) + "<<<<<<<<")
        brint=brint+1
        print(ATT.name + " HAS " + str(ATT.life) + " LIFE AND " + DFF.name + " HAS " + str(DFF.life) + " LIFE.")
        if(ATT.isChar):
            if(chkPOTION(ATT.items)):
                ATT.life=lifeMAX
                ATT.items.remove('p')
                print(ATT.name + " HAS " + str(ATT.life) + " LIFE AND " + DFF.name + " HAS " + str(DFF.life) + " LIFE.")
        else:
            if(chkPOTION(DFF.items)):
                DFF.life=lifeMAX
                DFF.items.remove('p')
                print(ATT.name + " HAS " + str(ATT.life) + " LIFE AND " + DFF.name + " HAS " + str(DFF.life) + " LIFE.")
        
        ###
        print('''
                 XXXX                  XXXX 
              XXXXXX                XXXXXX  
            XXXXXX                XXXXXX    
          XXXXXX                XXXXXX      
    XX  XXXXXX            XX  XXXXXX        
  XXXXXXXXXX            XXXXXXXXXX          
      XXXX                  XXXX            
    XX  XXXX              XX  XXXX          
  XX    XX              XX    XX            
''')
        time.sleep(2)
        #ATTACKER TURN
        print(">>>> " + ATT.name + " ATTACKS!<<<<")
        dice=random.randint(1,6)
        attResult=(ATT.att + dice)
        battleDIF=(attResult - DFF.dff)
        if(battleDIF>0):
            if(battleDIF==1):
                print(ATT.name + " lands a glancing blow!")
            elif(battleDIF==2):
                print(ATT.name + " scores a direct hit!")
            else:
                print(ATT.name + " does serious damage!")
            DFF.life-=attResult
            time.sleep(1)
            print(DFF.name + " is DEALT " + str(attResult) + " DAMAGE!")
            if(DFF.life<1):
                if(DFF.isChar):
                    charDead=1
                break
        else:
            print(DFF.name + " DEFENDS!")
        
        ###
        time.sleep(2)
        ###
        
        #DEFENDER TURN
        print('''
>>>> ''' + DFF.name + ''' ATTACKS!<<<<''')
        dice=random.randint(1,6)
        attResult=(DFF.att + dice)
        battleDIF=(attResult - ATT.dff)
        if(battleDIF>0):
            if(battleDIF==1):
                print(DFF.name + " lands a glancing blow!")
            elif(battleDIF==2):
                print(DFF.name + " scores a direct hit!")
            else:
                print(DFF.name + " does serious damage!")
            ATT.life-=attResult
            time.sleep(1)
            print(ATT.name + " is DEALT " + str(attResult) + " DAMAGE!")
            if(ATT.life<1):
                if(ATT.isChar):
                    charDead=1
                break
        else:
            print(ATT.name + " DEFENDS!")
        press2continue = input('''
>>>PRESS ENTER TO CONTINUE''')
    #END OF BATTLE
    if(charDead==1):
        return "X"
    else:
        if(ATT.isChar):
            return(ATT.life,ATT.items)
        else:
            return (DFF.life,DFF.items)

def chkPOTION(items):
    potionUsed=False
    for item in items:
        if(item=='p' and potionUsed==False):
            print("USE POTION?")
            print('''1- YES
2- NO''')
        try:
            usePotion = input('>')
            if(usePotion=="1"):
                potionUsed=True
                return True
            else:
                return False
        except NameError:
            print("YOUR INDECISION HAS COST YOU")
            return False
        except SyntaxError:
            print("YOUR FAILURE TO ACT HAS COST YOU")
            return False
    return