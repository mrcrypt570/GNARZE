#BEGIN THE ADVENTURE HERE
import time
import os

thisOS=os.name

def clearME():
    if(thisOS=="posix"):
        commandOS='clear'
    else:
        commandOS='cls'
    os.system(commandOS)

def tellStory():    
    clearME()
    print('''++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
A secluded mountain village, a properous people, a warm hearth - everything
taken from you when the Bandits invaded your home. With your small family
and most of your neighbors slain, it's up to you, Jorgen Wolfwinter, to use
your formidable warrior skills to earn money to rebuild.

You pack some food and gold, don your armor, put your shieled on your back,
and take up your sword to travel to the capital city of Gnarze to bring
fortune and glory back to your village.

You leave your cabin and wolk down the path out of the village and consider
which way to the city would be best. You're familiar enough with the FOREST
paths to make the trip in good time. The ROAD could be safer with all of
the people who use it.
''')
    choiceMade=False
    while(choiceMade==False):
        print("WHICH DO YOU CHOOSE?")
        print('''1- TRAVEL THE ROAD
2- TAKE THE FOREST PATHS''')
        try:
            makeChoice = input('>')
            if(makeChoice=="1"):
                choiceMade=True
                return 1
            elif(makeChoice=="2"):
                choiceMade=True
                return 2
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