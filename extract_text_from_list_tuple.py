#! /usr/bin/env python3
"""
Use Python re to match letters from a list or tuple of strings.

The code is entirely mine, not copied from anywhere.

The subject is based on https://regexone.com/lesson/introduction_abcs.
"""

import re


def main():
    items = ["abcdefg", "abcde", "abc", "xyz"]
    # items = ("abcdefg", "abcde", "abc", "xyz")
    pattern1 = r"abc"
    pattern2 = r"abcd*e*f*g*"
    pattern3 = r"[^a][b-c]"
    pattern4 = r"[^a][b-c]d?e?"
    regex = re.compile(pattern=pattern1)
    matches = [item for item in items if regex.fullmatch(string=item)]
    print(matches)
    matches = [
        regex.search(string=item).group(0) for item in items
        if regex.search(string=item)
    ]
    print(matches)
    # ['abc']
    regex = re.compile(pattern=pattern2)
    matches = [item for item in items if regex.fullmatch(string=item)]
    print(matches)
    # ['abcdefg', 'abcde', 'abc']
    matches = [
        regex.search(string=item).group(0) for item in items
        if regex.search(string=item)
    ]
    print(matches)
    # ['abcdefg', 'abcde', 'abc']
    regex = re.compile(pattern=pattern3)
    matches = [item for item in items if regex.search(string=item)]
    print(matches)
    # ['abcdefg', 'abcde', 'abc']
    matches = [
        regex.search(string=item).group(0) for item in items
        if regex.search(string=item)
    ]
    print(matches)
    # ['bc', 'bc', 'bc']
    regex = re.compile(pattern=pattern4)
    matches = [item for item in items if regex.search(string=item)]
    print(matches)
    # ['abcdefg', 'abcde', 'abc']
    matches = [
        regex.search(string=item).group(0) for item in items
        if regex.search(string=item)
    ]
    print(matches)
    # ['bcde', 'bcde', 'bc']


if __name__ == "__main__":
    main()
