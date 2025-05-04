#THE FOREST ADVENTURE PATH
import STATCHK
import HUNTER
import WOLF
import BATTLE
import time
import os
import forestStory
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
    wolf=[WOLF]
    clearME()
    showStory(1)
    choiceMade=False
    while(choiceMade==False):
        print("HOW DO YOU PROCEED?")
        print('''1- WITH CAUTION
2- WITH CONFIDENCE''')
        try:
            makeChoice = input('>')
            if(makeChoice=="1"):
                choiceMade=True
                gotoWolf(1,char,wolf)
            elif(makeChoice=="2"):
                choiceMade=True
                gotoWolf(2,char,wolf)
            else:
                print("not a choice")
                time.sleep(1)
        except NameError:
            print("not a choice")
            time.sleep(1)
        except SyntaxError:
            print("not a choice")
            time.sleep(1)
    return

#WOLF
def gotoWolf(selection,character,encounter):
    char=character
    wolf=encounter
    statCheck=STATCHK
    clearME()
    if(statCheck.checkSTAT(char.prr,1)==True and selection==1):
        showStory(2)
        press2continue = input(">>>PRESS ENTER TO CONTINUE")
        battleRES=doBattle(char,wolf)
        if(battleRES is not False):
            char.life=battleRES[0]
            char.items=battleRES[1]
            gotoFOREST2(char)
    else:
        showStory(3)
        press2continue = input(">>>PRESS ENTER TO CONTINUE")
        #BATTLE - WOLF GOES FIRST
        battleRES=doBattle(wolf,char)
        if(battleRES is not False):
            char.life=battleRES[0]
            char.items=battleRES[1]
            gotoFOREST2(char)
    return

#FOREST 2      
def gotoFOREST2(character):
    char=character
    hunter=[HUNTER]
    clearME()
    showStory(4)
    choiceMade=False
    while(choiceMade==False):
        print("HOW DO YOU PROCEED?")
        print('''1- LOOK AROUND FOR THE HUNTER
2- APPROACH THE CABIN''')
        try:
            makeChoice = input('>')
            if(makeChoice=="1"):
                choiceMade=True
                gotoHunter(char,hunter)
            elif(makeChoice=="2"):
                choiceMade=True
                gotoCabin(char,hunter)
            else:
                print("not a choice")
                time.sleep(1)
        except NameError:
            print("not a choice")
            time.sleep(1)
        except SyntaxError:
            print("not a choice")
            time.sleep(1)
    return

#HUNTER
def gotoHunter(character,encounter):
    char=character
    hunter=encounter
    statCheck=STATCHK
    clearME()
    if(statCheck.checkSTAT(char.prr,2)==True):
        showStory(5)
        choiceMade=False
        while(choiceMade==False):
            print("HOW DO YOU PROCEED?")
            print('''1- RESPECT
2- ATTACK''')
            try:
                makeChoice = input('>')
                if(makeChoice=="1"):
                    choiceMade=True
                    showStory(6)
                    char.legacy[1]=1
                    gotoFOREST3(char)
                elif(makeChoice=="2"):
                    choiceMade=True
                    print('''++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
You slip the dagger from your boot, spin and hurl it exactly where the
person in the tree would be were they still there. You look down to see them
racing toward you. In one motion, your sword unsheathes as you sling your
shield off your back and onto your arm.
''')
                    if(statCheck.checkSTAT(char.dxx,3)==True):
                        battleRES=doBattle(char,hunter)
                        if(battleRES is not False):
                            char.life=battleRES[0]
                            char.items=battleRES[1]
                            print("")
                            choiceMade=False
                            while(choiceMade==False):
                                print("WHICH DO YOU CHOOSE?")
                                print('''1- CONTINUE TO THE CABIN
2- CONTINUE TO THE GATES OF GNARZE''')
                                try:
                                    makeChoice = input('>')
                                    if(makeChoice=="1"):
                                        choiceMade=True
                                        gotoCabin(char,hunter)
                                    elif(makeChoice=="2"):
                                        choiceMade=True
                                        gotoFOREST3(char)
                                    else:
                                        print("not a choice")
                                        time.sleep(2)
                                except NameError:
                                    print("not a choice")
                                    time.sleep(2)
                                except SyntaxError:
                                    print("not a choice")
                                    time.sleep(2)
                        else:
                            print("YOU DIED")
                    else:
                        battleRES=doBattle(hunter,char)
                        if(battleRES is not False):
                            char.life=battleRES[0]
                            char.items=battleRES[1]
                            press2continue = input(">>>PRESS ENTER TO CONTINUE")
                            choiceMade=False
                            while(choiceMade==False):
                                print("WHICH DO YOU CHOOSE?")
                                print('''1- CONTINUE TO THE CABIN
2- CONTINUE TO THE GATES OF GNARZE''')
                                try:
                                    makeChoice = input('>')
                                    if(makeChoice=="1"):
                                        choiceMade=True
                                        gotoCabin(char,hunter)
                                    elif(makeChoice=="2"):
                                        choiceMade=True
                                        gotoFOREST3(char)
                                    else:
                                        print("not a choice")
                                        time.sleep(2)
                                except NameError:
                                    print("not a choice")
                                    time.sleep(2)
                                except SyntaxError:
                                    print("not a choice")
                                    time.sleep(2)
                else:
                    print("not a choice")
                    time.sleep(1)
            except NameError:
                print("not a choice")
                time.sleep(1)
            except SyntaxError:
                print("not a choice")
                time.sleep(1)
    else:
        print('''++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Quick but thorough scans to the left and right reveal nothing.
"Couldn't hurt to look around," you think to yourself and move out from your
cover to the cabin.
        
''')
        press2continue = input(">>>PRESS ENTER TO CONTINUE")
        gotoCabin(char,hunter)
    return

