#! /usr/bin/env python3
"""
Using bash commands in Python script.
"""

from pathlib import Path

import datasense as ds


def main():
    directories = ["directory_13", "directory_69"]
    # create a list of empty directories
    ds.create_directory(directories=directories)


if __name__ == '__main__':
    main()
