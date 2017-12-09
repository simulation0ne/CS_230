""" crypto.py
    Implements a simple substitution cypher
"""

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
key =   "XPMGTDHLYONZBWEARKJUFSCIQV"

def menu():
    print("""
SECRET DECODER MENU

0) Quit
1) Encode
2) Decode
""")
    return input("What do you want to do?")

def encode(phrase):
    phrase = phrase.upper()
    encoded_phrase = ""
    for l in phrase:
        if l not in alpha:
            continue
        else:
            encoded_phrase += key[alpha.index(l)]
    return encoded_phrase

def decode(phrase):
    phrase = phrase.upper()
    decoded_phrase = ""
    for l in phrase:
        if l not in alpha:
            continue
        else:
            decoded_phrase += alpha[key.index(l)]
    return decoded_phrase

def main():
  keepGoing = True
  while keepGoing:
    response = menu()
    if response == "1":
      plain = input("text to be encoded: ")
      print(encode(plain))
    elif response == "2":
      coded = input("code to be decyphered: ")
      print (decode(coded))
    elif response == "0":
      print ("Thanks for doing secret spy stuff with me.")
      keepGoing = False
    else:
      print ("I don't know what you want to do...")

if __name__ == '__main__':
    main()