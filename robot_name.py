import random
import string
class Robot:

    names = set()

    def __init__(self):
        self.reset()

    def generate_name(self):    
        name = ""
        for i in range(0,2):
            name += random.choice(string.ascii_uppercase)
        for i in range(0,3):
            name += str(random.randint(0,9))
        return name    

    def reset(self):
        name = self.generate_name()
        while name in self.names:
            name = self.generate_name()
        self.names.add(name)
        self.name = name    
        