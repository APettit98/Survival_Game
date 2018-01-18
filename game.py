import random, os
from scenes import *

scene_options = ["cave", "river", "lake", "woods", "clearing"]

class game:
    def __init__(self):
        self.coordinates = [0,0]
        self.winning_coordinates = []
        self.time = {"hour": 8, "day":1}
        self.scene = ""
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

def time_up(game,length,player):
    game.time["hour"] += length
    if game.time["hour"] >= 24:
        game.time["hour"] = game.time["hour"] - 24
        game.time["day"] += 1
    player.health["energy"] -= 2 * length
    player.health["hunger"] += 2 * length

def ask_amount(type):
    if type == "time":
        response = int(input("How many hours would you like to do this for? "))
    return response

def handle_turn(game, player, new_scene):
    for lst in game.winning_coordinates:
        if game.coordinates[0] == lst[0] and game.coordinates[1] == lst[1]:
            handle_win(player)
            return 0
    if player.health["energy"] <= 0 or player.health["hunger"] >= 100:
        handle_lose(player)
        return 1
    if new_scene:
        scene_name = random.choice(scene_options)
        game.scene = scene_name
        if scene_name == "cave":
            scene = cave()
        elif scene_name == "river":
            scene = river()
        elif scene_name == "lake":
            scene = lake()
        elif scene_name == "woods":
            scene = woods()
        elif scene_name == "clearing":
            scene = clearing()

        print(scene)
    answer = input("What would you like to do next? ('help' for options) ")
    answer = answer.lower()
    handle_answer(answer,player,game)
    print("TEST TEST TEST TEST TEST")

def handle_answer(answer,player,game):
    if answer == "scavenge":
        time = ask_amount("time")
        handle_scavenge(time,player,game)
        handle_turn(game,player,False)
    elif answer == "hunt":
        time = ask_amount("time")
        handle_hunt(time,player,game)
        handle_turn(game,player,False)
    elif answer == "build":
        time = ask_amount("time")
        handle_build(time,player,game)
        handle_turn(game,player,False)
    elif answer == "fish":
        time = ask_amount("time")
        handle_fish(time,player,game)
        handle_turn(game,player,False)
    elif answer == "walk":
        time = ask_amount("time")
        handle_walk(time,player,game)
        handle_turn(game,player,True)
    elif answer == "sleep":
        time = ask_amount("time")
        handle_sleep(time,player,game)
        handle_turn(game,player,False)
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

def handle_lose(player):
    if player.health["energy"] <= 0:
        print("You are too exhausted to go on... Sorry,", player, "you have lost...")
    elif player.health["hunger"] >= 100:
        print("You are too hungry to continue, you should have made eating more of"
              " a priority... Sorry,", player, "you have lost...")

    return 0
