import time
import pygame
import random


pygame.mixer.init(44100, -16, 2, 2048)

intro_song = pygame.mixer.Sound('03 Start of the Journey.wav')
intro_song.set_volume(0.35)

failure_song = pygame.mixer.Sound('49 Grief.wav')
failure_song.set_volume(0.35)

transition_song = pygame.mixer.Sound("05 Light Slumber.wav")
transition_song.set_volume(0.35)

town_music = pygame.mixer.Sound("04 Town.wav")
town_music.set_volume(0.35)

tavern_music = pygame.mixer.Sound("20 Capsule Monster.wav")
tavern_music.set_volume(0.35)

battle_music_one = pygame.mixer.Sound("08 Battle #1.wav")
battle_music_one.set_volume(0.35)

battle_music_two = pygame.mixer.Sound("16 Battle #2.wav")
battle_music_two.set_volume(0.35)

battle_music_three = pygame.mixer.Sound("48 Battle #3.wav")
battle_music_three.set_volume(0.35)

battle_music_victory = pygame.mixer.Sound("09 Triumph.wav")
battle_music_victory.set_volume(0.35)

sad_music = pygame.mixer.Sound("26 Parting.wav")
sad_music.set_volume(0.35)

timeShort = 0
timeLong = 0
timeVeryLong = 0


class BigDestiny():
    def __init__(self, bigDHP=8, bigDDam=2, bigDAttack="Big D' pierces with his Rapier", bigDTrust=False,
                 bigDName="Big D'"):
        self.bigDHP = bigDHP
        self.bigDDam = bigDDam
        self.bigDAttack = bigDAttack
        self.bigDTrust = bigDTrust
        self.bigDName = bigDName


class Town():
    def __init__(self, magicCookie=False, angryBaker=False, fountainEvent=False, tavernEvent=False,
                 beerDrink=False, hardDrink=False, magicElixir=False, angryBarTender=False):
        self.magicCookie = magicCookie
        self.angryBaker = angryBaker
        self.fountainEvent = fountainEvent
        self.tavernEvent = tavernEvent
        self.beerDrink = beerDrink
        self.hardDrink = hardDrink
        self.magicElixir = magicElixir
        self.angryBarTender = angryBarTender


class Hero():
    def __init__(self, heroName="matt", currentHP=2, currentDam=2, weapCrit=2, weapName="test", weapAttack="test",
                 weapCritAttack="test", ageName="test", className="test", fitName="test"):
        self.heroName = heroName
        self.currentHP = currentHP
        self.currentDam = currentDam
        self.weapCrit = weapCrit
        self.weapName = weapName
        self.weapAttack = weapAttack
        self.weapCritAttack = weapCritAttack
        self.ageName = ageName
        self.className = className
        self.fitName = fitName


