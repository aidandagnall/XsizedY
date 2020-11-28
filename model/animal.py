
class Animal:
    def __init__(self, name, score, plural, size) -> None:
        self.name = name
        self.score = score
        self.plural = plural
        self.size = size

    def __eq__ (self, other):
        return self.name == other.name
    
    def get_image(self):
        return self.name