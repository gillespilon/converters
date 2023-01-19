#! /usr/bin/env python3
"""
Examples of using blake2.py module

Requires datasense:
- https://github.com/gillespilon/datasense
"""

from pyblake2 import blake2b
from pathlib import Path

import datasense as ds


def main():
    STRING_01_02 = b"Nobody inspects the spammish repetition"
    STRING_02 = b" the spammish repetition"
    PATH_EXCEL_FILE = Path("<file>.xlsx")
    OUTPUT_URL = "blake2_hashing.html"
    PATH_PDF_FILE = Path("<file>.pdf")
    PATH_PNG_FILE = Path("<file>.png")
    PATH_SVG_FILE = Path("<file>.svg")
    HEADER_TITLE = "Blake2 hashing"
    STRING_01 = b"Nobody inspects"
    HEADER_ID = "blake2-hashing"
    BLOCK_SIZE = 65536
    original_stdout = ds.html_begin(
        output_url=OUTPUT_URL,
        header_title=HEADER_TITLE,
        header_id=HEADER_ID
    )
    ds.script_summary(
        script_path=Path(__file__),
        action="started at"
    )
    # hash a single string with blake2
    hash_object = blake2b()
    hash_object.update(STRING_01)
    print("hash a single string with Blake2")
    print("string_01:", STRING_01)
    print(hash_object.hexdigest())
    print()
    # hash an additional, single string
    hash_object.update(STRING_02)
    print("hash an additional, single string")
    print("string_02:", STRING_02)
    print(hash_object.hexdigest())
    print()
    # hash two single strings
    hash_object = blake2b()
    hash_object.update(STRING_01)
    hash_object.update(STRING_02)
    print("hash two single strings with Blake2")
    print("string_01:", STRING_01)
    print("string_02:", STRING_02)
    print(hash_object.hexdigest())
    print()
    # hash the two single strings as one string
    hash_object = blake2b()
    hash_object.update(STRING_01_02)
    print("hash the two single strings as one string")
    print("string_01_02:", STRING_01_02)
    print(hash_object.hexdigest())
    print()
    # hash an svg file
    print("hash an svg file")
    hash_object = blake2b()
    with open(
        file=PATH_SVG_FILE,
        mode="rb"
    ) as f:
        hash_object.update(f.read(size=BLOCK_SIZE))
    print(PATH_SVG_FILE)
    print(hash_object.hexdigest())
    print()
    # hash a png file
    print("hash a png file")
    hash_object = blake2b()
    with open(
        file=PATH_PNG_FILE,
        mode="rb"
    ) as f:
        hash_object.update(f.read(size=BLOCK_SIZE))
    print(PATH_PNG_FILE)
    print(hash_object.hexdigest())
    print()
    # hash a pdf file
    print("hash a pdf file")
    hash_object = blake2b()
    with open(
        file=PATH_PDF_FILE,
        mode="rb"
    ) as f:
        hash_object.update(f.read(size=BLOCK_SIZE))
    print(PATH_PDF_FILE)
    print(hash_object.hexdigest())
    print()
    # hash an excel file
    print("hash an excel file")
    hash_object = blake2b()
    with open(
        file=PATH_EXCEL_FILE,
        mode="rb"
    ) as f:
        hash_object.update(f.read(size=BLOCK_SIZE))
    print(PATH_EXCEL_FILE)
    print(hash_object.hexdigest())
    print()
    # hash svg, png files
    print("hash svg, png files")
    path_svg_png_files = [PATH_SVG_FILE, PATH_PNG_FILE]
    hash_object = blake2b()
    for path in path_svg_png_files:
        with open(
            file=path,
            mode="rb"
        ) as f:
            hash_object.update(f.read(size=BLOCK_SIZE))
    print(path_svg_png_files)
    print(hash_object.hexdigest())
    print()
    # hash svg, png, pdf files
    print("hash svg, png, pdf files")
    path_svg_png_pdf_files = [PATH_SVG_FILE, PATH_PNG_FILE, PATH_PDF_FILE]
    hash_object = blake2b()
    for path in path_svg_png_pdf_files:
        with open(
            file=path,
            mode="rb"
        ) as f:
            hash_object.update(f.read(size=BLOCK_SIZE))
    print(path_svg_png_pdf_files)
    print(hash_object.hexdigest())
    print()
    # hash svg, png, pdf, Excel files
    print("hash svg, png, pdf, Excel files")
    path_svg_png_pdf_xlsx_files = [
        PATH_SVG_FILE, PATH_PNG_FILE, PATH_PDF_FILE, PATH_EXCEL_FILE
    ]
    hash_object = blake2b()
    for path in path_svg_png_pdf_xlsx_files:
        with open(
            file=path,
            mode="rb"
        ) as f:
            hash_object.update(f.read(size=BLOCK_SIZE))
    print(path_svg_png_pdf_xlsx_files)
    print(hash_object.hexdigest())
    print()
    ds.script_summary(
        script_path=Path(__file__),
        action="finished at"
    )
    ds.html_end(
        original_stdout=original_stdout,
        output_url=OUTPUT_URL
    )


if __name__ == "__main__":
    main()
