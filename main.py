import random, sys, os
from player import *
from game import *

def main():
    game_g = game([],[],[])
    print("Welcome to this text survival game! What is your name?")
    name = input()
    user = player(name,{},{},{},{},False)
    os.system('clear')
    print("Hello,", user)


if __name__ == "__main__":
    main()
