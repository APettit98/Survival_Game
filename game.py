import random, os

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