class Combat():
    def __init__(self, heroHP=0, heroDam=0, heroCritDam=0, heroAttack="Test", heroCritAttack="Test",
                 enemyHP=0, enemyDam=0, enemyAttack="Test", heroName="Test", enemyName="Test", fighting=False):
        self.heroHP = heroHP
        self.heroDam = heroDam
        self.heroCritDam = heroCritDam
        self.heroAttack = heroAttack
        self.heroCritAttack = heroCritAttack
        self.heroName = heroName
        self.enemyName = enemyName
        self.enemyHP = enemyHP
        self.enemyDam = enemyDam
        self.enemyAttack = enemyAttack
        self.fighting = fighting

    def battle(self):
        while self.fighting:
            if theHero.currentHP >= 0 and self.enemyHP >= 0:
                if random.randrange(0, 6) == 0:
                    print("Attack                   select # 1")
                    print("Critical Attack          select # 2")
                    answer = input()
                    if answer == "1":
                        print(f"{theHero.heroName} attacks, {theHero.weapAttack}, {theHero.currentDam} damage was done")
                        self.enemyHP = self.enemyHP - theHero.currentDam
                        print(f"{self.enemyName}s current HP: {self.enemyHP}\n")
                        print(f"{self.enemyName} attacks, {self.enemyAttack}, {self.enemyDam} damage was done")
                        theHero.currentHP = theHero.currentHP - self.enemyDam
                        print(f"{theHero.heroName} current HP: {theHero.currentHP}\n")
                    elif answer == "2":
                        print(
                            f"{theHero.heroName} attacks, {theHero.weapCritAttack}, {theHero.weapCrit} damage was done")
                        self.enemyHP = self.enemyHP - theHero.weapCrit
                        print(f"{self.enemyName}s current HP: {self.enemyHP}\n")
                        print(f"{self.enemyName} attacks, {self.enemyAttack}, {self.enemyDam} damage was done")
                        theHero.currentHP = theHero.currentHP - self.enemyDam
                        print(f"{theHero.heroName} current HP: {theHero.currentHP}\n")
                    else:
                        print("Attack missed")
                        print(f"{self.enemyName} attacks, {self.enemyAttack}, {self.enemyDam} damage was done")
                        theHero.currentHP = theHero.currentHP - self.enemyDam
                        print(f"{theHero.heroName} current HP: {theHero.currentHP}\n")
                else:
                    print("Attack                   select # 1")
                    answer = input()
                    if answer == "1":
                        print(f"{theHero.heroName} attacks, {theHero.weapAttack}, {theHero.currentDam} damage was done")
                        self.enemyHP = self.enemyHP - theHero.currentDam
                        print(f"{self.enemyName}s current HP: {self.enemyHP}\n")
                        print(f"{self.enemyName} attacks, {self.enemyAttack}, {self.enemyDam} damage was done")
                        theHero.currentHP = theHero.currentHP - self.enemyDam
                        print(f"{theHero.heroName} current HP: {theHero.currentHP}\n")
                    else:
                        print("Attack missed")
                        print(f"{self.enemyName} attacks, {self.enemyAttack}, {self.enemyDam} damage was done")
                        theHero.currentHP = theHero.currentHP - self.enemyDam
                        print(f"{theHero.heroName} current HP: {theHero.currentHP}\n")
            elif theHero.currentHP <= 1:
                print(f"{theHero.heroName} failed in his fight against Big Destiny\n")
                gameOver()
            elif self.enemyHP <= 1:
                battle_music_two.stop()
                battle_music_victory.play(loops=-1)
                time.sleep(timeShort)
                self.fighting = False


class Inventory():
    def __init__(self, magicCookie=False, magicElixir=False, checkingItems=False):
        self.magicCookie = magicCookie
        self.magicElixir = magicElixir
        self.checkingItems = checkingItems

    def use(self):
        while self.checkingItems:
            if self.magicCookie and self.magicElixir:
                pass
            elif self.magicCookie and self.magicElixir is False:
                pass
            elif self.magicCookie is False and self.magicElixir:
                pass
            else:
                pass


townPlace = Town()
theHero = Hero()
bigDestinyFight = BigDestiny()
theCombat = Combat()
useItem = Inventory()


def gameOver():
    intro_song.stop()
    town_music.stop()
    failure_song.stop()
    battle_music_two.stop()
    failure_song.play(loops=-1)
    print(f"\n I do not remember the story ending for {theHero.heroName} that way or maybe it did.")
    print(" Continue where at the last event?         Select #1")
    print(" Start from the beginning?                 Select #2")
    print(" Stop the story and give up?               Select #3 \n")
    answer = input("")
    if "1" in answer:
        storyPT1_Town()
        # take off on the last save
    elif "2" in answer:
        townPlace.angryBaker = False
        townPlace.magicCookie = False
        townPlace.tavernEvent = False
        townPlace.angryBarTender = False
        townPlace.magicElixir = False
        townPlace.fountainEvent = False
        townPlace.beerDrink = False
        townPlace.hardDrink = False
        bigDestinyFight.bigDTrust = False
        startGame()
    elif "3" in answer:
        quit()
    else:
        gameOver()


def startGame():
    intro_song.stop()
    failure_song.stop()
    intro_song.play(loops=-1)
    print("Welcome travel. Sit down and let me tell you a story, the story of the champion ... \n")
    theHero.heroName = input("")
    print(f"Awe yes the great hero {theHero.heroName} and his great triumph over the Green Lean Ugly Machine")
    time.sleep(timeShort)
    beginningPT2_AGE()


