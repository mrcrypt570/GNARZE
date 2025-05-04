import os
thisOS=os.name

def clearME():
    if(thisOS=="posix"):
        commandOS='clear'
    else:
        commandOS='cls'
    os.system(commandOS)

def showStory(part):
    clearME()
    if(part==1):
        print('''++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
The road, so far, is an easy trip. There haven't seen many people and the
wildlife isn't giving up any hints of anyone hidden off in the woods.
Most of the day goes by before you start to hear the first cart approaching.
A small canopied cart drawn by a single horse, driven by an overweight older
fellow with a straw hat and colorful, tattered clothing.
''')
    elif(part==2):
        print('''++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
The vibe you picked up even before you saw the traveler proved true.
The gate he allowed his horse, and his manner - a confidence born from
experience - clued you in immediately to the boon that might be offered in
befriending this goodly man.

"Ahoy, gentle traveler!" you greet him, as if he were an old friend.
"How goes the road ahead?"

Whatever doubt about this encounter evaporated by his jolly, instantaneous
laughter.

"Ahoy yourself, friend! It's been a decent trip! Thank you for asking."

You both slow and stop within a comfortable distance from one another.

You begin, "Good to hear! I've come from the Winter Village. If you have
wares to sell, you'll find business there. We were attacked by bandits not
too long ago, causing much hardship."

"Now that you mention it," he says, pausing briefly after you'd spoken,
"there are some folks you may want to avoid up the road. Not that you
couldn't take care of them if they turn out to be a hassle."

You realize that you, too, were being measured on your approach.
''')
        press2continue = input(">>>PRESS ENTER TO CONTINUE")
        clearME()
        print('''++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
"There are only three," he continues. "But, if avoiding hassle is what
you're after, you could pull it off with them."
He shakes his head and rolls his eyes, indicating the people he talks about
aren't too bright.

"Either way, take this." He reaches into a satchel set beside him and
produces a brown glass bottle, then tosses it to you. You catch it,
immediately recognizing it's a HEALING POTION.

You're stunned - surprised. You begin to thank him, but he waves you off.
"It's free of charge. I do, in fact, have quite a few supplies your
kinfolk could probably use. I'll make that my next destination."

"Thank you! Tell them Jorgen said to give you shelter."

"I will."

You reach up and clasp arms in farewell, then each of you continue on in your
own directions.
''')
        press2continue = input(">>>PRESS ENTER TO CONTINUE")
    elif(part==3):
        print('''++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Driving the cart at a steady pace, the man seems like he pays attention
enough to hold his own in the Great Wood.

"Ahoy, traveler! How goes the journey?" you greet him. He slows down a
little and pauses to gauge you.

"Ahoy yourself! The journey goes well enough, but there might be some
trouble up ahead," he replies bluntly.

"Oh! Thanks for the warning." You thought perhaps you'd offended him, or
perhaps his experience with them didn't go well. "I'll do my best."

The traveler pauses.

"I'm sure you will," he smiles, then prods his horse forward down the road.
''')
        press2continue = input(">>>PRESS ENTER TO CONTINUE")
    elif(part==4):
        print('''++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Although the driver looks friendly, even smiling at you in passing, you
don't have time for even the quickest conversation. Your people need you,
and nothing will stop you bringing home supplies - and honor!
''')
        press2continue = input(">>>PRESS ENTER TO CONTINUE")
    elif(part==5):
        print('''++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Maybe only a few minutes pass before you start hearing more human-like
noises: fearful whimpering, metal clanging off wood, raised voices. You slow
your pace a bit and slink through the wood bordering the road. Your warrior
skills hunting in the forest lend you cover as you press on enough for the
scene to come into view.

These are the three Bandits that the Traveler had mentioned. They seem to
have waylaid the horse-drawn coach of a wealthy man. Both the man and his
Coachman are kneeling straight up with their hands behind their heads.

"You're not telling me what I want to hear, Councilman Gorfe!" the lead
Bandit threateningly holding the tip of his sword to the neck of the Councilman.

"I'm not carrying any gold, fool brigand! My business," Gorfe grimaces as
the sword tip press slightly more into the underside of his chin, "isn't
coin, but in favor."

Gorfe and his Coachman appear to be capable fighters, judging by their
weaponry and attitude given their disposition. The Bandits aren't well
armored, but you guess they're skilled rogues since they were able to get
the drop on the other two.
''')
        press2continue = input(">>>PRESS ENTER TO CONTINUE")
    elif(part==6):
        print('''++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
You instinctively slip your dagger from its sheath in your boot. Realizing
quickly that the Bandits are going to kill these people no matter what, you
expertly hurl the dagger straight into the neck of the Bandit closest to the
hostages.
''')
        press2continue = input(">>>PRESS ENTER TO CONTINUE")
    elif(part==7):
        print('''++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
You instinctively slip the dagger from its sheath in your boot.
Realizing quickly that the Bandits are going to kill these people no matter
what, you expertly hurl the dagger which just misses the head of the Bandit
closest to the hostages. Alerted to your presence, the three Bandits turn to
find you. This gives the Coachman a chance to produce a hidden dagger of his
own and kill the very same Bandit you missed.
''')
        press2continue = input(">>>PRESS ENTER TO CONTINUE")
    elif(part==8):
        print('''++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
You feel a bit outnumbered and decide to stay hidden. Although you'd rather
not watch something like this go down, there's no way you can leave undiscovered.

"That's it!" the Bandit leader decides, and thrusts his sword through the
neck of the Councilman.

The Coachman, who had produced a dagger from his sleeve, barely gets up
before the others cut him down, too. It was a vicious scene.

After ransacking the coach, the Bandits make their way down the road towards
the city of Gnarze. You breathe a sigh of relief that you weren't found.
''')
        press2continue = input(">>>PRESS ENTER TO CONTINUE")
    elif(part==9):
        print('''++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
You feel a bit outnumbered and decide to stay hidden. Although you'd rather
not watch something like this go down, there's no way you can leave
undiscovered. You twitch reflexively, though, snapping some twigs near your
back foot and draw the attention of the Bandits.

"Looks like we got a spy, boys!" the Bandit leader proclaims. Suddenly you
all hear the scream of the Bandit nearest the hostages as the Coachman
buries a dagger in the side of his head.
''')
        press2continue = input(">>>PRESS ENTER TO CONTINUE")
    elif(part==10):
        print('''++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Maybe only a few minutes pass before you start hearing haughty laughter just
up the road. Around the next bend, however, you discover a more serious scene:
three Bandits have waylaid a wealthy gentleman and his Coachman, both
kneeling with their hands behind their heads.

"You're not telling me what I want to hear, Councilman Gorfe!" the lead
Bandit threateningly holds the tip of his sword to the neck of the Councilman. 

"I'm not carrying any gold, fool brigand! My business," Gorfe grimaces as
the sword tip press slightly more into the underside of his chin, "isn't
coin, but in favor."

Gorfe and his Coachman appear to be capable fighters, judging by their
weaponry and attitude given their disposition. The Bandits aren't well
armored, but you guess they're skilled rogues since they were able to get
the drop on the other two. 
''')
        press2continue = input(">>>PRESS ENTER TO CONTINUE")
    elif(part==11):
        print('''++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
"Hey, assholes!" you yell, drawing your sword and readying your shield.
The Bandits turn to find you, which gives the Coachman the opportunity to
produce a dagger from his sleeve and bury it in the head of the Bandit
closest to him. Caught completely off guard, the remaining Bandits attack!
''')
        press2continue = input(">>>PRESS ENTER TO CONTINUE")
    elif(part==12):
        print('''++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
All the memories of the battle with the Bandits who attacked your village
come flooding back.

"No!" you growl. Sword drawn and shield at the ready, you charge the scene!
''')
        press2continue = input(">>>PRESS ENTER TO CONTINUE")
    elif(part==13):
        print('''++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Wiping the blood from your sword on the lead Bandit's cloak, you hear the
Coachman run to Councilman Gorfe.

"I'm fine," Gorfe reassures his friend, helping him up. "Indeed, traveler,
you arrived just in time!"

Gorfe sheaths his sword and dusts himself off while the Coachman checks on
the horses.

"And though I'm terribly grateful for your assistance in a situation that
would surely have been my end," Gorfe laughs,"I honestly have no gold with
which to reward you."

The Coachman now approaches with a satchel he got from somewhere tucked
within the carriage. He hands the satchel to the Councilman who reaches in,
then hands you a fancy bottle.

A HEALING POTION.

"Well, this will certainly help," you inform him. "Paid in full! Thank you!"

"We should be fine enough for a while, traveler. The gates to the city of
Gnarze are just a mile or so ahead. Please tell the guards of the Bandits,"
Gorfe requests. "They'll send out patrols."

You part ways with the Councilman and continue toward the city.
''')
        press2continue = input(">>>PRESS ENTER TO CONTINUE")
    elif(part==14):
        print('''++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Wiping the blood from your sword on the lead Bandit's cloak, you hear the
Coachman run to Councilman Gorfe. "I'm fine," Gorfe reassures his friend,
helping him up. "Indeed, traveler, you arrived just in time!"

Gorfe sheaths his sword and dusts himself off while the Coachman checks on
the horses. He introduces himself, "I am Councilman Arturo Gorfe and this
is my Coachman, August. Who might you be?"

"Jorgen Wolfwinter of the Winter Village. I'm traveling to the city of
Gnarze to earn some fortune for me and my people."

"Well, Jorgen," the Councilman turns toward August who has brought a
satchel from somewhere tucked within the carriage, "I believe I can help
you with that."

Gorfe takes the satchel, reaches in and takes out an ornate metal rod.
"Since you've proven your prowess and courage to me this day, I'd like to
hire you as part of my company. Evidently, I could use a bit more muscle."

"Take this," he hands you the rod. "It's the Signet of the Council. Show
this to the guards at the gates of Gnarze, and they will let you in. Find
your lodging and meet us at the Council Chamber tomorrow."

You begin to protest leaving them, but Gorfe interrupts. "Go," he says,
smiling. "We can make it ourselves, thanks to you. It's going to be a while
before the horses calm enough to continue at a proper pace. The guards will
send a patrol."

You bid them farewell with a solid clasp of hands, then make your way toward
the city.
''')
        press2continue = input(">>>PRESS ENTER TO CONTINUE")
    elif(part==15):
        print('''++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
It was nearly dusk before you crested the last hill and made your way down
the switchback road into a fortified ravine, bisected by an immense wall
built into its sides. Built into the wall, the famed gates of Gnarze stood.
You take in the beauty of the city guard lighting torches across the top of
the wall in the evening light.

The day could not be more beautiful, but the guards still seem to be a bit
uneasy. One is staring you down well, with the other two whispering in his
ear.

"Good evening, gentlemen," you greet them as warmly as you could through
their palpable suspicion.

"Good evening!" the one observing you says.
"What brings you to the city of Gnarze?"

"Fortune and glory, my friend! I'm..."
"Fortune and glory, eh?" he interrupts. "Where you from?"
"I'm from..."

"You see anything about the missing Councilman?" another guard joins in
the interrogation.

"There were a few people back up the road, held up by Bandits. I didn't think I..."

"You sure about that?" the first guard breaks in again. "You have to come
with us, ruffian! We heard things differently."

The other guard blows a whistle and you're overwhelmed by their
reinforcements before you have a chance to explain what happened.
''')
        press2continue = input(">>>PRESS ENTER TO CONTINUE")
        clearME()
        print('''++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Instead of striding proudly through the city gates, you're led shackled and
ashamed to the holding cell in the guard station.

YOU LOSE!

THANKS FOR PLAYING!!!
''')
        press2continue = input(">>>PRESS ENTER TO CONTINUE")
    elif(part==16):
        print('''++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
At twilight, you crest the final hill on the road to the city of Gnarze, its
gates and massive wall built into the fortified ravine. On the lengthy
switchbacks, you take in the beauty of the city guard lighting torches
across the top of the wall.

The guards at the gate notice you from afar but pay little heed until you're
more or less within earshot of their debate.

"Well met, friend!" the guard on your left calls out, holding up a hand to
interrupt his companion. They both turn their focus fully on you.
"What business do you have in our fair city?"

You introduce yourself, "Well met, indeed! I'm Jorgen Wolfwinter from the
Winter Village." You reveal the Signet of the Council. "Councilman Gorfe
and his Coachman are up the road and require a patrol for assistance."

The guard turns to his companion, nods, and the other heads swiftly off
toward the guard barracks.

The first guard turns back to you, "Are you heading in, or going back with
the patrol?"

"Heading in," you explain. "We met on the road when I helped them out.
The Councilman hired me, but let me go to secure my lodging in the city."

"Thank you, Jorgen! Please enter and seek your arrangements."

The guard opens the person-sized door next to the giant city gate. Before he
closes it, you look back and see the patrol leave to find Gorfe and August
''')
        press2continue = input(">>>PRESS ENTER TO CONTINUE")
        clearME()
        print('''++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
CONGRATULATIONS!!! You've reached the city prepared to earn a good bit of
coin and better your reputation.

THANKS FOR PLAYING!!!
''')
        press2continue = input(">>>PRESS ENTER TO CONTINUE")
    elif(part==17):
        print('''++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
You crest the final hill on the road to the city. In the early twilight, the
road stretches down toward a fortified ravine with a massive wall built edge
to edge. Built into that are the famously gigantic gates to the city of
Gnarze, and in from of them are built a handful of huts and a guard barracks.

Descending the path, the lengthy switchbacks give you opportunity to take in
the beauty of the guards lighting the torches across the top of the wall.

The guards at the gate notice you from afar but pay little heed until you're
more or less within earshot of their debate.

"Well met, friend!" the guard on your left calls out, holding up a hand to
interrupt his companion. They both turn their focus fully on you.
"What business do you have in our fair city?"

You introduce yourself, "Well met, indeed! I'm Jorgen Wolfwinter from the
Winter Village. Although I've mainly come to earn some coin to help my people,
I've come across someone named Councilman Gorfe who needs your assistance
up the road."

At that, the second guard trots off to fetch a patrol. "I did my part to
defend he and his Coachman from some Bandits. They sent me to you for help.

"Thank you for this, Jorgen, and welcome to the city of Gnarze! We'll wave
your entry fee this one time."

You're led through a person-sized door in the wall next to the city gates.
''')
        press2continue = input(">>>PRESS ENTER TO CONTINUE")
        clearME()
        print('''++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
CONGRATULATIONS!!!

You're made it to your destination prepared to earn fortune and glory for
your Village!

THANKS FOR PLAYING!!!
''')
        press2continue = input(">>>PRESS ENTER TO CONTINUE")
    else:
        print('''++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
roadStory - else - if you see this text, contact me
''')
        press2continue = input(">>>PRESS ENTER TO CONTINUE")