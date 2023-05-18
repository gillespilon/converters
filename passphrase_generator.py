#! /usr/bin/env python3
"""
WHAT
Generate ten random passphrases of six words:
    Word space Word space Word space Word space Word space integer+character

An example would be:
    Creosol Eradicates Cycloheptanone Posttracheal Impostumation 4&

HOW
- json dictionary of English words
    https://github.com/dwyl/english-words/blob/master/words_alpha.txt
- list comprehension of five random title-case words
- extend the list with an integer and special character
"""

import random

import pandas as pd


def main():
    df = pd.read_json(path_or_buf="words_dictionary.json", orient="index")
    for phrase in range(0, 10, 1):
        # Create a list of five random words.
        random_passphrase = [x.title() for x in df.sample(n=5).index.tolist()]
        # Extend the list with a random integer and a random special symbol.
        random_passphrase.extend(
            [
                str(random.randint(0, 9)),
                random.choice([
                    "~", "!", "@", "#", "$", "%", "^", "&", "*",
                    "(", ")", "_", "-", "+", "=", "{", "}", ".",
                    "[", "]", "|", "\\", ":", ";", "\'", "\"", ",",
                    "<", ">", "?", "/"
                ])
            ]
        )
        # Join the random integer and random symbol into one string.
        random_passphrase[-2:None] = ["".join(random_passphrase[-2:None])]
        print(*random_passphrase, sep=" ")


if __name__ == "__main__":
    main()
