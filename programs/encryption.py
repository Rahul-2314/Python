# Write a python program to translate a message into secret code language. Use the rules below to translate normal English into secret code language

# Coding:
# if the word contains atleast 3 characters, remove the first letter and append it at the end
#   now append three random characters at the starting and the end
# else:
#   simply reverse the string

# Decoding:
# if the word contains less than 3 characters, reverse it
# else:
#   remove 3 random characters from start and end. Now remove the last letter and append it to the beginning

# Your program should ask whether you want to code or decode
import random
import string

def random_words():
    return "".join(random.choices(string.ascii_lowercase, k=3))

def encryption():
    print("=" * 40, " Welcome to Secret Code Translator ", "=" * 40)
    usr_choice = int(input("\ncoding(1)/decoding(2)\n\nchoose your option(1/2) :"))
    coding_key = 1234
    decoding_key = 2314
    if (usr_choice == 1):
        # start coding
        c_key = int(input("\nEnter coding key :"))
        if c_key == coding_key:
            input_string = str(input("\nEnter the massage :"))
            if len(input_string) >= 3:
                first_letter = input_string[0]
                rest_word = input_string[1:]
                random_prefix = random_words()
                random_suffix = random_words()
                print("\nCoded value :", random_prefix +rest_word+first_letter+random_suffix)
            elif len(input_string) < 3:
                print("\nCoded value :", input_string[::-1])
            else:
                print("\nEnter Correct Value")
        else:
            print("\nPlease enter correct key")
    elif (usr_choice == 2):
        # start decoding
        c_key = int(input("\nEnter decoding key :"))
        if c_key == decoding_key:
            decoding_val = str(input("\nEnter the coded message :"))
            if len(decoding_val) >= 3:
                real_val = decoding_val[3:-3]
                first_letter = real_val[-1]
                rest_word = real_val[:-1]
                print("\nDecoded massage :", first_letter+rest_word)
            elif len(decoding_val) < 3:
                print("\nDecoded massage :", decoding_val[::-1])
            else:
                print("\nEnter Correct Value")
        else:
            print("\nPlease enter correct key")
    else:
        print("\n (1 for coding / 2 for decoding)\n\n choose your option carefully")

while(True):
    encryption()
