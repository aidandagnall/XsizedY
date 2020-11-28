from model.pair import Pair
from model.animal import Animal
import csv
import random
class Generator:
    def __init__(self) -> None:
        self.animals = []
        self.file = open("../Animals.csv", "r")
        reader = csv.reader(self.file, delimiter =",")
        for row in reader:
            self.animals.add(Animal(row[0], row[1]))
    
    def createPair(self):
        # x, y  = new random animal
        x = y = 1
        while (x == y):
            x = self.animals[random.randint(0, len(self.animals))]
            y = self.animals[random.randint(0, len(self.animals))]

        return Pair(x, y)

    def createPair(x):
        # y = new random animal
        return Pair(x, y)