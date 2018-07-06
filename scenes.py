import time, random, os
from game import *

class clearing:
    def __init__(self):
        self.near_water = False
        self.day_danger = 1
        self.night_danger = 3

    def __str__(self):
        return "You come to a clearing in the woods"

class lake:
    def __init__(self):
        self.near_water = True
        self.day_danger = 2
        self.night_danger = 4

    def __str__(self):
        return "You come across a small lake"


class woods:
    def __init__(self):
        self.near_water = False
        self.day_danger = 5
        self.night_danger = 8

    def __str__(self):
        return "You are standing in the middle of the woods"


class river:
    def __init__(self):
        self.near_water = True
        self.day_danger = 4
        self.night_danger = 7

    def __str__(self):
        return "You come to the bank of a river"


class cave:
    def __init__(self):
        self.near_water = False
        self.day_danger = 7
        self.night_danger = 10

    def __str__(self):
        return "You come to the entrance of a dark cave"

def clear_scene(player):
    os.system("clear")
    print("Your materials: ",player.materials,"\n",
          "Your food:",player.food,"\n","Your health:",player.health)

def handle_scavenge(time_l,player,game):
    x = random.randint(1,2*time_l)
    materials = list(player.materials.keys())
    for i in range(0,x):
        item = pick_item(player,materials)
        player.materials[item] += 1
        print("You found", item)
        time.sleep(.25)
    print("That's all you found!")
    time.sleep(1)
    clear_scene(player)

def pick_item(player, materials):
    item = "bows"
    while item == "bows" or item == "spears" or item == "arros":
        item = random.choice(materials)

    return item



def handle_hunt(time_l,player,game):
    x = random.randint(1,100)
    if game.scene == "clearing":
        if x <= 2:
            animal = "bear"
        elif x <= 10:
            animal = "boar"
        elif x <= 15:
            animal = "squirrel"
        elif x <= 25:
            animal = "rabbit"
        elif x <= 35:
            animal = "porcupine"
        elif x <= 60:
            animal = "turkey"
        else:
            animal = "deer"
    elif game.scene == "cave":
        if x <= 65:
            animal = "bear"
        elif x <= 75:
            animal = "boar"
        elif x <= 80:
            animal = "squirrel"
        elif x <= 85:
            animal = "rabbit"
        elif x <= 95:
            animal = "porcupine"
        elif x <= 99:
            animal = "turkey"
        else:
            animal = "deer"
    elif game.scene == "river":
        if x <=25:
            animal = "bear"
        elif x <= 40:
            animal = "boar"
        elif x <= 45:
            animal = "squirrel"
        elif x <= 55:
            animal = "rabbit"
        elif x <= 65:
            animal = "porcupine"
        elif x <= 70:
            animal = "turkey"
        else:
            animal = "deer"
    elif game.scene == "lake":
        if x <=25:
            animal = "bear"
        elif x <= 40:
            animal = "boar"
        elif x <= 45:
            animal = "squirrel"
        elif x <= 55:
            animal = "rabbit"
        elif x <= 65:
            animal = "porcupine"
        elif x <= 70:
            animal = "turkey"
        else:
            animal = "deer"
    elif game.scene == "woods":
                if x <=15:
                    animal = "bear"
                elif x <= 35:
                    animal = "boar"
                elif x <= 45:
                    animal = "squirrel"
                elif x <= 50:
                    animal = "rabbit"
                elif x <= 65:
                    animal = "porcupine"
                elif x <= 70:
                    animal = "turkey"
                else:
                    animal = "deer"
    print("You found a", animal, "would you like to hunt it? (y/n) ")
    will_hunt = input()
    if will_hunt.lower().startswith('y'):
        print("You decided to hunt the", animal)
        weapon = input("What weapon would you like to use? ")
        if weapon == "knife":
            if player.materials["knives"] < 1:
                print("Sorry, you don't have that weapon!")
            else:
                print("You used a knife to hunt the", animal)
                x = random.randint(0,100)
                if animal == "bear":
                    print("You stupidly attacked a bear with a knife...")
                    time.sleep(.5)
                    if x <= 40:
                        print(" Now you're dead...")
                        handle_lose(player)
                        player.health["energy"] = 0
                    elif x <= 90:
                        print("Luckily you made it out alive...")
                    else:
                        print("But somehow you managed to kill it!")
                        player.food["bear"] += 1
                elif animal == "squirrel" or animal == "rabbit":
                    print("You chased the", animal, "with your knife..")
                    time.sleep(.5)
                    if x <= 75:
                        print("You never even got close...")
                    else:
                        print("Somehow you were able to catch it!")
                        player.food[animal] += 1
                elif animal == "boar":
                    print("You attacked the boar with your knife...")
                    time.sleep(.5)
                    if x <= 5:
                        print("It fought back and managed to kill you!")
                        handle_lose(player)
                    elif x <= 55:
                        print("It outran you...")
                    else:
                        print("You caught it!")
                        player.food["boar"] += 1
                elif animal == "deer":
                    print("You chased the deer with your knife")
                    time.sleep(.5)
                    if x <= 2:
                        print("It kicked you in the temple and bashed your head in!")
                        handle_lost(player)
                    elif x <= 80:
                        print("You weren't fast enough to catch it...")
                    else:
                        print("You caught the deer!")
                        player.food["deer"] += 1


        elif weapon == "bow":
            print("Not yet supported")
        elif weapon == "spear":
            print("Not yet supported")
    else:
        print("You decided not to hunt the", animal)

    if time_l - 1 > 0:
        handle_hunt(time_l - 1, player, game)




def handle_fish(time_l,player,game):
    print("Fish")

def handle_walk(time_l,player,game):
    print("Walk")

def handle_sleep(time_l,player,game):
    print("Sleep")

def handle_build(time_l,player,game):
    print("Build")
