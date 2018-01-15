class player:
    def __init__(self,name,materials,food,health,shelter,near_water):
        self.name = name
        self.materials = {"sticks":0, "string":0, "rope":0,"knives":0,
                          "matchboxes":0, "sharp rocks":0, "rusty fishing hooks":0,
                          "moss":0, "tinder":0, "logs":0, "bows":0, "arrows":0,
                          "spears":0}
        self.food = food_list = {"rabbit": 0, "fish":0, "deer":0, "boar":0,
                                 "squirrel":0,"bear":0,"turkey":0,"porcupine":0,
                                 "cooked fish":0,"cooked deer":0,"cooked boar":0,
                                 "cooked squirrel":0, "cooked rabbit":0,
                                 "cooked bear":0,"cooked turkey":0,
                                 "cooked porcupine":0}

        self.health = {"hunger":0, "energy":0}
        self.shelter = {"exits":False, "stability":0, "comfort":0}
        self.near_water = False

    def __str__(self):
        return self.name