def beginningPT2_AGE():
    print(f"Tell me a little bit about {theHero.heroName} let's start with how he looks")
    print("The shoes can tell you a lot about a person, how much they make, and where they have been. \n")
    time.sleep(timeLong)
    print("did they look like baby shoes          (select # 1)")
    print("did his shoes look like new shoes      (select # 2)")
    print("were they running shoes                (select # 3)")
    print("did they look like fancy shoes         (select # 4)")
    print("did his shoes look like terribly old   (select # 5)\n")
    answer = input()
    if answer == "1":
        print("Awe yes that's right, they were baby shoes \n")
        theHero.currentHP = 5
        theHero.currentDam = 1
        theHero.ageName = "Baby"
    elif answer == "2":
        print("Awe yes that's right, they were new shoes \n")
        theHero.currentHP = 6
        theHero.currentDam = 4
        theHero.ageName = "Young"
    elif answer == "3":
        print("Awe yes that's right, they were running shoes \n")
        theHero.currentHP = 7
        theHero.currentDam = 3
        theHero.ageName = "Late 20's"
    elif answer == "4":
        print("Awe yes that's right, they were fancy shoes \n")
        theHero.currentHP = 9
        theHero.currentDam = 2
        theHero.ageName = "Seasoned"
    elif answer == "5":
        print("Awe yes that's right, they were old shoes \n")
        theHero.currentHP = 6
        theHero.currentDam = 1
        theHero.ageName = "Old"
    else:
        print("That choice was not given, Please try again \n")
        time.sleep(timeShort)
        beginningPT2_AGE()
    time.sleep(timeShort)
    beginningPT3_FIT()


def beginningPT3_FIT():
    print(f"Tell me more about {theHero.heroName} what activities did he do in his free time?")
    print("What a person does when no one is watching defines us as people.\n")
    time.sleep(timeLong)
    print("Did they play a lot with numbers, moving 1s and 0s?      (select # 1)")
    print("Were they in the habit of practicing for battle often?   (select # 2)")
    print("Did they get into too many deadly duels?                 (select # 3)")
    print("Were they exercising every now and then?                 (select # 4)")
    print("Were games like jousting and such, played often?         (select # 5)\n")
    answer = input()
    if answer == "1":
        print("Awe yes that's right, they were playing with number in their free time.\n")
        theHero.currentHP += 5
        theHero.currentDam += 1
        theHero.fitName = "Unfit"
    elif answer == "2":
        print("Awe yes that's right, they were practicing for battle in their free time.\n")
        theHero.currentHP += 8
        theHero.currentDam += 3
        theHero.fitName = "Above Average"
    elif answer == "3":
        print("Awe yes that's right, they were getting into duels in their free time.\n")
        theHero.currentHP += 9
        theHero.currentDam += 4
        theHero.fitName = "Very Fit"
    elif answer == "4":
        print("Awe yes that's right, they were exercising in their free time.\n")
        theHero.currentHP += 7
        theHero.currentDam += 2
        theHero.fitName = "Average"
    elif answer == "5":
        print("Awe yes that's right, they were playing games in their free time. \n")
        theHero.currentHP += 6
        theHero.currentDam += 1
        theHero.fitName = "Below Average"
    else:
        print("That choice was not given, Please try again \n")
        time.sleep(timeShort)
        beginningPT3_FIT()
    time.sleep(timeShort)
    beginningPT4_CLASS()


