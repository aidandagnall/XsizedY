
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