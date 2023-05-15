#! /usr/bin/env python3
"""
Generate ten random passphrases of five words in title case, with a single
random integer at the end.

The json dictionary of English words is found here:
https://github.com/dwyl/english-words/blob/master/words_alpha.txt
"""

import random

import pandas as pd


def main():
    df = pd.read_json(path_or_buf="words_dictionary.json", orient="index")
    for phrase in range(0, 10, 1):
        random_passphrase = [x.title() for x in df.sample(n=5).index.tolist()]
        random_passphrase.append(random.randint(0, 9))
        print(*random_passphrase, sep=" ")


if __name__ == "__main__":
    main()
