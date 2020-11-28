
class Animal:
    def __init__(self, name, score) -> None:
        self.name = name
        self.score = score

    def __eq__ (self, other):
        return self.name == other.name
    
    def get_image(self):
        return self.name