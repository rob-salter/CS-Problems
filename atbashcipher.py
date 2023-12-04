#inspired by bfirest1's
import string

ENCODE_TABLE = str.maketrans(string.ascii_lowercase,string.ascii_lowercase[::-1])
DECODE_TABLE= str.maketrans(string.ascii_lowercase[::-1],string.ascii_lowercase)

def decode(ciphered_text):
  text = ''.join([c for c in ciphered_text if c.isalnum()])
  return text.lower().translate(DECODE_TABLE)

def encode(plain_text):
  text = ''.join([c for c in plain_text if c.isalnum()])
  return chunk(text.lower().translate(ENCODE_TABLE))

def chunk(text):
 return ' '.join([text[i:i+5] for i in range(0, len(text), 5)])
  
# def encode(plain_text):
#   return chunk(''.join([LETTERS_REVERSED[LETTERS.index(char)] if not char.isnumeric() else char for char in plain_text.lower().replace(' ','').replace(',','').replace('.','')]))

# def decode(ciphered_text):
#   return ''.join([LETTERS[LETTERS_REVERSED.index(char)] if not char.isnumeric() else char for char in ciphered_text.lower().replace(' ','').replace(',','').replace('.','')])

#print(decode("thequ12ickbrownfoxjumpsoverthelazydog"))
#print(encode("gsv12jf rxpyi ldmu"))

#print(encode("Testing,1 2 3, testing."))

