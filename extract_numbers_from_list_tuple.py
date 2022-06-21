#! /usr/bin/env python3
"""
Use Python re to extract numbers from a list or tuple of strings.

The code is entirely mine, not copied from anywhere.

The subject is based on https://regexone.com/lesson/letters_and_digits.
"""

import re


def main():
    items = [
        "abc123xyz",
        "define '123'",
        "foo234bar",
        "var g = 123;"
    ]
    # items = (
    #     "abc123xyz",
    #     "define '123'",
    #     "var g = 123;"
    # )
    pattern1 = r"123"
    pattern2 = r"\d{3}"
    pattern3 = r"\d.."
    pattern4 = r"[1-3]{3}"
    pattern5 = r"[2-4]{3}"
    regex = re.compile(pattern=pattern1)
    matches = [item for item in items if regex.search(string=item)]
    print(matches)
    # ['abc123xyz', "define '123'", 'var g = 123;']
    matches = [
        regex.search(string=item).group(0) for item in items
        if regex.search(string=item)
    ]
    print(matches)
    # ['123', '123', '123']
    regex = re.compile(pattern=pattern2)
    matches = [item for item in items if regex.search(string=item)]
    print(matches)
    # ['abc123xyz', "define '123'", 'foo234bar', 'var g = 123;']
    matches = [
        regex.search(string=item).group(0) for item in items
        if regex.search(string=item)
    ]
    print(matches)
    # ['123', '123', '234', '123']
    regex = re.compile(pattern=pattern3)
    matches = [item for item in items if regex.search(string=item)]
    print(matches)
    # ['abc123xyz', "define '123'", 'foo234bar', 'var g = 123;']
    matches = [
        regex.search(string=item).group(0) for item in items
        if regex.search(string=item)
    ]
    print(matches)
    # ['123', '123', '234', '123']
    regex = re.compile(pattern=pattern4)
    matches = [item for item in items if regex.search(string=item)]
    print(matches)
    # ['abc123xyz', "define '123'", 'var g = 123;']
    matches = [
        regex.search(string=item).group(0) for item in items
        if regex.search(string=item)
    ]
    print(matches)
    # ['123', '123', '123']
    regex = re.compile(pattern=pattern5)
    matches = [item for item in items if regex.search(string=item)]
    print(matches)
    # ['foo234bar']
    matches = [
        regex.search(string=item).group(0) for item in items
        if regex.search(string=item)
    ]
    print(matches)
    # ['234']


if __name__ == "__main__":
    main()
