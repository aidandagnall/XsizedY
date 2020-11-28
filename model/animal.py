
class Animal:
    def __init__(self, name, score, plural, size) -> None:
        self.name = name
        self.score = score
        self.plural = plural
        self.size = size
        self.emoji = Animal.getEmoji(self)

    def __eq__ (self, other):
        return self.name == other.name
    
    def get_image(self):
        return self.name
    
    def getEmoji(self):
        if (self.name == "cow"):
            return '\U0000f404'
        elif(self.name == "pig"):
            return '\U0001f437'
        elif(self.name == "chicken"):
            return '\U0001f414'
        elif(self.name == "horse"):
            return '\U0001f40e'
        elif(self.name == "goat"):
            return '\U0001f410'
        elif(self.name == "sheep"):
            return '\U0001f411'
        elif(self.name == "duck"):
            return '\U0001f986'
        elif(self.name == "llama"):
            return '\U0001f999'
        elif(self.name == "panda"):
            return '\U0001f43C'
        elif(self.name == "rabbit"):
            return '\U0001f407'
        elif(self.name == "mouse"):
            return '\U0001f42d'
        elif(self.name == "hamster"):
            return '\U0001f439'
        elif(self.name == "fox"):
            return '\U0001f98a'
        elif(self.name == "bear"):
            return '\U0001f43b'
        elif(self.name == "polar bear"):
            return '\U000200d'
        elif(self.name == "koala"):
            return '\U0001f428'
        elif(self.name == "tiger"):
            return '\U0001f42f'
        elif(self.name == "lion"):
            return '\U0001f981'
        elif(self.name == "frog"):
            return '\U0001f438'
        elif(self.name == "monkey"):
            return '\U0001f648'
        elif(self.name == "penguin"):
            return '\U0001f427'
        elif(self.name == "bird"):
            return '\U0001f426'
        elif(self.name == "dodo"):
            return '\U0001f9a4'
        elif(self.name == "eagle"):
            return '\U0001f985'
        elif(self.name == "owl"):
            return '\U0001f989'
        elif(self.name == "bat"):
            return '\U0001f987'
        elif(self.name == "wolf"):
            return '\U0001f43a'
        elif(self.name == "boar"):
            return '\U0001f417'
        elif(self.name == "bee"):
            return '\U0001f41d'
        elif(self.name == "snail"):
            return '\U0001f40c'
        elif(self.name == "lady bug"):
            return '\U0001f41e'
        elif(self.name == "ant"):
            return '\U0001f41c'
        elif(self.name == "fly"):
            return '\U0001fab0'
        elif(self.name == "snake"):
            return '\U0001f40d'
        elif(self.name == "lizard"):
            return '\U0001f98e'