#CABIN
def gotoCabin(character,encounter):
    print("CABIN")
    char=character
    hunter=encounter
    clearME()
    if(hunter[0].life<1):
        print('''++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
You approach the Cabin cautiously even though you're certain no one else is
there. The fire had died down, but there was still meat set to cook. You
approach the Cabin door. It's locked.

Patting down your pockets and searching your pouches, you slowly realize
your lock picks are missing. The battle dislodged them from your pocket,
giving the Hunter one final blow from beyond the grave.
''')
        choiceMade=False
        while(choiceMade==False):
            print("WHICH DO YOU CHOOSE?")
            print('''1- BASH THE DOOR
2- MOVE ON''')
            try:
                makeChoice = input('>')
                if(makeChoice=="1"):
                    choiceMade=True
                    statCheck=STATCHK
                    if(statCheck.checkSTAT(char.dxx,2)==True):
                        showStory(7)
                        char.legacy[1]=2
                        gotoFOREST3(char)
                    else:
                        showStory(8)
                        char.legacy[1]=3
                        gotoFOREST3(char)
                elif(makeChoice=="2"):
                    choiceMade=True
                    print('''++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
You pause briefly to take in the tranquil, rustic comfort the Hunter
afforded himself before quenching quenching the fire and grabbing one of the
cooking skewers.

"Only one waste today," you say remorsefully and continue on toward
the gates of Gnarze.
''')
                    char.legacy[1]=3
                    gotoFOREST3(char)
                else:
                    print("not a choice")
                    time.sleep(2)
            except NameError:
                print("not a choice")
                time.sleep(2)
            except SyntaxError:
                print("not a choice")
                time.sleep(2)
    else:
        print('''++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Having only heard rumors about the Hunter's temperament, you move cautiously.
The fire is low and there are five cooked meat skewers stuck in the ground
around it on one side. You approach the Cabin door. It's locked.
''')
        choiceMade=False
        while(choiceMade==False):
            print("WHAT DO YOU DO?")
            print('''1- PICK THE LOCK
2- BASH IT DOWN
3- OBSERVE THE AREA''')
            try:
                makeChoice = input('>')
                if(makeChoice=="1"):
                    gotoPick(char,hunter)
                    choiceMade=True
                elif(makeChoice=="2"):
                    gotoBash(char,hunter)
                    choiceMade=True
                elif(makeChoice=="3"):
                    gotoObserve(char)
                    choiceMade=True
                else:
                    print("not a choice")
                    time.sleep(2)
            except NameError:
                print("errnot a choice")
                time.sleep(2)
            except SyntaxError:
                print("rrenot a choice")
                time.sleep(2)
    return

