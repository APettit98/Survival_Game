import random, sys, os, time
from player import *
from game import *
from scenes import *

def main():
    game_g = game()
    print("Welcome to this text survival game! What is your name?")
    name = input()
    user = player(name)
    print("Good luck", name, "your adventure is about to begin...")
    time.sleep(2)
    os.system('clear')
    print("You wake up in the middle of the woods... "
          "You have no clue how you got there.\nThe sun is beating down on you, "
          "you look around and all you see are trees... \n"
          "You check your phone, no service. You don't know if anyone else knows you are here\n"
          "Which direction would you like to go? ('help' for furthur instructions)\n")
    answer = input()
    answer = answer.lower()
    if answer == "help":
        handle_help()
        handle_turn(game_g,user,False)
    elif answer == 'north' or answer.startswith("n"):
        length = ask_amount("time")
        game_g.coordinates[1] += length
        if game_g.coordinates[1] > 100:
            print("Sorry you've reached the bounds of the game, you only walked",
                  length - (game_g.coordinates[1] - 100), "hours")
    elif answer == 'south' or answer.startswith("s"):
        length = ask_amount("time")
        game_g.coordinates[1] -= length
        if game_g.coordinates[1] < -100:
            print("Sorry you've reached the bounds of the game, you only walked",
                  length + (game_g.coordinates[1] + 100), "hours")
    elif answer == 'east' or answer.startswith("e"):
        length = ask_amount("time")
        game_g.coordinates[0] += length
        if game_g.coordinates[0] > 100:
            print("Sorry you've reached the bounds of the game, you only walked",
                  length - (game_g.coordinates[0] - 100), "hours")
    elif answer == 'west' or answer.startswith("w"):
        length = ask_amount("time")
        game_g.coordinates[0] -= length
        if game_g.coordinates[0] < -100:
            print("Sorry you've reached the bounds of the game, you only walked",
                  length + (game_g.coordinates[1] + 100), "hours")

    else:
        print("Sorry that is not a valid command\n")
        handle_help()
    time_up(game_g,length,user)
    handle_turn(game_g, user, True)
    sys.exit()



if __name__ == "__main__":
    main()
