#! /usr/bin/env python3
"""
Move directories to keep history.

Before running this script:
- create a .txt file with the names of the source directories
- create a .txt file with the names of the destination directories
All of the above directories must exist.
"""

from pathlib import Path

import datasense as ds


def main():
    sources = input("file with source directories      : ")
    destinations = input("file with destination directories : ")
    with Path(sources).open() as f:
        lines = f.readlines()
        sources = [Path(line.rstrip("\n")).resolve() for line in lines]
    with Path(destinations).open() as f:
        lines = f.readlines()
        destinations = [Path(line.rstrip("\n")).resolve() for line in lines]
    if len(sources) == len(destinations):
        ds.rename_directory(sources=sources, destinations=destinations)
        ds.copy_directory(
            sources=[destinations[len(destinations) - 1]],
            destinations=[sources[len(sources) - 1]],
        )
    else:
        print()
        print("number source directories <> number destination directories")
        print()
        print("source directories:")
        print(sources)
        print()
        print("destination directories:")
        print(destinations)


if __name__ == "__main__":
    main()
