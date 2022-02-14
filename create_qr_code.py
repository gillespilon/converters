#! /usr/bin/env python3
"""
Create a QR code from a string.
"""

from pathlib import Path
from typing import NoReturn
import pyqrcode as pq


def main():
    qr_code_string = input("Enter QR code string: ")
    qr_code_path = input("Enter QR code path  : ")
    # qr_code_type = input('Which file format ["svg", "png"]? ')
    create_code(qr_code_string=qr_code_string, qr_code_path=qr_code_path)


def create_code(qr_code_string: str, qr_code_path: str) -> NoReturn:
    """
    Create a QR code and save as .svg and .png.

    Parameters
    ----------
    qr_code_string : str
        Text for the QR code
    qr_code_path : str
        Text for the path

    Example
    -------
    >>> python create_qr_code.py
    >>> Enter QR code string: https://github.com/gillespilon
    >>> Enter QR code path  : ~/downloads/mygithuburl
    """
    pq.create(content=qr_code_string).svg(
        Path(qr_code_path).with_suffix(".svg"), scale=4
    )
    pq.create(content=qr_code_string).png(
        Path(qr_code_path).with_suffix(".png"), scale=4
    )


if __name__ == "__main__":
    main()
