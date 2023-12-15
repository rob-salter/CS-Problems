import random
import string
from itertools import cycle

ALPHABET = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

class Cipher:
    def __init__(self, key=None):
        if key==None:
            self.key = "".join(random.choice(string.ascii_lowercase) for i in range(100))
        else:
            self.key = key

    def encode(self, text):
        shifted_text = []
        
        for char, letter in zip(text, cycle(self.key)):
            cipher_index = int(ALPHABET.index(letter))
            shift_index = ALPHABET.index(char) + cipher_index
            shifted_text.append(ALPHABET[int(shift_index)])
            
        return ''.join(shifted_text)

    def decode(self, text):
        shifted_text = []
        
        for char, letter in zip(text, cycle(self.key)):
            cipher_index = int(ALPHABET.index(letter))
            shift_index = ALPHABET.index(char) - cipher_index
            shifted_text.append(ALPHABET[int(shift_index)])
            
        return ''.join(shifted_text)        
