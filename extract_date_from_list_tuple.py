#! /usr/bin/env python3
"""
Use Python re to extract a date from a list or tuple of strings.
"""

import re


def main():
    items = [
        "A 06/08/1956 A 01/14/1968 A",
        "B 1956-06-08 B 1968-01-14 B",
        "C 1956-06-08 C 01/14/1968 C"
    ]
    # items = (
    #     "A 06/08/1956 A 01/14/1968 A",
    #     "B 1956-06-08 B 1968-01-14 B",
    #     "C 1956-06-08 C 01/14/1968 C"
    # )
    pattern1 = r"\b\d{1,2}\/\d{1,2}\/\d{2,4}\b"
    pattern2 = r"\b\d{2,4}-\d{1,2}-\d{1,2}\b"
    regex = re.compile(pattern=pattern1)
    matches = [item for item in items if regex.findall(string=item)]
    print(matches)
    # ['A 06/08/1956 A 01/14/1968 A', 'C 1956-06-08 C 01/14/1968 C']
    matches = [
        regex.findall(string=item) for item in items
        if regex.findall(string=item)
    ]
    print(matches)
    # [['06/08/1956', '01/14/1968'], ['01/14/1968']]
    matches = [item for sublist in matches for item in sublist]
    print(matches)
    # ['06/08/1956', '01/14/1968', '01/14/1968']
    regex = re.compile(pattern=pattern2)
    matches = [item for item in items if regex.findall(string=item)]
    print(matches)
    # ['B 1956-06-08 B 1968-01-14 B', 'C 1956-06-08 C 01/14/1968 C']
    matches = [
        regex.findall(string=item) for item in items
        if regex.findall(string=item)
    ]
    print(matches)
    # [['1956-06-08', '1968-01-14'], ['1956-06-08']]
    matches = [item for sublist in matches for item in sublist]
    print(matches)
    # ['1956-06-08', '1968-01-14', '1956-06-08']
    regex = re.compile(
        pattern=pattern1 + "|" + pattern2
    )
    matches = [item for item in items if regex.findall(string=item)]
    print(matches)
    # [
    #     'A 06/08/1956 A 01/14/1968 A',
    #     'B 1956-06-08 B 1968-01-14 B',
    #     'C 1956-06-08 C 01/14/1968 C'
    # ]
    matches = [
        regex.findall(string=item) for item in items
        if regex.findall(string=item)
    ]
    print(matches)
    # [
    #     ['06/08/1956', '01/14/1968'],
    #     ['1956-06-08', '1968-01-14'],
    #     ['1956-06-08', '01/14/1968']
    # ]
    matches = [item for sublist in matches for item in sublist]
    print(matches)
    # [
    #     '06/08/1956', '01/14/1968',
    #     '1956-06-08', '1968-01-14',
    #     '1956-06-08', '01/14/1968'
    # ]


if __name__ == "__main__":
    main()
