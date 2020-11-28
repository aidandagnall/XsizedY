from model.pair import Pair
from model.animal import Animal
import json
import random

class Generator:
    def __init__(self) -> None:
        self.animals = []
        self.scores = [0,0,0,0,0,0,0,0,0,0]
        with open('model/animals.json') as json_file:
            self.data = json.load(json_file)
            for p in self.data['animals']:
                self.animals.append(Animal(p['name'], p['score'], p['plural'], p['size']))
    
    def createPairRand(self):
        # x, y  = new random animal
        x = y = Animal("", 0, "", "")
        while (x.name == y.name or y.size <= x.size):
            x = self.animals[random.randint(0, len(self.animals) - 1)]
            y = self.animals[random.randint(0, len(self.animals) - 1)]
        return Pair(x, y)
    
    def createPair(self, x):
        y = x
        while (x == y):
            y = self.animals[random.randint(0, len(self.animals) - 1)]
        return Pair(x, y)
    
    def createGivenPair(self, a, b):
        if a == None or b == None:
            return None
        return Pair(a, b)

    def getAnimal(self, str):
        str = str.lower()
        for animal in self.animals:
            if str == animal.name:
                return animal
        return None
    def TOPSCORE(self):
        file = open("model/animals.json","r")
        json_object = json.load(file)
        file.close()
        for i in range(len(json_object['animals'])):
            print(str(json_object['animals'][i]['score']))
            if json_object['animals'][i]['score'] > self.scores[9]:
                for x in self.scores:
                    if json_object['animals'][i]['score'] >= self.scores[x]:
                        self.scores.insert(x,json_object['animals'][i]['score'])
                        self.scores.pop(10)
                        self.scores.sort(reverse=True)
                        break
        print(str(self.scores))