def beginningPT4_CLASS():
    print(f"Oh yes, we're getting a much better picture of {theHero.heroName} but there is one more thing.")
    print("How were their dietary habits, what really filled their belly \n")
    time.sleep(timeLong)
    print("Did they prefer stolen food?                             (select # 1)")
    print("Were they in the habit of eating only Kosher food?       (select # 2)")
    print("Did they only eat raw meat?                              (select # 3)")
    print("Was their food of a foreign variety                      (select # 4)")
    print("Were they in normally eating a well balanced meal?       (select # 5)\n")
    answer = input()
    if answer == "1":
        print("Awe yes that's right, they would eat food that did not belong to them.\n")
        theHero.currentHP += 5
        theHero.currentDam += 1
        theHero.className = "Thief"
    elif answer == "2":
        print("Awe yes that's right, they would eat Kosher meals.\n")
        theHero.currentHP += 9
        theHero.currentDam += 2
        theHero.className = "Paladin"
    elif answer == "3":
        print("Awe yes that's right, they would eat raw meat.\n")
        theHero.currentHP += 8
        theHero.currentDam += 3
        theHero.className = "Beastman"
    elif answer == "4":
        print("Awe yes that's right, they would only eat foreign food.\n")
        theHero.currentHP += 7
        theHero.currentDam += 3
        theHero.className = "Warrior"
    elif answer == "5":
        print("Awe yes that's right, they would eat well balanced meals \n")
        theHero.currentHP += 8
        theHero.currentDam += 2
        theHero.className = "Knight"
    else:
        print("That choice was not given, Please try again \n")
        time.sleep(timeShort)
        beginningPT4_CLASS()
    print(
        f"Awe yes I remember now the {theHero.fitName}, {theHero.ageName}, {theHero.className}, {theHero.heroName}!\n")
    beginningPT5_WEAP()


def beginningPT5_WEAP():
    time.sleep(timeLong)
    print("Now that we know a good bit about the hero, what was their choice of weapon?\n")
    time.sleep(timeShort)
    print("Did they prefer a good old fashion Sword?                (select # 1)")
    print("Have they a fancy for a Battle Axe?                      (select # 2)")
    print("Were they normally in the mood for Long Range?           (select # 3)")
    print("Would they get up close and personal with Daggers?       (select # 4)")
    print("Would they fight at a range with a Long Spear?           (select # 5)")
    print("Did they fight like a wild thing, with tooth and claw?   (select # 6)\n")
    answer = input()
    if answer == "1":
        print("Awe yes that's right, they would fight with a Sword.\n")
        theHero.currentDam += 3
        theHero.weapCrit = theHero.currentDam * 2
        theHero.weapName = "Sword"
        theHero.weapAttack = "The Sword Slashes!"
        theHero.weapCritAttack = "A Tremendous Blow!"
    elif answer == "2":
        print("Awe yes that's right, they would fight with a Battle Axe.\n")
        theHero.currentDam += 3
        theHero.weapCrit = theHero.currentDam * 3
        theHero.weapName = "Battle Axe"
        theHero.weapAttack = "The Axe Cleaves!"
        theHero.weapCritAttack = "An Annihilating Strike!"
    elif answer == "3":
        print("Awe yes that's right, they would fight with a Bow.\n")
        theHero.currentDam += 2
        theHero.weapCrit = theHero.currentDam * 2
        theHero.weapName = "Bow"
        theHero.weapAttack = "The Bow Twangs and an Arrow Flies!"
        theHero.weapCritAttack = "A Powerful Shot!"
    elif answer == "4":
        print("Awe yes that's right, they would fight with a Daggers.\n")
        theHero.currentDam += 2
        theHero.weapCrit = theHero.currentDam * 3
        theHero.weapName = "Daggers"
        theHero.weapAttack = "The Daggers Cuts Deep!"
        theHero.weapCritAttack = "A Stab to a Vital spot!"
    elif answer == "5":
        print("Awe yes that's right, they would fight with a Long Spear.\n")
        theHero.currentDam += 2
        theHero.weapCrit = theHero.currentDam * 3
        theHero.weapName = "Long Spear"
        theHero.weapAttack = "The Spear Pierces!"
        theHero.weapCritAttack = "A Deadly Spinning Thrust!"
    elif answer == "6":
        print("Awe yes that's right, they would fight with a Claws.\n")
        theHero.currentDam += 3
        theHero.weapCrit = theHero.currentDam * 3
        theHero.weapName = "Claws"
        theHero.weapAttack = "The Claws Tear the Flesh!"
        theHero.weapCritAttack = "A Thunderous Ripping"
    else:
        print("That choice was not given, Please try again \n")
        time.sleep(timeShort)
        beginningPT5_WEAP()

    print(f"Now that we have a good picture of the hero {theHero.heroName} who fought with his {theHero.weapName}!\n")
    print(
        f"Current HP = {theHero.currentHP}, Current Dam = {theHero.currentDam}, current crit dam = {theHero.weapCrit}")
    time.sleep(timeShort)
    print("Well lets get on with the story!\n\n")
    intro_song.stop()
    transition_song.play(loops=-1)
    time.sleep(timeLong)
    storyPT1_Town()


