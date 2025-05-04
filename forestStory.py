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
Since the attack on your village, you've had no time for anything but
resowing the fields for harvest. The Great Wood has been your home since you
were born, so the choice was clear. All of the little gullies, paths and
hills were known to you before you could even hold a sword. This late in the
season, anything could happen.
''')
    elif(part==2):
        print('''++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
"Be mindful, Jorgen," you think to yourself, remembering fondly the trials
in your journeys into the Great Wood. They weren't perfect trips, but they
taught you all of the important lessons you rely on to survive to this day.

Walking almost silently along the forest floor, you hear some kind of
commotion in the distance. You slow your pace and sneak to a stop trying to
hear what it might be, but even after a minute it was impossible to tell it
was anything other than people fighting. After it all dies down and you
decide to move on, you hear some steps behind you.

More than two legs...

You draw your sword as you spin to attack a wolf.
''')
    elif(part==3):
        print('''++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
"Be mindful, Jorgen," you think to yourself, remembering fondly the trials
in your journeys into the Great Wood. They weren't perfect trips, but they
taught you all of the important lessons you rely on to survive to this day.

You begin to feel something is a bit off when you start hearing what sounds
like people fighting. The commotion gets slightly louder, then fades quickly.
Slowing to try and hear better what was going on, instead you hear the sound
of an animal running toward you.

Before you could turn all the way around, a wolf is upon you.
''')
    elif(part==4):
        print('''++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Bent over and panting, you finally catch your breath. Only your experience
in the Great Wood saved you in this battle. You wipe your blade and sheath
it. Another wolf attack could happen at any moment, so you get your bearing
and continue on your journey.

You start to smell wood smoke not long afterward, and suddenly realize where
you are - the territory of the Hunter of the Great Wood. Folks from the
region who know of him leave him to his solitude. Those who don't only find
him by accident. Being currently in both groups, you proceed with caution.

The Hunter's cabin is revealed once you're through a light thicket. You see
a modest cabin made of logs, stone, and a lot of clay. In front, a
smoldering fire pit is bordered on one side by a fairly large vegetable
garden. The Hunter, however, is nowhere in sight.
''')
    elif(part==5):
        print('''++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Quick but thorough scans to the left and right reveal nothing. Then, almost
at the very edge of your perception as you glance over your shoulder,
something seems out of place. You continue looking around as a rouse,
however, to process what you think you saw and not let on you saw it.

"A figure in the tree," you decide.
''')
    elif(part==6):
        print('''++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
"My name is Jorgen Wolfwinter from the Winter Village!" you proclaim.
"I mean you no harm, Hunter!"

You briefly question the decision to engage like this until you hear the
tree behind you creek a bit, then a heavy thud on the ground as the Hunter
jumped from the tree and landed.

"Well met, Wolfwinter!" the Hunter greets you as if he were an old friend.
The puzzled look on your face gives him pause, though.

"I know Johann Wolfwinter, also from the Winter Village," he says.
"I've only traded with him a few times, though."

Johann, the Village's master blacksmith, was known to deal with all of the
folk in the region.

"Well met, then," you respond, smiling. It was good to know this encounter
would go well.

Soon after more introductions and a few quips, the Hunter invites you to
his cabin and, noticing your wounds from the wolf, gives you a HEALING
POTION. You both sit around his fire and get to more serious conversation.

"You couldn't have been looking for just me, though, friend," the Hunter
begins, "If you have somewhere to be, why travel through the Great Wood?
What circumstances brought you to my abode?"
''')
        press2continue = input(">>>PRESS ENTER TO CONTINUE")
        clearME()
        print('''++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
"I'm headed to the city of Gnarze to find my fortune and honor for my
village. Taking the road felt like missing out on the adventure, so I came
through here," you explain.

The Hunter smiles but says nothing. He gets up, goes briefly into his cabin,
emerging from its entrance with something in hand.

"Follow the right paths and you'll meet a ranger guarding the forest around
the gate to the city of Gnarze," he says, handing you a Wooden Pendant.

"Giving him this should get you into the city in good standing. He'll
return it to me, too, after you're safely inside."

"What a gracious gift! Thank you!"

"It's the least I can do to help your village," he explains. "The gates
aren't far from here. Even this late in the day, you should have no problem
reaching the city of Gnarze by dusk."

You bid your new friend farewell, tuck the Wooden Pendant into your belt
pouch, then make way once again to the city of Gnarze.
''')
        press2continue = input(">>>PRESS ENTER TO CONTINUE")
    elif(part==7):
        print('''++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
You slip your shield onto your arm and use it to bash the door down. It was
lighter than you'd expected, so with little effort it gives way and breaks
some more when it hits the floor.

