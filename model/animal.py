
class Animal:
    def __init__(self, name, score) -> None:
        self.name = name
        self.score = score
    
    def get_image(self):
        return self.name