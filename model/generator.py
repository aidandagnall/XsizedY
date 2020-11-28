from model.pair import Pair
from model.animal import Animal
import csv
import json
import random
class Generator:
    def __init__(self) -> None:
        self.animals = []
        with open('model/animals.json') as json_file:
            self.data = json.load(json_file)
            for p in self.data['animals']:
                self.animals.append(Animal(p['name'], p['score'], p['plural'], p['size'], '😀'))
    
    def createPairRand(self):
        # x, y  = new random animal
        x = y = Animal("", 0, "", "", "")
        while (x == y or x.size == y.size):
            x = self.animals[random.randint(0, len(self.animals) - 1)]
            y = self.animals[random.randint(0, len(self.animals) - 1)]
        return Pair(x, y)
    
    def createPair(self, x):
        y = x
        while (x == y):
            y = self.animals[random.randint(0, len(self.animals) - 1)]
        return Pair(x, y)

    def getAnimal(self, str):
        str = str.lower()
        for animal in self.animals:
            if str == animal.name:
                return animal
        return Animal(str, 0)
