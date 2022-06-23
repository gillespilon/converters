#! /usr/bin/env python3
"""
Use Python re to match letters from a list or tuple of strings.

The code is entirely mine, not copied from anywhere.

The subject is based on https://regexone.com/lesson/introduction_abcs.
"""

import re


def main():
    items = [
        "abcdefg", "abcde", "abc", "xyz", "1.  abc", "2.   abc",
        "3.      abc", "4.abc"
    ]
    # items = (
    #     "abcdefg", "abcde", "abc", "xyz", "1.  abc", "2.   abc",
    #     "3.      abc", "4.abc"
    # )
    pattern1 = r"\babc\b"
    pattern2 = r"\babcd*e*f*g*\b"
    regex = re.compile(pattern=pattern1)
    matches = [item for item in items if regex.findall(string=item)]
    print(matches)
    # [' abc ', '1.  abc', '2.   abc', '3.      abc', '4.abc']
    matches = [
        regex.findall(string=item) for item in items
        if regex.findall(string=item)
    ]
    print(matches)
    # [['abc'], ['abc'], ['abc'], ['abc'], ['abc']]
    matches = [item for sublist in matches for item in sublist]
    print(matches)
    # ['abc', 'abc', 'abc', 'abc', 'abc']
    regex = re.compile(pattern=pattern2)
    matches = [item for item in items if regex.fullmatch(string=item)]
    print(matches)
    # ['abcdefg', 'abcde', 'abc']
    matches = [
        regex.findall(string=item) for item in items
        if regex.fullmatch(string=item)
    ]
    print(matches)
    # [['abcdefg'], ['abcde'], ['abc']]
    matches = [item for sublist in matches for item in sublist]
    print(matches)
    # ['abcdefg', 'abcde', 'abc']


if __name__ == "__main__":
    main()
