#! /usr/bin/env python3
"""
Using bash commands in Python script.
"""

from pathlib import Path

import datasense as ds


def main():
    directories_new = ["directory_07", "directory_13", "directory_69"]
    directories_old = ["directory_13", "directory_69"]
    # create a list of empty directories
    ds.create_directory(directories=directories_new)
    # delete list of directories
    ds.delete_directory(directories=directories_old)


if __name__ == '__main__':
    main()