A quick scan of the Cabin turned into more than a few minutes of looking
through the possessions of their former owner. Some supplies you already had,
a dagger to replace the one you lost in the fight, but no real riches except
a Wooden Pendant precariously balanced at the back of a shelf. The
craftsmanship is exquisite! You're sure it was precious to the Hunter.

On your way out, you quench the fire and grab one of the cooked meat skewers.

"Only one waste today," you say remorsefully and drape the Wooden Pendant
around your neck. You continue to the gates of Gnarze.
''')
        press2continue = input(">>>PRESS ENTER TO CONTINUE")
    elif(part==8):
        print('''++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
You slip your shield onto your arm and put your weight behind it as you bash
the door down. It was lighter than you'd expected, though, so you stumble in
and trip over a bench, landing awkwardly on what's left of the Cabin door.

A quick scan of the Cabin turned into more than a few minutes of looking
through the possessions of their former owner. Some supplies you already had,
a dagger to replace the one you lost in the fight, but no real riches. On
your way out, you quench the fire and grab one of the cooked meat skewers.

"Only one waste today," you say remorsefully and continue to
the gates of Gnarze.
''')
        press2continue = input(">>>PRESS ENTER TO CONTINUE")
    elif(part==9):
        print('''++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
You immediately stop and raise your hands in submission.

"My name is Jorgen Wolfwinter from the Winter Village," you tell him.
"I mean you no harm, Hunter."

"Breaking into my cabin IS harm, friend." He pauses. "Wolfwinter? I know
Johann from the Winter Village."

"The Blacksmith," you confirm. You slowly put your hands down and stand to
your height. "An honorable man, for sure, and far better a man then me,
it seems."

The Hunter smiles at your self-deprecation, but you can tell he still hasn't
totally changed his mind about you"

You apologize, "I'm sorry. I should've at least called out to you, instead."

At that, the Hunter's face softened just a little. You guess that was about
as much as you were getting.

"What brings you to my door, Jorgen?"

"I'm on my way to the city of Gnarze to find fortune and glory for my
village," you explain. "Bandits raided us and, although we've recovered,
some resources are beyond us."

"That's tragic to hear. I'll have to bring Johann some more business to help
out," the Hunter says, moving toward you.
''')
        press2continue = input(">>>PRESS ENTER TO CONTINUE")
        clearME()
        print('''++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
"Take one of the skewers, if you'd like. I hope you find what you're looking
for."

"Thank you," you reply after a pause. It seems you found some fortune with
him, but know not to press your luck.

You reach down and pluck a skewer from the ground as you walk away, then
look back once to nod. He returns the gesture and watches you walk away from
his camp. It's getting late, but you still think you can make it by dusk.
''')
    elif(part==10):
        print('''++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Since you lost your dagger fighting the Hunter, your only option is to bash
the door down.

You slip your shield onto your arm and use it to bash the door down. It was
lighter than you'd expected, so with little effort it gives way and breaks
some more when it hits the floor.

A quick scan of the Cabin turned into more than a few minutes of looking
through the possessions of their former owner. Some supplies you already had,
a dagger to replace the one you lost in the fight, but no real riches except
a Wooden Pendant precariously balanced at the back of a shelf. The
craftsmanship is exquisite! You're sure it was precious to the Hunter.

On your way out, you quench the fire and grab one of the cooked meat skewers.

"Only one waste today," you say remorsefully and drape the Wooden Pendant
around your neck. You continue to the gates of Gnarze.
''')
        press2continue = input(">>>PRESS ENTER TO CONTINUE")
    elif(part==11):
        print('''++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
You slip your shield onto your arm and put your weight behind it as you bash
the door down. It was lighter than you'd expected, though, so you stumble in
and trip over a bench, landing awkwardly on what's left of the Cabin door.

A quick scan of the Cabin turned into more than a few minutes of looking
through the possessions of their former owner. Some supplies you already had,
a dagger to replace the one you lost in the fight, but no real riches.
On your way out, you quench the fire and grab one of the cooked meat skewers.

"Only one waste today," you say remorsefully and continue to
the gates of Gnarze.
''')
        press2continue = input(">>>PRESS ENTER TO CONTINUE")
    elif(part==12):
        print('''++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
You turn to admire all the Hunter has afforded himself, then see a figure
approaching as if he materialized from the Great Wood itself.

It's the Hunter.

"My name is Jorgen Wolfwinter from the Winter Village!" you proclaim.
"I mean you no harm, Hunter!"

"Well met, Wolfwinter!" the Hunter greets you as if he were an old friend.
The puzzled look on your face gives him pause, though.

I know Johann Wolfwinter, also from the Winter Village," he says.
"I've traded with him many times."

Johann, the Village's master blacksmith, was known to deal with all of the
folk in the region.

"Well met, then," you respond, smiling. It was good to know this encounter
would go well.

