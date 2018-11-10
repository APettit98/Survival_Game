import random, os
from scenes import *

# For all functions containing game or player parameters,
# game and player are the global variables for the game and player that are
# passed around to every function

scene_options = ["cave", "river", "lake", "woods", "clearing"]

# Class object for a game
# Contains the current coordinate location, a list of winning coordinates,
# the current time, and the current 'scene',
class game:
    def __init__(self):
        self.coordinates = [0,0]
        self.winning_coordinates = []
        self.time = {"hour": 0, "day":1}
        self.scene = ""
        i = 0
        for i in range(0,101):
            new_x = random.randint(-100,100)
            new_y = random.randint(-100,100)
            if new_x == 0 and new_y == 0:
                new_x = random.randint(-100,100)
                new_y = random.randint(-100,100)
            self.winning_coordinates.append([new_x,new_y])

# Used to handle case when user asks for help, displays instructions located in
# help.txt
def handle_help():
    os.system("cat help.txt")

# Used to handle case when user decides to quit, gracefully exits program
def handle_quit():
    sys.exit(0)

# Used to increment time in the game
# game and player are the global game and player variables
# length is the amount of time to increase by
def time_up(game,length,player):
    game.time["hour"] += length
    if game.time["hour"] >= 24:
        game.time["hour"] = game.time["hour"] - 24
        game.time["day"] += 1
    player.health["energy"] -= 2 * length
    player.health["hunger"] += 2 * length

# Asks user to enter an amount
# Type is type of input they are giving, e.g. time
# Game is the global game object, and player is the global player object
# Does not exit gracefully if user does not enter a number
def ask_amount(type, game, player):
    if type == "time":
        response = int(input("How many hours would you like to do this for? "))
        time_up(game,response,player)
    return response

# Used to handle player's turns
# Displays a new scene if the player has moved since the last turn
# Asks the user what to do next
# game and player are global variables that are passed around
# new_scene is a boolean that dictates whether or not the user has moved
def handle_turn(game, player, new_scene):
    for lst in game.winning_coordinates:
        if game.coordinates[0] == lst[0] and game.coordinates[1] == lst[1] or game.time["day"] >= 365:
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

# Handles user's response when asked what to do next
# Answer is the next action
def handle_answer(answer,player,game):
    if answer == "scavenge":
        time = ask_amount("time", game, player)
        handle_scavenge(time,player,game)
        time_up(game,time,player)
        handle_turn(game,player,False)
    elif answer == "hunt":
        time = ask_amount("time", game, player)
        handle_hunt(time,player,game)
        time_up(game,time,player)
        handle_turn(game,player,False)
    elif answer == "build":
        time = ask_amount("time", game, player)
        handle_build(time,player,game)
        time_up(game,time,player)
        handle_turn(game,player,False)
    elif answer == "fish":
        time = ask_amount("time", game, player)
        handle_fish(time,player,game)
        time_up(game,time,player)
        handle_turn(game,player,False)
    elif answer == "walk":
        time = ask_amount("time", game, player)
        handle_walk(time,player,game)
        time_up(game,time,player)
        handle_turn(game,player,True)
    elif answer == "sleep":
        time = ask_amount("time", game, player)
        handle_sleep(time,player,game)
        time_up(game,time,player)
        handle_turn(game,player,False)
    elif answer == "help":
        handle_help()
        handle_turn(game,player,False)
    elif answer == 'quit':
        handle_quit()
    else:
        print("Sorry that is not a valid command...")
        handle_help()
        answer = input("What would you like to do next? ")
        answer = answer.lower()
        handle_answer(answer, player, game)

# Handles case where user has won the game
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

# Handles cases where user has lost the game
def handle_lose(player):
    if player.health["energy"] <= 0:
        print("You are too exhausted to go on... Sorry,", player, "you have lost...")
    elif player.health["hunger"] >= 100:
        print("You are too hungry to continue, you should have made eating more of"
              " a priority... Sorry,", player, "you have lost...")
    elif player.health["injury"] >= 100:
        print("After numerous mishaps on your road to survival, you finally succummed"
        " to your many injuries... Sorry,", player, "you have lost...")

    return 0
