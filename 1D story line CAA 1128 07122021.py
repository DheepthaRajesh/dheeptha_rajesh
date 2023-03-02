import random
from time import sleep
import TicTacToe1
import threading

with open("MuddyArea.txt","w") as f1:
    f1.write("\nWear your walking boots when passing this area")
    f1.write("\nUse poles and plant by your backfoot as this provides a strong stabiliser as you push off")
    f1.write("\nAlways keep one pole in firm contact with the ground")
    f1.write("\nPull your tummy button towards your spine as this will engage your core muscles and give you greater balance")
    f1.write("\nRelax your neck and shoulders while walking")
    f1.write("\nReduce your arm swing")
    f1.write("\nSlow down and reduce your stride length significantly")
f1.close()

with open("SaveTrees.txt","w") as f2:
    f2.write("\nTrees are an important foundation for a liveable and sustainable city")
    f2.write("\nThey improve both air and water quality by absorbing pollutants, intercepting particulates, releasing oxygen, reducing ozone levels and reducing soil erosion")
    f2.write("\nBy capturing some of the falling rain with their leaves and increasing the capacity of soil to absorb rainwater, trees reduce the strain on our stormwater drainage network")
    f2.write("\nTrees reduce greenhouse gases when they take in carbon dioxide from the atmosphere and store it as wood")
    f2.write("\nTrees enhance community well-being. Studies show that exposure to greenery improves the attention levels and cognitive functioning of children")
    f2.write("\nUrban trees and green spaces are beneficial to our physical and mental health")
f2.close()

with open("poisonousInsects.txt","w") as f3:
    f3.write("\nTake shelter and avoid hiking near this area during dusk or dawn")
    f3.write("\nApply bug spray and repellent")
    f3.write("\nEat garlic or onion if available as they contain high traces of insect-repelling allicin")
    f3.write("\nRemove bee stingers or ticks immediately")
    f3.write("\nTo treat insect bites, use antispectic soap to clean the wound and cold compress or ice to reduce swelling, pain and itching")
f3.close()

def timerinsecs():
    global timer
    timer = 15

    for a in range(timer):
        timer -= 1
        sleep(1)
        
def Truth(checklist,sentence):
    while True:
        choice = input(sentence)
        if choice not in checklist:
            print("INVALID answer! Please type the number next to the action.")
            print()
        else:
            break
    return choice

def choice(mylist,sentence = "You choose to: "):
    print()
    numberofchoice = [str(i+1) for i in range(len(mylist))]
    for i in range(len(mylist)):
        Toadd = "\n" + str(i+1) + ") " + mylist[i]
        sentence += Toadd
    sentence = sentence + "\n" + "\nWhat do you choose? "
    choice = Truth(numberofchoice,sentence)
    return choice

class Person:
    
    def __init__(self,name,gender="He"):
        self.__name = name
        self.__moral = 5
        self.__gender = gender
    
    def name(self):
        return self.__name

    def moraldecrease(self):
        self.__moral += -1

    def moraltest(self):
        if self.__moral < 3:
            return False
        return True

    def gender(self,lower=False):
        if lower:
            return self.__gender[0].lower() + self.__gender[1:]
        return self.__gender

    def gender2(self,lower=False):
        if self.__gender == "He":
            if lower:
                return "his"
            return "His"
        elif self.__gender == "She":
            if lower:
                return "her"
            return "Her"
    
    def gender3(self,lower=False):
        if self.__gender == "He":
            if lower:
                return "him"
            return "Him"
        elif self.__gender == "She":
            if lower:
                return "her"
            return "Her"

def RPS():
    while True:
        mydict = {"ROCK":"PAPER","PAPER":"SCISSORS","SCISSORS":"ROCK"}
        mylist = ["ROCK", "PAPER", "SCISSORS"]
        mylistplay = [("Play " + x) for x in mylist]
        print("Anne prepares to throw her hand...")

        decision = int(choice(mylistplay))
        symbol = mylist[decision-1]
        computer = mylist[random.randint(0,2)]
        if computer in mydict[symbol]:
            print(f"\nYou played {symbol}!")
            print(f"Anne PLAYED {computer}!")
            print("YOU LOST!\n")
            print('"Yes, I won!" Anne exclaims. "This is fun!"')
        elif computer == symbol:
            print(f"\nYou played {symbol}!")
            print(f"Anne PLAYED {computer}!")
            print("YOU TIED!\n")
            print('"A tie huh?" Anne says, disappointed. "At least I didn\'t lose..."')
        else:
            print(f"\nYou played {symbol}!")
            print(f"Anne PLAYED {computer}!")
            print("YOU WIN!\n")
            print('"Awww, I lost..." Anne complains. "I want to play once more!"')
            
        print("Do you want to keep playing against Anne?")
        answer = choice(["Keep playing","No"])
        if answer == "1":
            continue
        return

