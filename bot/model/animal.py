
import unicodedata
class Animal:
    def __init__(self, name, score, plural, size, emoji) -> None:
        self.name = name
        self.score = score
        self.plural = plural
        self.size = size
        self.emoji = emoji.encode('ASCII').decode('unicode-escape')
                                
    def __lt__ (self, other):
        return self.size < other.size
    
    def get_image(self):
        return self.name
