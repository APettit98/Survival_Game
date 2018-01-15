import random

class game:
    def __init__(self,coordinates,winning_coordinates,time):
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
