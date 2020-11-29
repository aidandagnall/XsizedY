from model.pair import Pair
from model.animal import Animal
import json
import random

class Generator:
    def __init__(self) -> None:
        self.animals = []
        with open('bot/model/animals.json') as json_file:
            self.data = json.load(json_file)
            for p in self.data['animals']:
                self.animals.append(Animal(p['name'], p['score'], p['plural'], p['size'], p['emoji']))
    
    def createPairRand(self):
        x = y = Animal("", 0, "", "", "")
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
    
    def getTopScores(self):
        scores = sorted(self.animals, key=lambda x: x.score, reverse=True)
        del(scores[5:])
        return scores

    def saveJSON(self, name, newscore):
        print("saving json")
        f = open("bot/model/animals.json", "r")
        json_object = json.load(f)
        f.close()
        for i in json_object['animals']:
            if (i['name'] == name):
                    i['score'] = newscore
        f = open("bot/model/animals.json", "w")
        json.dump(json_object, f, indent=4, sort_keys=True, separators=(',', ': '))
        f.close()


