import random
import string


def random_words():
    return "".join(random.choices(string.ascii_lowercase, k=3))


def encode_word(word):
    if len(word) >= 3:
        first_letter = word[0]
        rest_word = word[1:]
        random_prefix = random_words()
        random_suffix = random_words()
        return random_prefix + rest_word + first_letter + random_suffix
    else:
        return word[::-1]


def decode_word(word):
    if len(word) >= 3:
        real_val = word[3:-3]
        first_letter = real_val[-1]
        rest_word = real_val[:-1]
        return first_letter + rest_word
    else:
        return word[::-1]


def encryption():
    print("=" * 40, " Welcome to Secret Code Translator ", "=" * 40)
    usr_choice = int(
        input("\ncoding(1)/decoding(2)\n\nchoose your option(1/2) :"))
    coding_key = 1234
    decoding_key = 2314

    if usr_choice not in [1, 2]:
        print("\n(1 for coding / 2 for decoding)\n\nChoose your option carefully")
        return

    key = int(input("\nEnter coding key :" if usr_choice ==
              1 else "\nEnter decoding key :"))

    if usr_choice == 1 and key != coding_key or usr_choice == 2 and key != decoding_key:
        print("\nPlease enter correct key")
        return

    input_string = input("\nEnter the message :")

    if usr_choice == 1:
        coded_message = ' '.join(encode_word(word)
                                 for word in input_string.split())
        print("\nCoded value :", coded_message)
    else:
        decoded_message = ' '.join(decode_word(word)
                                   for word in input_string.split())
        print("\nDecoded message :", decoded_message)


while True:
    encryption()