#GOTO PICK
def gotoPick(character,encounter):
    char=character
    hunter=encounter
    clearME()
    print('''++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
You examine the lock - not very complicated. You unsnap a concealed pocket
and produce some wire lock picks just then you hear someone behind you
clearing their throat.

"Care to explain why you're picking my lock?" the Hunter asks.
''')
    choiceMade=False
    while(choiceMade==False):
        print("HOW DO YOU REACT?")
        print('''1- HANDS UP
2- ATTACK''')
        try:
            makeChoice = input('>')
            if(makeChoice=="1"):
                showStory(9)
                char.legacy[1]=3
                choiceMade=True
                gotoFOREST3(char)
            elif(makeChoice=="2"):
                clearME()
                print('''++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Out of pure instinct you spin away from picking the lock and whip your
dagger right where your expert skills tell you the voice behind you was coming
from. You see, however, your dagger fly back into the bushes while the Hunter
dodges.
''')
                press2continue = input(">>>PRESS ENTER TO CONTINUE")
                battleRES=doBattle(char,hunter)
                if(battleRES is not False):
                    char.life=battleRES[0]
                    char.items=battleRES[1]
                    choiceMade2=False
                    clearME()
                    print('''++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
You search for your lock picks after the fight, but they were batted too far
away for you to find.
''')
                    while(choiceMade2==False):
                        print("WHAT DO YOU WANT TO DO?")
                        print('''1- BASH THE DOOR DOWN
2- MOVE ON''')
                        try:
                            statCheck=STATCHK
                            makeChoice = input('>')
                            if(makeChoice=="1"):
                                choiceMade2=True
                                if(statCheck.checkSTAT(char.dxx,2)==True):
                                    showStory(10)
                                    char.legacy[1]=2
                                    gotoFOREST3(char)
                                else:
                                    showStory(11)
                                    char.legacy[1]=3
                                    gotoFOREST3(char)
                            elif(makeChoice=="2"):
                                print('''You grab one of the cooked meat skewers.
"Only one waste today." you say remorsefully and
continue to the gates of Gnarze.
''')
                                char.legacy[1]=3
                                choiceMade2=True
                                gotoFOREST3(char)
                            else:
                                print("not a choice")
                                time.sleep(2)
                        except NameError:
                            print("not a choice")
                            time.sleep(2)
                        except SyntaxError:
                            print("not a choice")
                            time.sleep(2)
                else:
                    print("YOU DIED")
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
    return

#GOTO BASH
def gotoBash(character,encounter):
    char=character
    hunter=encounter
    statCheck=STATCHK
    clearME()
    if(statCheck.checkSTAT(char.dxx,2)==True):
        print('''++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
You slip your shield onto your arm and use it to bash the door down. It was
lighter than you'd expected, so with little effort it gives way and breaks
some more when it hits the floor.

You're suddenly aware of someone running toward you. You hear them yelling
as you quickly turn, drawing your sword. The Hunter charges into your attack.
''')
        press2continue = input(">>>PRESS ENTER TO CONTINUE")
        battleRES=doBattle(char,hunter)
        if(battleRES is not False):
            char.life=battleRES[0]
            char.items=battleRES[1]
            clearME()

            print('''A quick scan of the Cabin turned into more than a few minutes
of looking through the possessions of their former owner. Some supplies you
already had, a dagger to replace the one you lost in the fight, but no real
riches. On your way out, you quench the fire and grab one of the cooked meat
skewers.

"Only one waste today," you say remorsefully and continue to
the gates of Gnarze.
''')
            char.legacy[1]=3
            press2continue = input(">>>PRESS ENTER TO CONTINUE")
            gotoFOREST3(char)
        else:
            print("YOU DIED")
    else:
        print('''++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
You slip your shield onto your arm and put your weight behind it as you bash
the door down. It was lighter than you'd expected, though, so you stumble in
and trip over a bench, landing awkwardly on what's left of the Cabin door.

You barely have a moment to regain your feet when a small knife flies into
the Cabin at you, nearly hitting you in the eye. The Hunter rushes in right
behind it.You manage to get your shield in place on your arm before the
Hunter makes his first attack.
''')
        press2continue = input(">>>PRESS ENTER TO CONTINUE")
        battleRES=doBattle(hunter,char)
        if(battleRES is not False):
            char.life=battleRES[0]
            char.items=battleRES[1]
            clearME()            
            print('''A quick scan of the Cabin turned into more than a few minutes
of looking through the possessions of their former owner. Some supplies you
already had, a dagger to replace the one you lost in the fight, but no real
riches. On your way out, you quench the fire and grab one of the cooked meat
skewers.

"Only one waste today," you say remorsefully and continue to the gates of Gnarze.
''')
            char.legacy[1]=3
            press2continue = input(">>>PRESS ENTER TO CONTINUE")
            gotoFOREST3(char)
        else:
            print("YOU DIED")
    return
                                      
#GOTO OBSERVE
def gotoObserve(character):
    char=character
    clearME()
    showStory(12)
    char.legacy[1]=1
    gotoFOREST3(char)
    return

#FOREST 3
def gotoFOREST3(character):
    char=character
    clearME()
    if(char.legacy[1]==1):
        showStory(13)
    elif(char.legacy[1]==2):
        showStory(14)
    else:
        showStory(15)
    return

#SHOW STORY
def showStory(part):
    story=forestStory
    story.showStory(part)
    return