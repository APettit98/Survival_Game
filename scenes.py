import time, random, os, sys
from game import *
from player import *

# For all functions containing game or player parameters,
# game and player are the global variables for the game and player that are
# passed around to every function

# Scene classes, each containing values for how dangerous they are,
# whether or not they are near water, and a string output to be displayed
# when the user reaches that scene
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

# clears the scene by clearing screen and displaying materials, food, health,
# and time
def clear_scene(player, game):
    os.system("clear")
    print("Your materials: ")
    for element in player.materials.keys():
        if player.materials.get(element) > 0:
            print(element, player.materials[element])

    print("\nYour food: ")
    for element in player.food.keys():
        if player.food.get(element) > 0:
            print(element, player.food[element])
    if player.shelter["exists"]:
        print("\nYour shelter: ", player.shelter)

    print("Your health: ",player.health)
    print("Current time: ",game.time)

# Handles case where user decides to scavenge
# time_l is the length of time the user wants to scavenge
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
    clear_scene(player, game)

# Picks a random item to be picked up by the player
# ensures player doesn't pick up, bows, spears, or arrows
def pick_item(player, materials):
    item = "bows"
    while item == "bows" or item == "spears" or item == "arrows" or item == "fishing poles":
        item = random.choice(materials)

    return item


# Handles case where user decides to hunt
# time_l is amount of time user wants to hunt
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
    will_hunt = input().lower()
    if will_hunt.startswith('y'):
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
                        player.health["injury"] = 100
                        handle_lose(player)
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
                        player.health["injury"] = 100
                        handle_lose(player)
                    elif x <= 55:
                        print("It outran you...")
                    else:
                        print("You caught it!")
                        player.food["boar"] += 1
                elif animal == "porcupine":
                    print("You attacked the porcupine with your knife")
                    time.sleep(.5)
                    if x <= 50:
                        print("You scared it and it attacked you with its needles! Thats gotta hurt...")
                        player.health["injury"] += 20
                    elif x <= 70:
                        print("It scurried up a tree before you could get it...")
                    else:
                        print("You caught it!")
                        player.food["porcupine"] += 1
                elif animal == "turkey":
                    print("You attacked the turkey with your knife")
                    time.sleep(.5)
                    if x <= 60:
                        print("You scared it away...")
                    else:
                        print("You successfully caught the turkey!")
                        player.food["turkey"] += 1
                elif animal == "deer":
                    print("You chased the deer with your knife")
                    time.sleep(.5)
                    if x <= 2:
                        print("It kicked you in the temple and bashed your head in!")
                        player.health["injury"] = 100
                        handle_lose(player)
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
    else:
        time_up(game,time_l,player)
        clear_scene(player,game)



# Handles case where user wants to fish
def handle_fish(time_l,player,game):
    scene = game.scene
    if scene != 'lake' and scene != 'river':
        print("You can't fish here, there's no water!")
        clear_scene(player,game)
    if player.materials["fishing poles"] == 0:
        print("You don't have anything to fish with, you need to make a fishing pole first")
        time.sleep(2)
        clear_scene(player,game)
    else:
        num_fish = 0
        for i in range (0,time_l):
            x = random.randint(0,100)
            if x < 50:
                num_fish += 1

        print("You caught {} fish!".format(num_fish))
        player.food["fish"] += num_fish
        time_up(game,time_l,player)
        clear_scene(player,game)


