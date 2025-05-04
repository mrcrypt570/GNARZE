legacy=[0,0,0]
name="Jorgen"
isChar=True
life=35
att=5
dff=7
dxx=6
prr=5
items=[]

def deathText(selection):
    print('''
   |XXXXXXXX|      |XXXXXXXX|      |XXXXXXXX|      |XXXXXXXX|   
  |XXXXXXXXXX|    |XXXXXXXXXX|    |XXXXXXXXXX|    |XXXXXXXXXX|  
  |X   XX   X|    |X   XX   X|    |X   XX   X|    |X   XX   X|  
   XXXX  XXXX      XXXX  XXXX      XXXX  XXXX      XXXX  XXXX   
   |XXXXXXXX|      |XXXXXXXX|      |XXXXXXXX|      |XXXXXXXX|   
    XX XX XX        XX XX XX        XX XX XX        XX XX XX    
''')
    if(selection=="The Wolf"):
        print('''
The Wolf's powerful jaws clamp down hard around your neck.
You react too late and only begin to escape. You fall backward,
blood gushing. Then a second wolf joins the first.

You've been defeated.

>THANKS FOR PLAYING!!!
''')
        return
    elif(selection=="Bandit Leader"):
        print('''
The Bandit Leader dodges your blow. The momentum of your attack
carries you right into his lunging counter-attack, piercing your body.
You collapse in a pool of your own blood.

You've been defeated.

>THANKS FOR PLAYING!!!
''')
        return
    elif(selection=="Bandit 02"):
        print('''
The second Bandit parries your strike and ripostes! His blade slips
squarely between your eyes, exiting through the back of your head.

You've been defeated.

>THANKS FOR PLAYING!!!
''')
        return
    elif(selection=="Bandit 03"):
        print('''
You charge the final Bandit, but he blocks. Braced for your attack,
he shoves you back and you lose your footing. Your head cracks off a
rock when you land, breaking your neck.

You've been defeated.

>THANKS FOR PLAYING!!!
''')
        return
    else:
        print('''
The Hunter finally charges you, feints to stab at you, but stops and
plants his boot square into your chest. As you stumble backward, he
continues his assault. You smack into a tree and that stunned moment
gives the Hunter the opportunity to bury his short sword in your chest.

You've been defeated.

>THANKS FOR PLAYING!!!
''')
        return
