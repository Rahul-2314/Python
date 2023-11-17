import random
import string

random_space = ["₹", "¡", "£", "¢", "¥", "§", "Ö", "Σ", "φ", "∅"]

ascii_dict = {'!': '.', '"': 'o', '#': '9', '$': 'g', '%': '^', '&': '\\', "'": 'F', '(': ')', ')': '0', '*': 'n', '+': 'E', ',': '*', '-': '1', '.': '-', '/': 'Z', '0': '5', '1': 'S', '2': 'e', '3': 'h', '4': '~', '5': 'a', '6': 't', '7': 'I', '8': '>', '9': 'z', ':': '[', ';': 'j', '<': '+', '=': '|', '>': '2', '?': '7', '@': 'X', 'A': 'l', 'B': 'r', 'C': '"', 'D': '<', 'E': 'V', 'F': 'k', 'G': '@', 'H': '!', 'I': ']', 'J': ',', 'K': 'J', 'L': 'f', 'M': 'i', 'N': 'm', 'O': '8',
              'P': 'K', 'Q': 'w', 'R': 'b', 'S': 'H', 'T': 'D', 'U': 'T', 'V': 'W', 'W': 'Q', 'X': '=', 'Y': 'A', 'Z': 'N', '[': 'P', '\\': '3', ']': 'x', '^': 'c', '_': '&', '`': 'L', 'a': 'Y', 'b': 'R', 'c': '`', 'd': '/', 'e': 'C', 'f': '?', 'g': 'p', 'h': '_', 'i': 'y', 'j': ';', 'k': 'u', 'l': 'G', 'm': '}', 'n': ':', 'o': '6', 'p': '{', 'q': 'v', 'r': 'B', 's': '%', 't': '(', 'u': '$', 'v': "'", 'w': '4', 'x': '#', 'y': 's', 'z': 'q', '{': 'U', '|': 'O', '}': 'd', '~': 'M'}


def enc_transform(word):
    mod_word = ""
    for char in word:
        if char in ascii_dict:
            mod_word += ascii_dict[char]
        else:
            mod_word += char 
    return mod_word


def dec_transform(word):
    mod_word = ""
    rev_dict = {v: k for k, v in ascii_dict.items()}
    for char in word:
        if char in rev_dict:
            mod_word += rev_dict[char]
        else:
            mod_word += char
    return mod_word

def random_words():
    return "".join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=2))


def encode_word(word):
    rev_word = word[::-1]
    mod_word=enc_transform(rev_word)
    enc_word=""
    for i in range(len(mod_word)):
        random_word=random_words()
        enc_word=enc_word+random_word+mod_word[i]
    return enc_word


def decode_word(word):
    dec_word =""
    for i in range(2,len(word),3):
        dec_word=dec_word+word[i]
    dec_word = dec_transform(dec_word)
    return dec_word[::-1]

def replace_spaces(sentence):
    new_sentence = ""
    for char in sentence:
        if char == ' ':
            random_char = random.choice(random_space)
            new_sentence += random_char
        else:
            new_sentence += char
    return new_sentence

def revert_spaces(sentence):
    new_sentence = ""
    for char in sentence:
        if char in random_space:
            new_sentence += ' '
        else:
            new_sentence += char
    return new_sentence


def encryption():
    print("=" * 40, " Welcome to Encryption Translator ", "=" * 40)

    usr_choice = int(
        input("\ncoding(1)/decoding(2)\n\nchoose your option(1/2) :"))
    
    coding_key = 1234
    decoding_key = 2314

    if usr_choice not in [1, 2]:
        print("\n(1 for coding / 2 for decoding)\n\nChoose your option carefully")
        return

    key = int(input("\nEnter coding key :" if usr_choice == 1 else "\nEnter decoding key :"))

    if usr_choice == 1 and key != coding_key or usr_choice == 2 and key != decoding_key:
        print("\nPlease enter correct key")
        return

    input_string = input("\nEnter the message :")

    if usr_choice == 1:
        coded_message = ' '.join(encode_word(word)
                                 for word in input_string.split())
        print("\nCoded message :",replace_spaces(coded_message))
    else:
        decoded_message = ' '.join(decode_word(word)
                                   for word in revert_spaces(input_string).split())
        print("\nDecoded message :",decoded_message)


while True:
    encryption()