# Handles case where user wants to walk somewhere else
def handle_walk(time_l,player,game):
    print("Which direction would you like to go?")
    answer = input().lower()
    if answer == "help":
        handle_help()
        handle_turn(game,player,False)
    elif answer == 'north' or answer.startswith("n"):
        length = time_l
        game.coordinates[1] += length
        if game.coordinates[1] > 100:
            print("Sorry you've reached the bounds of the game, you only walked",
                  length - (game.coordinates[1] - 100), "hours")
    elif answer == 'south' or answer.startswith("s"):
        length = time_l
        game.coordinates[1] -= length
        if game.coordinates[1] < -100:
            print("Sorry you've reached the bounds of the game, you only walked",
                  length + (game.coordinates[1] + 100), "hours")
    elif answer == 'east' or answer.startswith("e"):
        length = time_l
        game.coordinates[0] += length
        if game.coordinates[0] > 100:
            print("Sorry you've reached the bounds of the game, you only walked",
                  length - (game.coordinates[0] - 100), "hours")
    elif answer == 'west' or answer.startswith("w"):
        length = time_l
        game.coordinates[0] -= length
        if game.coordinates[0] < -100:
            print("Sorry you've reached the bounds of the game, you only walked",
                  length + (game.coordinates[1] + 100), "hours")
    else:
        print("That was not a valid direction, valid directions are 'north', 'south', 'east', and 'west'."
        " Please try again...")
        handle_walk(time_l,player,game)

    time_up(game,time_l,player)
    clear_scene(player, game)

# Gets danger values of current scene
def get_danger(game):
    scene = game.scene
    if scene == 'clearing':
        danger = [1,3]
    elif scene == 'lake':
        danger = [2,4]
    elif scene == 'woods':
        danger = [5,8]
    elif scene == 'river':
        danger = [4,7]
    elif scene == 'cave':
        danger = [7,10]
    return danger


# Handles case where user decides to sleep
# Adds energy and also allows for possibility of a bear attack in the night
def handle_sleep(time_l,player,game):
    danger = get_danger(game)
    energy = player.health["energy"]
    if game.time["hour"] < 6 or game.time["hour"] > 21:
        danger = danger[1]
    else:
        danger = danger[0]

    x = random.randint(0, 100)
    if x <= danger * 9:
        print("A bear came out of nowhere and attacked you!\n"
        "Quick! Roll right (r) or left (l), or pull out your knife (k)!")
        answer = input().lower()
        y = random.choice(['r','l'])
        if answer.lower().startswith(y) and not answer.lower().startswith('k'):
            print("Shew, you successfully rolled away")
            if player.shelter["exists"]:
                print("Unfortunately it damaged your shelter...")
                shelter_damage(player, 25)
        elif answer.lower().startswith('k'):
            if player.materials["knives"] > 0:
                print("You pulled out your knife in defense!")
                z = random.randint(0,100)
                if z <= 35:
                    print("You stabbed the bear as it attacked you and killed it!")
                    if player.shelter["exists"]:
                        print("Unfortunately it managed to damage your shelter...")
                        shelter_damage(player, 20)
                    player.food["bear"] += 1
                elif z <= 70:
                    print("You stabbed the bear as it attacked you and it ran away, "
                    "but not after it gave you a few nasty cuts...")
                    if player.shelter["exists"]:
                        print("Unfortunately it managed to damage your shelter...")
                        shelter_damage(player, 20)
                    player.health["injury"] += 20
                else:
                    print("You attempted to stab the bear but you could't get to your knife "
                    "quickly enough!")
                    player.health["injury"] = 100
                    handle_lose(player)
            else:
                print("You reached for your knife, but you don't have one! "
                "Should've run while you had the chance...")
                player.health["injury"] = 100
                handle_lose(player)
        else:
            print("Unfortunately you rolled straight into the bear's swiping paw...")
            player.health["injury"] = 100
            handle_lose(player)

    energy += 5 * time_l + (2 * player.shelter["comfort"])
    if energy > 100:
        energy = 100

    print("You got", time_l, "hours of sleep")
    time.sleep(2)
    time_up(game, time_l,player)
    player.health["energy"] = energy
    clear_scene(player, game)



# Called when shelter is damaged
def shelter_damage(player, amount):
    shelter = player.shelter
    player.shelter["stability"] -= amount
    player.shelter["comfort"] -= amount
    if player.shelter["stability"] <= 0:
        player.shelter["exists"] = False
        player.shelter["stability"] = 0
        player.shelter["comfort"] = 0
    elif player.shelter["comfort"] < 0:
        player.shelter["comfort"] = 0




