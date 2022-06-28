#! /usr/bin/env python3
"""
Use Python re to match hexadecimal strings from a list or tuple of strings.
"""

import re


def main():
    items = [
        "Text ffffff + 0xffffff & 0Xffffff.",
        "ffffff", "0xffffff", "0Xffffff"
    ]
    # items = (
    #     "Text ffffff + 0xffffff & 0Xffffff.",
    #     "ffffff", "0xffffff", "0Xffffff"
    # )
    pattern = r"\b[0|(xX)]?[a-fA-FxX0-9]{6,8}\b"
    regex = re.compile(pattern=pattern)
    matches = [item for item in items if regex.search(string=item)]
    print(matches)
    # ['Text ffffff + 0xffffff & 0Xffffff.', 'ffffff', '0xffffff', '0Xffffff']
    matches = [
        regex.findall(string=item) for item in items
        if regex.search(string=item)
    ]
    print(matches)
    # [
    #     ['ffffff', '0xffffff', '0Xffffff'],
    #     ['ffffff'], ['0xffffff'], ['0Xffffff']
    #    ]
    matches = [item for sublist in matches for item in sublist]
    print(matches)
    # ['ffffff', '0xffffff', '0Xffffff', 'ffffff', '0xffffff', '0Xffffff']


if __name__ == "__main__":
    main()
