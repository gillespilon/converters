#! /usr/bin/env python3
"""
Use Python re to extract a date from a list or tuple of strings.

The code is entirely mine, not copied from anywhere.

The subject is in response to someone's query.
"""

import re


def main():
    items = [
        "Hello 06/08/1956 date.",
        "Hello 1956-06-08 date."
    ]
    # items = (
    #     "Hello 06/08/1956 date.",
    #     "Hello 1956-06-08 date."
    # )
    regex = re.compile(pattern=r"\d{1,2}\/\d{1,2}\/\d{2,4}")
    matches = [item for item in items if regex.search(string=item)]
    print(matches)
    # ['Hello 06/08/1956 date.']
    matches = [
        regex.search(string=item).group(0) for item in items
        if regex.search(string=item)
    ]
    print(matches)
    # ['06/08/1956']
    regex = re.compile(pattern=r"\d{2,4}-\d{1,2}-\d{1,2}")
    matches = [item for item in items if regex.search(string=item)]
    print(matches)
    # ['Hello 1956-06-08 date.']
    matches = [
        regex.search(string=item).group(0) for item in items
        if regex.search(string=item)
    ]
    print(matches)
    # ['1956-06-08']
    regex = re.compile(
        pattern=r"\d{2,4}-\d{1,2}-\d{1,2}|\d{1,2}\/\d{1,2}\/\d{2,4}"
    )
    matches = [item for item in items if regex.search(string=item)]
    print(matches)
    # ['Hello 06/08/1956 date.', 'Hello 1956-06-08 date.']
    matches = [
        regex.search(string=item).group(0) for item in items
        if regex.search(string=item)
    ]
    print(matches)
    # ['06/08/1956', '1956-06-08']


if __name__ == "__main__":
    main()
