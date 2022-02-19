#! /usr/bin/env python3
"""
Using bash commands in Python script.
"""

from pathlib import Path

import datasense as ds


def main():
    directories_create = ["directory_07", "directory_13", "directory_69"]
    directories_delete = ["directory_13", "directory_69"]
    directories_old_name = ["directory_07"]
    directories_new_name = ["directory_77"]
    # create a list of empty directories
    ds.create_directory(directories=directories_create)
    # delete list of directories
    ds.delete_directory(directories=directories_delete)
    # rename directories
    ds.rename_directory(
        sources=directories_old_name, destinations=directories_new_name
    )


if __name__ == '__main__':
    main()
