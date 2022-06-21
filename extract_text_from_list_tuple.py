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
    regex = re.compile(pattern=r"abc")
    matches = [item for item in items if regex.fullmatch(string=item)]
    print(matches)
    # ['abc']
    regex = re.compile(pattern=r"abcd*e*f*g*")
    matches = [item for item in items if regex.fullmatch(string=item)]
    print(matches)
    # ['abcdefg', 'abcde', 'abc']
    matches = [
        regex.search(string=item).group(0) for item in items
        if regex.search(string=item)
    ]
    print(matches)


if __name__ == "__main__":
    main()
