import random, os
from scenes import *

scene_options = ["cave", "river", "lake", "woods", "clearing"]

class game:
    def __init__(self):
        self.coordinates = [0,0]
        self.winning_coordinates = []
        self.time = {"hours":0, "days":0}
        i = 0
        for i in range(0,101):
            new_x = random.randint(-100,100)
            new_y = random.randint(-100,100)
            if new_x == 0 and new_y == 0:
                new_x = random.randint(-100,100)
                new_y = random.randint(-100,100)
            self.winning_coordinates.append([new_x,new_y])


def handle_help():
    os.system("cat help.txt")

def ask_amount(type):
    if type == "time":
        response = int(input("How many hours would you like to do this for? "))
    return response

def handle_turn(game, player):
    for lst in game.winning_coordinates:
        if game.coordinates[0] == lst[0] and game.coordinates[1] == lst[1]:
            handle_win(player)
            return 0

    scene_name = random.choice(scene_options)
    if scene_name == "cave":
        scene = cave()
    elif scene_name == "river":
        scene = river()
    elif scene_name == "lake":
        scene = lake()
    elif scene_name == "woods":
        scene = lake()
    elif scene_name == "clearing":
        scene = clearing()

    print(scene)
    answer = input("What would you like to do next? ('help' for options) ")
    answer = answer.lower()
    handle_answer(answer,player)

def handle_answer(answer,player):
    if answer == "scavenge":
        time = ask_amount("time")
        handle_scavenge(time,player)
        handle_turn(game,player)
    elif answer == "hunt":
        time = ask_amount("time")
        handle_hunt(time)
        handle_turn(game,player)
    elif answer == "build":
        time = ask_amount("time")
        handle_build(time,player)
        handle_turn(game,player)
    elif answer == "fish":
        time = ask_amount("time")
        handle_fish(time,player)
        handle_turn(game,player)
    elif answer == "walk":
        time = ask_amount("time")
        handle_walk(time,player)
        handle_turn(game,player)
    elif answer == "sleep":
        time = ask_amount("time")
        handle_sleep(time,player)
        handle_turn(game,player)
    elif answer == "help":
        handle_help()
    else:
        print("Sorry that is not a valid command...")
        handle_help()
        answer = input("What would you like to do next? ")
        answer = answer.lower()
        handle_answer(answer)

def handle_win(player):
    x = random.randint(0,3)
    if x == 0:
        print("You come to the crest of a hill and you see a road just a few"
              " feet ahead!\nThere's a car coming!\nYou flagged down the car and"
              " they brought you to civilization!\nCongratulations", player, ",you have "
              "won the game!\n")

    elif x == 1:
        print("You hear a noise above you, you look up, it's a helicopter!\n"
              "They lower down a rope for you and you make it safely back home\n"
              "Congratulations", player, ", you have won the game!\n")

    elif x == 2:
        print("Up ahead it looks like there's some kind of manmade structure!\n"
              "Yes! It's a small town! Some people come out to greet you, they"
              " offer to let you spend the night and they can drive you home"
              " tomorrow.\nCongratulations", player, "you have won the game!\n")

    elif x == 3:
        print("There's a hiker up ahead!\nYou run up to them and ask for help\n"
              "They have a car that's not too far from here and offer to drive you"
              " home!\nCongratulations", player, "you have won the game!")
    return 0