def storyPT1_Town():
    transition_song.stop()
    town_music.stop()
    town_music.play(loops=-1)
    print(f"{theHero.heroName.upper()}! {theHero.heroName.upper()}! Where have you Been? I have been cleaning up "
          "for ages, \n and we have guests in a few hours! Go to the Store and pick up a few things for me please!\n "
          "Your aunt Merkle and grandpa Biedon are coming over so you will need to get that BLUEBERRY PIE!\n")
    time.sleep(timeVeryLong)
    print(f"{theHero.heroName} went on their way to the store to pick up groceries and a BLUEBERRY PIE")
    print(f"After not too long {theHero.heroName} finished picking up what they needed and \n"
          "made their way to the bakery.\n")
    storyPT2_Pie()


def storyPT2_Pie():
    time.sleep(timeLong)
    print(f"You there! why isn't that {theHero.heroName} what can i get you me'fellow?")
    answer = input("#Tell the baker what you want:   \n\n")
    answer = answer.upper()
    if "BLUE" in answer:
        print("Awe yes me'fellow, here you are, that'll' be 2 copper pieces.\n")
        storyPT3_PiePT2()
    else:
        print("The baker did not understand the request, please try again\n")
        storyPT2_Pie()


def storyPT3_PiePT2():
    time.sleep(timeShort)
    print(f"{theHero.heroName} reached into his coin purse and pulled out\n")
    print("2 copper pieces                        (select # 1)")
    print("3 copper pieces, 'for your troubles'   (select # 2)")
    print("1 silver piece, 'for your troubles'    (select # 3)")
    print("Nothing *runs away with the pie!*      (select # 4)\n")
    answer = input()
    if answer == "1":
        print("Thank you, have a great day!\n")
    elif answer == "2":
        print("Thank you, and a tip no less! have a bless'ed day\n!")
    elif answer == "3":
        print(f"Whats this {theHero.heroName}? oh my what a mighty gesture THANK YOU!")
        print("Here take this magic cookie with you, it could come in handy!\n")
        townPlace.magicCookie = True
    elif answer == "4":
        print(f"Hey you get back here {theHero.heroName.upper()} You Thief!\n")
        townPlace.angryBaker = True
    else:
        print("That does not seem to be an option, please try again\n")
        storyPT3_PiePT2()
    storyPT4_theChoice()


def storyPT4_theChoice():
    tavern_music.stop()
    town_music.stop()
    battle_music_victory.stop()
    sad_music.stop()
    town_music.play()
    time.sleep(timeShort)
    print(f"{theHero.heroName} decided to go to...")
    print("Go to the Tavern         select # 1")
    print("Go to the fountain       select # 2")
    print("Go home                  select # 3\n")
    answer = input()
    if answer == "1":
        if townPlace.tavernEvent:
            print(f"{theHero.heroName} has already been there, please try again\n")
            storyPT4_theChoice()
        else:
            print(f"{theHero.heroName} decided to go to the Tavern\n")
            townPlace.tavernEvent = True
            storyPT5_theTavern()
    elif answer == "2":
        if townPlace.fountainEvent:
            print(f"{theHero.heroName} has already been there, please try again\n")
            storyPT4_theChoice()
        else:
            print(f"{theHero.heroName} decided to go to the Fountain\n")
            townPlace.fountainEvent = True
            storyPT6_theFountain()
    elif answer == "3":
        print(f"{theHero.heroName} decided to go Home\n")
        storyPT7_Home()
    else:
        print("That does not seem to be an option, please try again\n")
        storyPT4_theChoice()


def storyPT5_theTavern():
    town_music.stop()
    tavern_music.stop()
    battle_music_victory.stop()
    tavern_music.play(loops=-1)
    time.sleep(timeShort)
    if townPlace.hardDrink and townPlace.beerDrink:
        storyPT5_theTavern_PT2()
    else:
        print("Have a drink 'Beer'          select # 1")
        print("Have a drink 'Hard Alcohol'  select # 2")
        print("Leave                        select # 3\n")
        answer = input()
        if answer == "1":
            townPlace.beerDrink = True
            print("You have a nice refreshing pint of beer!\n")
            storyPT5_theTavern()
        elif answer == "2":
            townPlace.hardDrink = True
            print("You feel the heat in your stomach of a hard spirit\n")
            storyPT5_theTavern()
        elif answer == "3":
            storyPT4_theChoice()
        else:
            print("That does not seem to be an option, please try again\n")
            storyPT5_theTavern()