# Handles case where user decides to build
# Only shelter and bows implemented so far
def handle_build(player,game):
    print("What would you like to build?")
    answer = input().lower()
    if answer == "shelter":
        if player.materials["logs"] < 3:
            print("You dont have enough wood to make a shelter")
            time.sleep(2)
            clear_scene(player,game)
        else:
            time_spent = 0
            print("How many logs would you like to use?")
            logs = int(input())
            if logs > player.materials["logs"]:
                logs = player.materials["logs"]
                print("You didn't have that many logs so you added {} logs".format(logs))
            print("You added {} logs to your shelter".format(logs))
            time_spent += 0.25 * logs
            player.materials["logs"] -= logs
            player.shelter["stability"] += logs * 2
            player.shelter["exists"] = True
            player.shelter["comfort"] += logs // 2
        if player.materials["rope"] > 0:
            print("How much rope would you like to use?")
            rope = int(input())
            if rope > player.materials["rope"]:
                rope = player.materials["rope"]
                print("You didn't have that much rope so you only added {}".format(rope))
            print("You added {} rope to your shelter".format(rope))
            time_spent += 0.25 * rope
            player.materials["rope"] -= rope
            player.shelter["stability"] += rope
        if player.materials["moss"] > 0:
            print("How much moss would you like to add?")
            moss = int(input())
            if moss > player.materials["moss"]:
                moss = player.materials["moss"]
                print("You didn't have that much moss so you only added {}".format(moss))
            print("You added {} moss to your shelter".format(moss))
            time_spent += .25 * moss
            player.materials["moss"] -= moss
            player.shelter["comfort"] += moss * 2
        print("You built a shelter with {} stability and {} comfort".format(player.shelter["stability"], player.shelter["comfort"]))
        time_up(game,int(time_spent,10),player)
        print("It took you {} hours to build".format(int(time_spent, 10)))
        time.sleep(2)
        clear_scene(player,game)

    elif answer == "bow":
        if player.materials["string"] < 1 or player.materials["sticks"] < 1:
            print("You don't have enough materials to make a bow")
            time.sleep(2)
            clear_scene(player,game)
        else:
            player.materials["string"] -= 1
            player.materials["sticks"] -= 1
            player.materials["bows"] += 1
            print("You made a bow! It took you 4 hours")
            time_up(game, 4, player)
            time.sleep(2)
            clear_scene(player,game)

    elif answer == "arrow":
        if player.materials["sticks"] < 1 or player.materials["sharp rocks"] < 1:
            print("You don't have enough materials to make an arrow")
            time.sleep(2)
            clear_scene(player,game)
        else:
            player.materials["sticks"] -= 1
            player.materials["sharp rocks"] -= 1
            player.materials["arrows"] += 1
            print("You made an arrow! It took you 1 hour")
            time_up(game,1,player)
            time.sleep(2)
            clear_scene(player,game)

    elif answer == "spear":
        if player.materials["sticks"] < 1 or player.materials["sharp rocks"] < 1 and player.materials["knives"] < 1 or player.materials["rope"] < 1:
            print("You don't have enough materials to make a spear")
            time.sleep(2)
            clear_scene(player,game)
        else:
            if player.materials["knives"] > 0 and player.materials["sharp rocks"] > 0:
                print("Would you like to use a knife or a sharp rock?")
                answer = input().lower()
                if answer.startswith('k'):
                    print("You made a spear using a knife!")
                    player.materials["knives"] -= 1
                else:
                    print("You made a spear using a sharp rock!")
                    player.materials["sharp rocks"] -= 1
            elif player.materials["knives"] > 0:
                print("You made a spear using a knife!")
                player.materials["knives"] -= 1
            else:
                print("You made a spear using a sharp rock!")
                player.materials["sharp rocks"] -= 1

            player.materials["sticks"] -= 1
            player.materials["rope"] -= 1
            player.materials["spears"] += 1
            print("It took you 2 hours")
            time_up(game, 2, player)
            time.sleep(2)
            clear_scene(player,game)


    else:
        print("That is not someething you can build...try again")
        hanlde_help()
        handle_build(time-l, player,game)
