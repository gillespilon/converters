#! /usr/bin/env python3
"""
Create a QR code from a string.

Example
-------
./create_qr_code.py
"https://github.com/gillespilon"
/home/gilles/downloads/github_gilles_pilon

The above will produce two files:
/home/gilles/downloads/github_gilles_pilon.svg
/home/gilles/downloads/github_gilles_pilon.png
"""

from pathlib import Path

import datasense as ds


def main():
    qr_code_string = input("Enter QR code string: ")
    qr_code_path = Path(input("Enter QR code path  : "))
    # qr_code_type = input('Which file format ["svg", "png"]? ')
    ds.qr_code(qr_code_string=qr_code_string, qr_code_path=qr_code_path)


if __name__ == "__main__":
    main()