def storyPT5_theTavern_PT2():
    time.sleep(timeShort)
    print("*Big Destiny walks in with his two of his cronies*")
    print("Hey bar keeps, we are here for our protection money!")
    print("Crony: 'You better pay up before things get broken'\n")
    print("Talk to Big Destiny              select # 1")
    print("Fight Big Destiny                select # 2")
    print("Do not get involved  *leaves*    select # 3\n")
    answer = input()
    if answer == "1":
        storyPT5_theTavern_PT3talk()
    elif answer == "2":
        storyPT5_theTavern_PT4fight()
    elif answer == "3":
        townPlace.angryBarTender = True
        storyPT4_theChoice()
    else:
        print("That does not seem to be an option, please try again\n")
        storyPT5_theTavern_PT2()


def storyPT5_theTavern_PT3talk():
    time.sleep(timeShort)
    print("'You won't be taking anything while I'm around!      select # 1")
    print("'Why are you doing this?'                            select # 2")
    print("'You are the lowest scum of the earth!'              select # 3")
    print("'Can I join your gang?'                              select # 4\n")
    answer = input()
    if answer == "1":
        print("Big D: Then you will die where you stand!\n")
        storyPT5_theTavern_PT4fight()
    elif answer == "2":
        storyPT5_theTavern_PT3talk_PT2()
    elif answer == "3":
        print("Big D: You think your so big? Then you will not leave here alive!\n")
        storyPT5_theTavern_PT4fight()
    elif answer == "4":
        townPlace.angryBarTender = True
        if theHero.currentDam >= 8:
            print("Prove to me your POWER and you can join!")
            print("Arm wrestle with Big Destiny to prove your POWER\n")
            answer = input()
            answer = answer.upper()
            if answer == "POW":
                bigDestinyFight.bigDTrust = True
                print("Yes you are quite powerful and can join my gang")
                print(f"{theHero.heroName} leaves the tavern\n")
                storyPT4_theChoice()
            else:
                print("You are not strong enough! Get out of here!\n")
                storyPT4_theChoice()
        else:
            print("No your too weak! Get out of here!\n")
            storyPT4_theChoice()
    else:
        print("That does not seem to be an option, please try again\n")
        storyPT5_theTavern_PT3talk()


def storyPT5_theTavern_PT3talk_PT2():
    print("Big D: Why you ask? I just like this SORT of thing")
    print("I am powerful and have it all!")
    print("You are sick!                                        select # 1")
    print("You should get out of here before you get hurt!      select # 2")
    print("Sounds fun. Can I join you?                          select # 3\n")
    answer = input()
    answer = answer.upper()
    if answer == "1":
        print("Big D: I may be sick but you are a dead man!")
        storyPT5_theTavern_PT4fight()
    elif answer == "2":
        print("Big D: I may get hurt? Well then bring it on!")
        storyPT5_theTavern_PT4fight()
    elif answer == "3":
        townPlace.angryBarTender = True
        if theHero.currentDam >= 8:
            print("Prove to me your POWER and you can join!")
            print("Arm wrestle with Big Destiny to prove your POWER\n")
            answer = input()
            answer = answer.upper()
            if answer == "POW":
                bigDestinyFight.bigDTrust = True
                print("Yes you are quite powerful and can join my gang")
                print(f"{theHero.heroName} leaves the tavern\n")
                storyPT4_theChoice()
            else:
                print("You are not strong enough! Get out of here!\n")
                storyPT4_theChoice()
    elif answer == "SORT":
        storyPT5_theTavern_PT3talk_PT3()
    else:
        print("That does not seem to be an option, please try again\n")
        storyPT5_theTavern_PT3talk_PT2()