Soon after more introductions and a few quips, the Hunter invites you to
have a seat and, noticing your wounds from the wolf, gives you a HEALING
POTION. You both sit around his fire and get to more serious conversation.

"You couldn't have been looking for just me, though, friend," the Hunter
begins, "If you have somewhere to be, why travel through the Great Wood?
What circumstances brought you to my abode?"

"I'm headed to the city of Gnarze to find my fortune and honor for my
village. Taking the road felt like missing out on the adventure, so I came
through here," you explain.
''')
        press2continue = input(">>>PRESS ENTER TO CONTINUE")
        clearME()
        print('''++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
The Hunter smiles but says nothing. He gets up, goes briefly into his cabin,
emerging from its entrance with something in hand.

"Follow the right paths and you'll meet a ranger guarding the forest around
the gate to the city of Gnarze," he says, handing you a Wooden Pendant.

"Giving him this should get you into the city in good standing. He'll return
it to me, too, after you're safely inside."

"What a gracious gift! Thank you!"

"It's the least I can do to help your village," he explains. "The gates
aren't far from here. Even this late in the day, you should have no problem
reaching the city of Gnarze by dusk."

You bid your new friend farewell, tuck the Wodden Pendant into your belt
pouch, then make way once again to the city of Gnarze.
''')
        press2continue = input(">>>PRESS ENTER TO CONTINUE")
    elif(part==13):
        print('''++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
You know there's still plenty of light left in the day to travel open ground,
but you are in the Great Wood and daylight hours don't last as long here. It
takes some concentration to stay on the path. Your attention divided, you're
surprised by a sudden voice from behind you.

"Ahoy, traveler! Do you serve the King's Regent?"

You halt and reply, "I am from the Winter Village and know nothing of him."

You turn when you hear the man emerge from some nearby foliage. Although his
sword is drawn, he's only walking toward you at a casual pace

"Then, well met, friend!" he greets you. "I've heard unfortunate tidings of
what had befallen you all, but I'm glad it seems like you're recovering."

"We have, yes," you reply as the Ranger sheaths his sword. You produce the
Wooden Pendant from your belt pouch and hold it out to him.

"I hope you're the person I'm supposed to see with this," you explain as
you place it in the Ranger's hand, "as I've been told by the Hunter of the
Great Wood that revealing this item to the Rangers of Gnarze would grant me
favor and perhaps a guide to the city gates."
''')
        press2continue = input(">>>PRESS ENTER TO CONTINUE")
        clearME()
        print('''++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
"Yes," he nods, "I am a Ranger, and I hope you know the boon bestowed on you.
The blessing of the Hunter of the Great wood is seldom, if ever, given. What
are you called, friend?"

"Jorgen Wolfwinter. You?"

"Burt. Now let's get going."

You follow Burt the Ranger through the remaining trails that lead to the
gates of Gnarze. At twilight, you crest the final hill on the road to the
city, its gates and massive wall built into a fortified ravine. On the
lengthy switchbacks, you take in the beauty of the city guard lighting
torches across the top of the gigantic wall in the early evening light.

The guards at the gates notice you from afar but pay little heed until you're
more or less within earshot of their debate.

"Well met, friend!" the guard on your left calls out, holding up a hand to
interrupt his companion. They both turn their focus fully on you.

"What business have you in our fair city?"

You introduce yourself, "Well met, indeed! I'm Jorgen Wolfwinter from the
Winter Village. I've come to earn coin to help rebuild after a Bandit attack."
''')
        press2continue = input(">>>PRESS ENTER TO CONTINUE")
        clearME()
        print('''++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
"I helped lead him, for a time, through the Great Wood," Burt finally piped
up. "He gave me the Wooden Pendant of the Hunter of the Great Wood."
You notice the shocked admiration of the two guards.

"He requested that be returned to him," you turn and say to Burt.

"I surely will!" he agrees. "Thank you, Jorgen."

The guard you had spoken to opens the person-sized door next to the giant
city gate to let you in. The other guard is called away back to his position
as another small group of people approach his station.
''')
        press2continue = input(">>>PRESS ENTER TO CONTINUE")
        clearME()
        print('''++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
CONGRATULATIONS! You've made it to your destination prepared to earn a good
bit of coin and better your reputation!

THANK YOU FOR PLAYING!!!
''')
    elif(part==14):
        print('''++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
You know there's still plenty of light left in the day to travel open ground,
but you are in the Great Wood and daylight hours don't last as long here. It
takes some concentration to stay on the path. Your attention divided, you're
surprised by a sudden voice from behind you.

"Ahoy, traveler! Do you serve the King's Regent?"

You halt and reply, "I am from the Winter Village and know nothing of him."

You turn when you hear the man emerge from some nearby foliage. Although his
sword is drawn, he's only walking toward you at a casual pace

