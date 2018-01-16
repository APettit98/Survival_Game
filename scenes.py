import time, random, os

class clearing:
    def __init__(self):
        self.near_water = False
        self.day_danger = 1
        self.night_danger = 3

    def __str__(self):
        str = "You come to a clearing in the woods"
        return str

class lake:
    def __init__(self):
        self.near_water = True
        self.day_danger = 2
        self.night_danger = 4

    def __str__(self):
        str = "You come across a small lake"
        return str


class woods:
    def __init__(self):
        self.near_water = False
        self.day_danger = 5
        self.night_danger = 8

    def __str__(self):
        str = "You are standing in the middle of the woods"
        return str


class river:
    def __init__(self):
        self.near_water = True
        self.day_danger = 4
        self.night_danger = 7

    def __str__(self):
        str = "You come to the bank of a river"
        return str


class cave:
    def __init__(self):
        self.near_water = False
        self.day_danger = 7
        self.night_danger = 10

    def __str__(self):
        str = "You come to the entrance of a dark cave"
        return str

def handle_scavenge(time_l,player):
    x = random.randint(1,2*time_l)
    materials = list(player.materials.keys())
    for i in range(0,x):
        item = random.choice(materials)
        player.materials[item] += 1
        print("You found", item)
        time.sleep(.25)
    print("That's all you found!")
    time.sleep(1)
    os.system("clear")
    print("Your materials: ",player.materials,"\n",
          "Your food:",player.food,"\n","Your health:",player.health)


def handle_hunt(time):
    print("Hunt")

def handle_fish(time):
    print("Fish")

def handle_walk(time):
    print("Walk")

def handle_sleep(time):
    print("Sleep")

def handle_build(time):
    print("Build")