def storyPT5_theTavern_PT3talk_PT3():
    tavern_music.stop()
    sad_music.stop()
    sad_music.play(loops=-1)
    print("Big D: What you see through my bravado?")
    print("I didn't always live a life of crime...")
    print("My daughter has a very rare and deadly illness")
    print("We only have a few more months until she dies. Unless I can get the money for treatment")
    print("So I have been using my boys to mash up the town to get money out of them, but I don't want to\n")
    time.sleep(timeVeryLong)
    print("Now I have turned to the life of crime, if I do get the money, what will she THINK of me...\n\n")
    print("Big D, this is no way to help your daughter, turn yourself in to the authorities     select # 1")
    print("Take pity on Big D and give him 1 gold coin (worth 1000 copper pieces)               select # 2")
    print("*Cut down Big D and the Destiny Gang*                                                select # 3\n")
    answer = input()
    answer = answer.upper()
    if answer == "1":
        print("Big D: Maybe your right, I have caused too much pain in this world, my daughter would never forgive me")
        print("*The Destiny gang leaves to turn themselves in remorseful*\n")
        time.sleep(timeLong)
        storyPT4_theChoice()
    elif answer == "2":
        print("This is insane you are giving me all this money?!")
        print(f"With this I can pay for my daughter's treatment! Thank you {theHero.heroName}!")
        print("*Big Destiny and the Destiny gang leave*")
        bigDestinyFight.bigDTrust = True
        time.sleep(timeLong)
        storyPT4_theChoice()
    elif answer == "3":
        print(f"{theHero.heroName} defeated Big Destiny and his cronies")
        print(f"Bar Tender: {theHero.heroName} you have saved us from the tyranny of Big Destiny")
        print("Please take this magic elixir with you ")
        townPlace.magicElixir = True
        print(f"{theHero.heroName} left the tavern triumphantly\n")
        time.sleep(timeLong)
        storyPT4_theChoice()
    elif answer == "THINK":
        storyPT5_theTavern_PT3talk_PT4()
    else:
        print("That does not seem to be an option, please try again\n")
        storyPT5_theTavern_PT3talk_PT3()


def storyPT5_theTavern_PT3talk_PT4():
    print("There is always another way, have you heard of the traveling doctor located in DunWitch?\n"
          "He will help you for free, his name is Jonas him and his team the Jonas Brothers will help you!\n"
          "                                                                                     select # 1")
    print("Head to the Jonas Brothers after you return the money back to the town's folk        select # 2\n")
    answer = input()
    if answer == "1":
        print(f"Thank you {theHero.heroName}, we will make our way out to the Jonas Brothers")
        print("Big D and the Destiny gang leave\n")
        bigDestinyFight.bigDTrust = True
        storyPT4_theChoice()
    elif answer == "2":
        print(f"Thank you {theHero.heroName}, we will make our way out to the Jonas Brothers")
        print("Big D and the Destiny gang leave\n")
        bigDestinyFight.bigDTrust = True
        print(f"Bar Tender: {theHero.heroName} you have saved us from the tyranny of Big Destiny")
        print("Please take this magic elixir with you ")
        townPlace.magicElixir = True
        print(f"{theHero.heroName} left the tavern triumphantly\n")
        time.sleep(timeLong)
        storyPT4_theChoice()
    else:
        print("That does not seem to be an option, please try again\n")
        storyPT5_theTavern_PT3talk_PT4()


def storyPT5_theTavern_PT4fight():
    tavern_music.stop()
    battle_music_two.play(loops=-1)
    theCombat.enemyName = bigDestinyFight.bigDName
    theCombat.enemyHP = bigDestinyFight.bigDHP
    theCombat.enemyDam = bigDestinyFight.bigDDam
    theCombat.enemyAttack = bigDestinyFight.bigDAttack
    time.sleep(timeShort)
    theCombat.fighting = True
    theCombat.battle()
    print(f"{theHero.heroName} defeated Big Destiny and his cronies run away")
    print(f"{theHero.heroName} you have saved us from the tyranny of Big Destiny")
    print("Please take this magic elixir with you ")
    townPlace.magicElixir = True
    print(f"{theHero.heroName} left the tavern triumphantly\n")
    time.sleep(timeLong)
    storyPT4_theChoice()


def storyPT6_theFountain():
    pass


def storyPT7_Home():
    pass


startGame()
