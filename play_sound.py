#! /usr/bin/env python3
"""
Example file to play a sound upon startup of the script.

Requires installation of playsound

    pip install --user playsound
"""

from playsound import playsound
from pathlib import Path


def main():
    path_to_sound = Path('ribbit.mp3')
    playsound(sound=path_to_sound)


if __name__ == '__main__':
    main()
