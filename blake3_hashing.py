#! /usr/bin/env python3
"""
Examples of using blake3.py module

Requires datasense:
- https://github.com/gillespilon/datasense
"""

from pathlib import Path
from blake3 import blake3

import datasense as ds


def main():
    STRING_01_02 = b"Nobody inspects the spammish repetition"
    STRING_02 = b" the spammish repetition"
    OUTPUT_URL = "blake3_hashing.html"
    HEADER_TITLE = "Blake3 hashing"
    STRING_01 = b"Nobody inspects"
    HEADER_ID = "blake3-hashing"
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
    # hash a single string with blake3
    hash_object = blake3()
    hash_object.update(STRING_01)
    print("hash a single string with Blake3")
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
    hash_object = blake3()
    hash_object.update(STRING_01)
    hash_object.update(STRING_02)
    print("hash two single strings with Blake3")
    print("string_01:", STRING_01)
    print("string_02:", STRING_02)
    print(hash_object.hexdigest())
    print()
    # hash the two single strings as one string
    hash_object = blake3()
    hash_object.update(STRING_01_02)
    print("hash the two single strings as one string")
    print("string_01_02:", STRING_01_02)
    print(hash_object.hexdigest())
    print()
    # hash an svg file
    print("hash an svg file")
    path_svg_file = Path("<file>.svg")
    hash_object = blake3()
    with open(
        file=path_svg_file,
        mode="rb"
    ) as f:
        hash_object.update(f.read(size=BLOCK_SIZE))
    print(path_svg_file)
    print(hash_object.hexdigest())
    print()
    # hash a png file
    print("hash a png file")
    path_png_file = Path("<file>.png")
    hash_object = blake3()
    with open(
        file=path_png_file,
        mode="rb"
    ) as f:
        hash_object.update(f.read(size=BLOCK_SIZE))
    print(path_png_file)
    print(hash_object.hexdigest())
    print()
    # hash a pdf file
    print("hash a pdf file")
    path_pdf_file = Path("<file>.pdf")
    hash_object = blake3()
    with open(
        file=path_pdf_file,
        mode="rb"
    ) as f:
        hash_object.update(f.read(size=BLOCK_SIZE))
    print(path_pdf_file)
    print(hash_object.hexdigest())
    print()
    # hash an excel file
    print("hash an excel file")
    path_excel_file = Path("<file>.xlsx")
    hash_object = blake3()
    with open(
        file=path_excel_file,
        mode="rb"
    ) as f:
        hash_object.update(f.read(size=BLOCK_SIZE))
    print(path_excel_file)
    print(hash_object.hexdigest())
    print()
    # hash svg, png files
    print("hash svg, png files")
    path_svg_png_files = [path_svg_file, path_png_file]
    hash_object = blake3()
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
    path_svg_png_pdf_files = [path_svg_file, path_png_file, path_pdf_file]
    hash_object = blake3()
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
        path_svg_file, path_png_file, path_pdf_file, path_excel_file
    ]
    hash_object = blake3()
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