def main():
    endinglist = []
    KeepPlaying = True
    while KeepPlaying:
        while True:
            while True:
                decision = choice(["Start Game","View Credits","View Endings"],"Welcome to the game!")
                if decision == "1":
                    break
                elif decision == "2":
                    print()
                    print("This game was made by: ")
                    print("Deoferio Raizel Hannah Quirimit")
                    print("Dheeptha Rajesh")
                    print("Chew Kia Hwee")
                    print("Skyler Teo")
                    print("Syarifuddin Azhar Bin Rosli ")

                elif decision == "3":
                    print()
                    if endinglist == []:
                        print("NO ENDINGS ACHIEVED!")
                    else:
                        print("You achieved: ")
                        print()
                        for i in endinglist:
                            print(i)

            name = input("Enter your character's name: ")
            gender = choice(["Play as a guy","Play as a girl"])
            if gender == "1":
                gender = "He"
            else:
                gender = "She"
            Main_Character = Person(name,gender)

            name = input("Enter the name of your first friend: ")
            gender = choice(["A guy","A girl"],"They are: ")
            if gender == "1":
                gender = "He"
            else:
                gender = "She"
            FriendA = Person(name,gender)

            name = input("Enter the name of your second friend: ")
            gender = choice(["A guy","A girl"],"They are: ")
            if gender == "1":
                gender = "He"
            else:
                gender = "She"
            FriendB = Person(name,gender)

            name = input("Enter the name of your third friend: ")
            gender = choice(["A guy","A girl"],"They are: ")
            if gender == "1":
                gender = "He"
            else:
                gender = "She"
            FriendC = Person(name,gender)

            bear_path = False

            print(f"""The evening sun beat down on your neck as you pushed on through the forest. The drone of bug calls combined with the rhythmic footsteps of your friends lulled you into an almost hypnotic state. Your mouth felt like sand and the sweltering 35 degrees wasn't helping. Feeling for your water bottle, you were once again reminded of its emptiness when u felt its lack of weight. Your last drops of water had been sucked dry an hour or two ago.\nIn a moment of foolish curiosity, your group had gone off the beaten path to take a side route while on your planned group trek. The 'path' had quickly disappeared. when your group decided to turn around, all you could see was a wall of green, the forest having seemingly swallowed the path behind you. you glance up at the sky for the thousandth time, the sun was lower since you checked an hour ago.\nAt the rate the sun was setting, your team had another hour or two before it got too dark to continue. A question from {FriendA.name()} broke the silence and pulled you back to attention.\n “Which direction are we heading? Wasn’t there a ranger out post somewhere in the west? We might run into a patrol route that they use if we head that way”.\n{FriendB.name()} grouched, “Finally, something useful came out of that air head of yours”.\n“Hey, what do you mean by air head”. \n“Well, it was your idea to go off the planned route, dumb ass.” \n{FriendC.name()} having had enough of their quibbling, cuts in “enough you two! Arguing isn’t gonna make anything better. Save your energy for walking”.\n{FriendC.gender()} then turns to you, “So any idea where we are?” """)

            direction = choice(["North","South","East","West"],"which direction are you facing? ")

            west1 = """ You glanced at the sky again. You determine saw the sun to your right, therefore you deduced that you were heading {} as the sun sets towards {}.""".format(direction, direction)

            west2 = """  Your group heads off due west, and by some measure of luck, you guys stumbled upon a ranger patrol path. Following the path, your group finds a ranger outpost, and the park rangers in there helped to get you home safely. Your group learnt the importance of staying to known paths after this incident."""

            wrong = f"""  Trudging on, it was starting to get visibly darker. You figured that it was a good idea to probably stop and rest. After all, there won’t be much point trying to feel your way through the darkness at night. You voice your opinion out to your group. {FriendA.name()} argues: “we have been walking for so long already, we can’t be far from the ranger outpost, right? Let’s just push on, we should be able to find it before it gets dark” """

            if direction == "4":
                print(west1)
                print("""  Your group heads off due west, and by some measure of luck, you guys stumbled upon a ranger patrol path. """)
                print("Following the path, your group finds a ranger outpost")
                print("It's empty, so you play Tic Tac Toe while waiting for the park ranger.")
                sleep(2)
                TicTacToe1.my_func()
                ##code is sourced from https://www.tutorialspoint.com/How-can-I-source-a-Python-file-from-another-Python-file
                sleep(2)
                print("Afterwards, the park rangers arrive.")
                print("They help you get home safely.")
                print("Your group learnt the importance of staying to known paths after this incident.")
                print("FAST ENDING!")
                if "FAST ENDING" not in endinglist:
                    endinglist.append("FAST ENDING")
                
                break

            else:
                print(wrong)

            Rest_push = choice(["Rest","Push on"])

            if Rest_push == "1":
                print(f"""{FriendC.name()}, being the ever reason of the group, reasons that: “look, we have no idea how far we are from the out post and, therefore no idea if we can reach it before sunset. It will be better if we rest first and continue tomorrow morning.”\nYour group, agreeing that {FriendC.gender()} had a point, decided to stop for the night and set up camp. The whine of a mosquito near your ear reminded you that setting up a fire is probably a good idea to prevent yourselves from getting eaten alive by bugs at night.\n“We should probably set up a fire and a shelter. This should keep the bugs away from us at night, as well as any wild animals. Let’s split up into pairs and look for the materials we need for those.”\n{FriendC.name()} approves. “Good idea, we can build a lean to as a quick easy shelter. Look for a sturdy tree that is small enough that you can bring back here. {FriendB.name()} and I will look for firewood.”\nLooking around the vicinity, you manage to find a sapling that was about the thickness of your wrist.\n“Well, that’s part of the problem solved, now how do we get it out of the ground? I don’t have a saw.”\n“Not an issue”, {FriendB.name()} strolled over and squatted down. {FriendB.gender()} gripped the tree with both hands, and with a heave, {FriendB.gender(True)} uprooted the whole tree out of the ground.\n“Remind me not to get in a fight with you”, you silently muttered to yourself.\n{FriendB.name()} tossed the sapling onto {FriendB.gender(True)} shoulder and the two of you made the way back to camp. Upon reaching camp, you saw that {FriendC.name()} and {FriendA.name()} had already started a fire.\n{FriendC.name()} told you that {FriendC.gender(True)} fashioned a bow out of a stick and her shoelaces. {FriendC.gender()} then twisted the string of the bow around a stick. Placing the stick vertically between a piece of wood and a stone and by moving the bow back and forth in a sawing motion, {FriendC.gender(True)} got the stick to spin at a high enough speed to start an ember.\n{FriendC.gender()} than wrapped the ember in some tinder and blew on it till it lit. After that, {FriendC.gender(True)} slowly fed it twigs till it was steady.\nIt had taken {FriendC.gender3(True)} quite a few tries to get the ember to catch and not go out.\nIt was now time to set up the lean to. First, you had to strip the sapling of all its branches as well scavenge the trees nearby for more branches. Next you leaned the main trunk of the sapling against a sturdy trunk, leaving enough space for the four of you to lie under to rest. After that, you piled the branches which you collected against one side of the sapling.\nThis created a ‘roof’ which could protect you from some light rain. By the time you were done, the sun had already set. The four of you gathered around the fire to rest after a long day of trekking and manual work. After having not eaten for almost a whole day, the four of you rummaged through tour bag for something to eat.\n""")

                check_stock = choice(["Eat till full","Check what you have and then ration it"],"Do you: ")

                Take_stock = """  Your group decide to lay out your supplies in the fire light. Seeing the amount of food you had, you decided to ration in case you all were stuck in here for more than 2 to 3 days. Having each eaten your portion of the ration, you kept the rest of the rations on a branch high off the ground to avoid animals from raiding it, and headed under the makeshift shelter for the night. Lying down, the four of you took notice of the night sky for the first time that night. The shimmering expanse of the milky way cover the whole sky. The sight took your breath away, this view would have been impossible to see with the amount of light pollution there was in the city. The four of you watched the starry night sky in silence till, one by one, each of you drifted off to sleep."""

                just_eat = """  You all ate your fill that night. After all, it would be trek through the forest if u had enough energy for the next day. Your group kept the rest of the remaining food on a branch high off the ground to avoid animals from raiding it, and headed under the makeshift shelter for the night. Lying down, the four of you took notice of the night sky for the first time that night. The shimmering expanse of the milky way cover the whole sky. The sight took your breath away, this view would have been impossible to see with the amount of light pollution there was in the city. The four of you watched the starry night sky in silence till, one by one, each of you drifted off to sleep."""

                if check_stock == "2":
                    print(Take_stock)
                else:
                    print(just_eat)
            else:
                print(f""" Your group continue walking through the forest, when {FriendB.name()} stops in his tracks. "There's something behind us", he whispered harshly. {FriendA.name()} snorted:"yeah, right, just move your ass and talk less". We reckoned it was just him hallucinting as we were dehydrated, tired and in the dark. He was also falling behind in your hike. you all trudged on without looking back. All of a sudden, you hear a loud scream coming from behind you. When you look back, your group froze. You see {FriendA.name()} being attacked by something. You could not make out the shape of the assailant in the darkness, but one thing was obvious, it was huge nearly twice you height. {FriendA.name()} continued to pummel {FriendA.gender2(True)} fist against the creature while screaming. {FriendA.gender2()} punch did not seem to faze the creature. The creature continued savaging {FriendA.gender3(True)}. You broke out of you stupor and started running towards {FriendA.gender3(True)} to help, but it seemed like you were running through molasses. {FriendA.gender()} was now being dragged away by the blighted creature. As you reach where {FriendA.name()} originally was, {FriendA.gender2(True)} feet were dragged, thrashing, into the darkness of the jungle beyond what your eyes could make out. You stood there, staring numbly into the darkness where your friend was just dragged of into. the metallic smell of blood permeated the air.""")

                bear_path = True

            if bear_path:
                chase_push = choice(["Chase after your friend","push on"], "Do you: ")
                
                if chase_push == "1":
                    print(f"""  Unwilling to accept defeat, you ran after the thing, following the trail {FriendA.name()} made when he was dragged. At the end of the trail,you found {FriendA.gender(True)} being mauled by the creature. {FriendA.gender()} was not moving, was {FriendA.gender(True)} even still alive? You slowly crept closer, staying low to the under brush to avoid being detected by the vile creature. once you got within 5 meters, for the first time, you finally got a view of what that creature was. A tiger. it finally stopped mauling at friend A after 5 minutes. """)

                    hide_noise = choice(["Remain hidden","Make noise to scare away the tiger"])
                    if hide_noise == "2":
                        print(f"""  The tiger ran away. You approach bleeding {FriendA.name()} and remember that you have a medical kit in your backpack. Should you help {FriendA.name()} using your med kit or should you save it for later, in case the bear attacks again? """)

                        
                        help_not = choice(["Help","Don't"])
                        if help_not == "1":
                            print(f""" You bandage {FriendA.name()} wounds and reunite with your other friends. You start walking into the wilderness, hoping to find civilization.{FriendC.name()} is carrying {FriendA.name()} on his back, slowing {FriendC.gender3(True)} down. {FriendB.name()} shouts from a short distance 'I found light!' You and your friends start running towards it but {FriendC.name()} is slowed down by {FriendA.name()}. Your group hear growling at a distance and you suggest for all of us to run faster. {FriendC.name()} could not follow through and tells you to get help. With hesitance, {FriendB.name()} and you ran towards the fading light. """)
                            timerinsecs_thread = threading.Thread(target=timerinsecs)
                            timerinsecs_thread.start()
                            while timer > 0:
                                message = "Grab your friend by the wrist and forearm. This is to avoid spraining the wrist."
                                display = "You have 15 seconds to type this: " + message + " "
                                answer = input(display)

                                if answer == message and timer>0:
                                    print("You have managed to save your friend.")
                                    print("As you run away, you spot a light flashing in your direction.")
                                    print("It is a park ranger. You have managed to find help!")
                                    print("RESCUE END!")
                                    if "RESCUE END" not in endinglist:
                                        endinglist.append("RESCUE END")
                                    break

                                elif answer != message or timer==0:
                                    if answer != message:
                                        print("You entered the wrong input!")
                                    else:
                                        print("Too slow!")
                                    print("You tried your best, but the sweat made gripping impossible.")
                                    print("You had to leave, but not your friend.")
                                    print("The monster got the better of them.")
                                    print("Your other friends succumb too.")
                                    print("Now, you are all alone.")
                                    print("BAD END!")
                                    if "BAD END" not in endinglist:
                                        endinglist.append("BAD END")
                                    break

                            break

                        else:
                            print(f""" You watched as {FriendA.name()} dies. {FriendB.name()} comes behind me and sees what happened.Immediately {FriendB.gender()} runs to you and punches you. {FriendC.name()} comes along and stops {FriendC.gender3(True)} from hitting another punch.{FriendC.name()} says "we should move on before the bear comes back", but {FriendB.name()}, still furious, refuses to move. The two of you leave {FriendB.gender3(True)} with {FriendA.name()} and promise that once you find someone who could help, you would direct him to them. {FriendC.name()} and you start walking again. After a while, {FriendC.name()} shouts from a short distance 'I found light!' The two of you start running towards it. You two hear growling at a distance which prompts you to run faster.""")

                            timerinsecs_thread = threading.Thread(target=timerinsecs)
                            timerinsecs_thread.start()

                            while timer > 0:
                                if timer == 0:
                                    break

                                message = "Run away from the bear quickly! Help is on the horizon"
                                display = "You have 15 seconds to type this: " + message + " "
                                answer = input(display)

                                if answer == message and timer>0:
                                    print("You manage to run away from the bear.")
                                    print("As you run away, you spot a light flashing in your direction.")
                                    print("It is a park ranger. You have managed to find help!")
                                    print(f"Perhaps {FriendB.name()} will be saved too...")
                                    print("RESCUE END!")
                                    if "RESCUE END" not in endinglist:
                                        endinglist.append("RESCUE END")
                                    break
                                
                                elif answer != message or timer==0:
                                    if answer != message:
                                        print("You entered the wrong input!")
                                    else:
                                        print("Too slow!")
                                    print("Alas, the bear catches with you.")
                                    print("As the monster closes in, you start to think back to your past memories.")
                                    print("You never should have gone hiking with your friends.")
                                    print("Darkness clouds your vision...")
                                    print("BAD END")
                                    if "BAD END" not in endinglist:
                                        endinglist.append("BAD END")
                                    break
                            
                            break
                        
                    else:
                        print(f""" You watched as {FriendA.name()} dies. {FriendB.name()} comes behind me and sees what happened. Immediately {FriendB.gender()} runs to you and punches you. {FriendC.name()} comes along and stops {FriendC.gender3(True)} from hitting another punch. {FriendC.name()} says "we should move on before the bear comes back", but {FriendB.name()}, still furious, refuses to move. The two of you leave {FriendB.gender3(True)} with {FriendA.name()} and promise that once you find someone who could help, you would direct him to them.{FriendC.name()} and you start walking again. After a while, {FriendC.name()} shouts from a short distance 'I found light!'The two of you start running towards it. You two hear growling at a distance which prompts you to run faster.""")

                        timerinsecs_thread = threading.Thread(target=timerinsecs)
                        timerinsecs_thread.start()

                        while timer > 0:
                            message = "Run as fast as you can! You have to seek help!"
                            display = "You have 15 seconds to type this: " + message + " "
                            answer = input(display)

                            if answer == message and timer>0:
                                print()
                                print("Thankfully, you manage to escape from the bear")
                                print("As you run away, you spot a light flashing in your direction.")
                                print("It is a park ranger. You have managed to find help!")
                                print(f"{FriendA.name()} might have died but maybe you can save {FriendB.name()}...")
                                print("RESCUE END.")
                                if "RESCUE END" not in endinglist:
                                    endinglist.append("RESCUE END")
                                break

                            elif answer != message or timer==0:
                                print()
                                if answer != message:
                                    print("You entered the wrong input!")
                                else:
                                    print("Too slow!")
                                print("Try as you may, you can't shake off the bear")
                                print("As it closes in, you think back to your past memories.")
                                print("You never should have went on this hiking trip.")
                                print("Darkness starts to cloud your vision...")
                                if "BAD END" not in endinglist:
                                    endinglist.append("BAD END")
                                break
                        break

                    
                else:
                    print(f"""  {FriendC.name()} chases after {FriendA.name()} into the wilderness.There was only two of you left.You started walking again. After a while, {FriendB.name()} shouts from a short distance 'I found light!' the two of you start running towards it. you both heard growling at a distance which prompts you to run faster""")

                    timerinsecs_thread = threading.Thread(target=timerinsecs)
                    timerinsecs_thread.start()
                    while timer > 0:
                        message = "Run faster and seek help. Escape from the bear!"
                        display = "You have 15 seconds to type this: " + message + " "
                        answer = input(display)

                        if answer == message and timer>0:
                            print()
                            print("You manage to run away from the beast")
                            print("As you run away, you spot a light flashing in your direction.")
                            print("It is a park ranger. You have managed to find help!")
                            print(f"Perhaps {FriendC.name()} and {FriendA.name()} can also be saved...")
                            print("RESCUE END")
                            if "RESCUE END" not in endinglist:
                                endinglist.append("RESCUE END")
                            break

                        elif answer != message or timer==0:
                            print()
                            if answer != message:
                                print("You entered the wrong input!")
                            else:
                                print("Too slow!")
                            print("You tried your best, but the monster catches up with you regardless.")
                            print("As the monster closes in, you start to think back to your past memories.")
                            print("You never should have gone hiking with your friends.")
                            print("Darkness clouds your vision...")
                            print("BAD END")
                            if "BAD END" not in endinglist:
                                endinglist.append("BAD END")
                            break
                    break
    
            else:
                print("You continue walking along the trail with your friends.")
                print("Before long, you reach a muddy area.")
                print("You start to recall something about muddy areas...")
                print("Do you focus on these thoughts?")

                decision = choice(["Yes","No"])
                if decision == "1":
                    print("That's right! You heard about tips for muddy areas before!")
                    print("If you don't recall wrongly, they go like this: ")
                    with open('MuddyArea.txt','r') as f:
                        for line in f:
                            print(line.strip())
                    f.close()
                    print()
                    print("With this information in mind, you feel more confident going forward.\n")

                else:
                    print("Whatever these thoughts are, they probably don't matter")
                    print("You push them aside as you forge onwards with your friends")

                print(f'"We should probably wear our boots before crossing", {FriendB.name()} says.\n')
                print(f'"Can we not? They are such a pain to put on..." {FriendA.name()} grumbles.\n')
                print(f'"You think so too, right {Main_Character.name()}?"')

                decision = choice(["Yes, let's not put on shoes","No, we should put on shoes"])
                if decision == "1":
                    Main_Character.moraldecrease()
                    print("You decide to forgo your boots. You're just stepping on some mud. What's the harm?")
                    print(f'"That\'s the spirit!" {FriendA.name()} proclaims, "Why do something so pointless?"\n')
                    print("As it turns out, your carelessness proves to your undoing.")
                    print("You slip as you step on the mud, almost crashing to the ground.")
                    print(f"Thankfully, {FriendB.name()} catches you before you can fall.\n")
                    print(f'"See, it pays to be careful," {FriendB.gender()} says.\n')
                    print(f"To your right, you hear {FriendA.name()} falling. You really should have put on your boots after all.")
                    print("At any rate, you continue moving.\n")

                else:
                    print("It's a hassle, but you decide to put on your shoes anyways. Better safe than sorry.")
                    print(f'{FriendA.name()} grumbles as he reluctantly puts on his boots too.')
                    print("Now adequately prepared, you trudge through the thick mud.\n")

                print("The muddy area seems to span forever with no end in sight.")
                print("Maybe it might be better to pick up your pace...")

                decision = choice(["Move faster","Stay at the same pace. It's better to move slower"])
                if decision == "1":
                    Main_Character.moraldecrease()
                    print("Heedless of the environment, you run forward.")
                    print("As you rush onwards, you bump into various objects near your feet. It doesn't matter.")
                    print("Anything to get out of this nasty environment faster.\n")
                    print(f'Somewhere in the distance, you hear {FriendB.name()} sigh.')
                    print("After a while, you find yourself out of the muddy area, albeit with a few scratches.\n")

                else:
                    print("There's no need to rush. Safety is more important.")
                    print("It takes a long while, but you eventually make it out of the muddy area with your friends.\n")

                print(f'"Hey, is that a waterfall at the end of the trail?" {FriendC.name()} says from behind.\n')
                print(f"You follow {FriendC.gender2(True)}'s gaze.")
                print("Indeed, there is a impressive waterfall.\n")
                print(f'"We should explore it," suggests {FriendB.name()}')
                print("And so, you do.\n")

                print("While exploring around the waterfall, you notice a derelict and forgotten hut around the back of the waterfall.")
                print("You and your friends are hesitant on whether to move closer to the hut or not")
                print(f"But then, {FriendB.name()} notices something.\n")
                print(f'"What\'s this apple tree doing here," he says, approaching it. You and your other friends start to move closer too.')
                print("You can't explain it, but the tree just seems so welcoming...")
                print('"Ah...people!" a unfamiliar voice says.\n')
                print("You turn to see a girl emerging from the hut.")
                print("She introduces herself as Anne, a lost hiker like you.\n")
                print("Curious, you and your friends probe Anne further.")
                print("She explains that she was on a mission SaveTrees! and she came to this forest to plant more trees and to encourage others to do so.")
                print("Unfortunately, she got lost when she was separated from her team and survived with limited supplies and the apple tree she had planted earlier")
                print("Noticing your confusion about SaveTrees!, Anne starts to explain her mission.")

                with open('Savetrees.txt','r') as f:
                        for line in f:
                            print(line.strip())
                f.close()

                print()
                print("You and your friends are inspired by Anne's speech.")
                print("Until today, you never really appreciated the environment. Now, you're starting to feel otherwise.\n")
                print(f'"Well, we can\'t help the environment if we\'re stuck here...." {FriendA.name()} says.')
                print(f'"So what do you think, Anne? Want to help us escape?" {FriendC.name()}.\n')
                print("After some convincing, Anne agrees to join your team.")
                print("You and your friends rest for a bit at her hut before setting forth again.\n")
                print("This time, you enter a swamp surrounded by insects and bugs...\n")
                print("You start to recall something about poisonous insects...\n")
                print("Do you focus on these thoughts?")
                decision = choice(["Yes","No"])

                if decision == "1":
                    print("That's right! You heard about tips for poisonous before!")
                    print("If you don't recall wrongly, they go like this: ")
                    with open('poisonousInsects.txt','r') as f:
                        for line in f:
                            print(line.strip())
                    f.close()
                    print()
                    print("With this information in mind, you feel more confident going forward.\n")

                else:
                    print("Whatever these thoughts are, they probably don't matter.")
                    print("You push them aside as you forge onwards with your friends.\n")

                print("Suddenly, a swarm of poisonous insects approaches your group.")
                print("Anne shrieks as she pulls out garlic from her bag.\n")
                print('"I-I heard that insects don\'t like garlic. Maybe if we hurl these at them, t-they\'ll go away!"')

                decision = choice(["Let Ann throw the garlic","Eat the garlic instead"])
                if decision == "1":
                    Main_Character.moraldecrease()
                    print("Anne tosses garlic at the insects, to no avail.")
                    print("The insect swarm simply weaves past the garlic. If anything, Anne's actions seems to have irritated the insects.\n")
                    print("Panicking, you and your friends run away from the insects.")
                    print("It takes a while, but you manage to shake the insects off.\n")

                else:
                    print("You tell Anne and your friends to eat the garlic instead.\n")
                    print('"Garlic wards off insects!" You say.\n')
                    print("Your friends takes your advice and chew down on the garlic.")
                    print("It seems to be effective. The insect swarm promptly scatters off.\n")

                print(f'"Ah!" {FriendC.name()} shrieks. {FriendC.gender()} raises {FriendC.gender2(True)} hand\n')
                print(f"Despite your best efforts, an insect has bitten {FriendC.name()}.\n")
                print(f'"We should treat the bite..." Anne says as she rummages through her bag. "But I can\'t seem to find my antiseptics..."\n')
                print(f"You turn to {FriendA.name()} and {FriendB.name()} for help.")
                print("They shrug their shoulders. It seems that they don\'t have antiseptics too.\n")
                print(f'"Don\'t mind me..." {FriendC.name()} says. "The longer we stay here, the sooner the insect swarm might return."\n')
                print(f"{FriendC.gender()} raises a good point.")
                print("It's just a simple insect bite after all, right?")

                decision = choice(["Wait for Anne to find her antiseptices","Carry on moving. The insect swarm might return"])
                if decision == "1":
                    print(f'"No, we should really treat that bite as soon as we can," you say, looking at {FriendC.name()}.\n')
                    print(f"{FriendC.name()} opens {FriendC.gender(True)} mouth to object, but {FriendC.gender(True)} decides against it.")
                    print(f"Wincing, {FriendC.gender(True)} covers his injured area.\n")
                    print("Has the pain worsened?\n")
                    print(f"As the thought crosses your mind, Anne suddenly shouts.\n")
                    print('"It was hidden away in this container this whole time..." She sheepishly remarks.\n')
                    print(f"Without wasting a moment, she rushes to treat {FriendC.name()}.")
                    print(f"After the treatment, {FriendC.name()} appears to look a little better.\n")
                    print(f'"Thanks, Anne." He raises, nursing his hand. "But I really think we should be moving now."')
                    print("To the distance, you hear some buzzing.")
                    print(f"{FriendC.name()} is right. Time to hightail out of here.\n")
                else:
                    Main_Character.moraldecrease()
                    print(f"{FriendC.name()} is right. The insect threat is too real.")
                    print("Hurrying, you convince your friends and Anne to run at full speed.")
                    print(f"While you are running, you hear loud panting from {FriendC.name()}")
                    print(f"You turn back to look at {FriendC.gender3(True)}\n")
                    print(f"{FriendC.name()} clutches {FriendC.gender2(True)} hand as {FriendC.gender(True)} grits his {FriendC.gender2(True)} teeth.")
                    print(f"Beads of sweats drop down {FriendC.gender2(True)} face rhymticaly, staining {FriendC.gender2(True)} shirt.")
                    print(f"No matter how you slice it, {FriendC.name()} looks worse for wear.\n")
                    print("Was the mosquite bite to blame?\n")
                    print(f"Whatever the case, {FriendC.name()} regains {FriendC.gender2(True)} composure seconds later.")
                    print("You can only hope for the best.\n")

                print("Two hours pass. You and your friends are finally free of the poisonous insects.")
                print("However, you find yourself stuck in a cave as you wait for the sudden downpour to pass.\n")
                print("Anne shuffles to you as you ponder on your trip so far.\n")
                print('"How about it?" She raises her hand. "Want to play a game of rock paper scissors to pass the time?"\n')
                print("Well, you do have nothing to do...\n")

                RPS()
                print("Some more time passes. The rain has stopped.")
                print("You and your friends are back on the trail, searching for an exit.\n")

                if Main_Character.moraltest():
                    print(f'"Hey isn\' that the exit!" {FriendA.name()} shouts.')
                    print(f"You gaze at {FriendA.name()}\'s direction.")
                    print("You see a faint road in the distance, filling you with relief.")
                    print("Cheers can be heard around you.\n")
                    print("Finally, the exit is within reach...\n")
                    print("Eventually, all of you reach the city safely.")
                    print('"I can\'t thank you guys enough!" Anne says as she departs.')
                    print("Neither can all of you.\n")
                    print("Thanks to Anne, you and your friends now know the importance of protecting the environment.")
                    print("Vowing to complete Anne\'s mission, you and your friends head back home, eager to reunite with your anxious parents...\n")
                    print("GOOD ENDING!")
                    if "ESCAPE ENDING" not in endinglist:
                        endinglist.append("ESCAPE ENDING")
                    break

                else:
                    print("You walk and walk, but each step takes you no closer to escape.")
                    print("Like lost lamb, you and your companions wander the forest, desperate for help.\n")
                    print("Of course, no help comes.\n")
                    print("One day passes, then another.\n")
                    print("You sigh as you glance at your dwindling supplies.")
                    print("Will you ever escape this forest?")
                    print("Was there something else you could have done? Did you ignore certain bits of advice?\n")
                    print("You can't remember.\n")
                    print("Despair sets in, shattering your optimism.\n")
                    print("Even Anne has lost her animated vigour.")
                    print(f"You never should have went on a hiking trip with {FriendA.name()}, {FriendB.name()} and {FriendC.name()} to begin with...\n")
                    print("LOST END...?")
                    if "LOST END" not in endinglist:
                        endinglist.append("LOST END")
                    break

        decision = choice(["Play again","Don't play"],"Do you want to play again? ")
        if decision == "2":
            return 

main()