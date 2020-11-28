from model.pair import Pair
from model.animal import Animal
import csv
import random
class Generator:
    def __init__(self) -> None:
        self.animals = []
        self.file = open("model/Animals.csv", "r")
        reader = csv.reader(self.file, delimiter =",")
        for row in reader:
            self.animals.append(Animal(row[0], row[1]))
    
    def createPairRand(self):
        # x, y  = new random animal
        x = y = 1
        while (x == y):
            x = self.animals[random.randint(0, len(self.animals) - 1)]
            y = self.animals[random.randint(0, len(self.animals) - 1)]
        return Pair(x, y)
    
    def createPair(self, x):
        y = x
        while (x == y):
            y = self.animals[random.randint(0, len(self.animals) - 1)]
        return Pair(x, y)