"Then, well met, friend!" he greets you. "I've heard unfortunate tidings of
what had befallen you all, but I'm glad it seems like you're recovering."

"We have, yes," you reply as the Ranger begins to sheath his sword. He's
measuring you, scanning from head to toe. With his sword finally sheathed,
he approaches, offering his hand.

"You've met the Hunter, I see," he says, looking at the Wooden Pendant around
your neck. You nod, smiling.

The Ranger walks over to a large, stony outcrop with a pile of somewhat mossy
rocks, puts one foot on them and leans on his raised knee.
''')
        press2continue = input(">>>PRESS ENTER TO CONTINUE")
        clearME()
        print('''++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
"I hope you know the boon bestowed on you. The blessing of the Hunter of the
Great Wood is seldom, if ever, given."

You nod again, then you both hear a whistle from somewhere - perhaps multiple
places at once. The Ranger, unfazed, tilts his head back and whistles a
different melody.

"Where are you heading tonight, traveler from the Winter Village?"
he pleasantly asks.

"To the city of Gnarze to earn some fortune for my people," you tell him.
"As you know, the Bandit raid was devastating. We're doing better but need
more supplies."

"What was the Hunter's advice when you told him?" he asks,
motioning to the Wooden Pendant.

You glance down, acknowledging his gesture and reply,
"He said it would bring me luck on my adventure..."

At that, you're interrupted by the Ranger's sharp whistle, followed by the
whistle of an arrow before it plunges into your throat. Shocked, trying to
staunch the blood gushing from you, then laying down to die, your last
experience is the Ranger standing above you.

The chord around your neck snaps as he grabs the Wooden Pendant. "The Hunter
would never have given this away for someone to keep. Your lies have given
you away."
''')
        press2continue = input(">>>PRESS ENTER TO CONTINUE")
        clearME()
        print('''++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
You have failed your quest.

THANK YOU FOR PLAYING!!!
''')
    elif(part==15):
        print('''++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
You know there's still plenty of light left in the day to travel open ground,
but you are in the Great Wood and daylight hours don't last as long here.
It takes some concentration to stay on the path. Your attention divided,
you're surprised by a sudden voice from behind you.

"Ahoy, traveler! Do you serve the King's Regent?"

You halt and reply, "I am from the Winter Village and know nothing of him."

You turn when you hear the man emerge from some nearby foliage. Although his
sword is drawn, he's only walking toward you at a casual pace

"Then, well met, friend!" he greets you. "I've heard unfortunate tidings of
what had befallen you all, but I'm glad it seems like you're recovering."

"We have, yes," you reply as the Ranger sheaths his sword. The Ranger walks
over to a large, stony outcrop  with a pile of somewhat mossy rocks, puts
one foot on them and leans on his raised knee.

"What do I call you, traveler from the Winter Village, and where are you
headed?" the Ranger asks.

"Jorgen Wolfwinter, and I'm headed to the city of Gnarze to earn some
fortune for my people," you tell him. "As you know, the Bandit raid was
devastating. We're doing better but need more supplies."
''')
        press2continue = input(">>>PRESS ENTER TO CONTINUE")
        clearME()
        print('''++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
You both suddenly hear a whistle from somewhere - perhaps multiple places at
once - in the Wood.

The Ranger, unfazed, tilts his head back and whistles a different melody,
then makes his way toward you.

"I am Burt, a Ranger tasked with protecting Gnarze and the Great Wood around
it." He offers you his hand, then says, "It's getting late. If you follow me,
we can make it to the gates by twilight."

You follow Burt the Ranger through the remaining trails that lead to the
gates of Gnarze. At twilight, you crest the final hill on the road to the
city, its gates and massive wall built into the fortified ravine. On the
lengthy switchbacks, you take in the beauty of the city guard lighting
torches across the top of the wall.

The guards at the gate notice you from afar but pay little heed until you're
more or less within earshot of their debate.

"Well met, friend!" the guard on your left calls out, holding up a hand to
interrupt his companion. They both turn their focus fully on you. "What
business do you have in our fair city?"

You introduce yourself, "Well met, indeed! I'm Jorgen Wolfwinter from the
Winter Village. I've come to earn some coin to help my village."

"The Winter Village! You have my sympathies for your losses," the guard says.

You all bid Burt farewell, then the guard leads you to the person-sized door
next to the enormous gates.
''')
        press2continue = input(">>>PRESS ENTER TO CONTINUE")
        clearME()
        print('''++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
You've made it to your destination prepared to earn a good bit of coin and
better your reputation.

CONGRATULATIONS!!!

THANKS FOR PLAYING!!!
''')
    else:
        print('''++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
forestStory - else - if you see this text, contact me
''')
        press2continue = input(">>>PRESS ENTER TO CONTINUE")