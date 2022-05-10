#! /usr/bin/env python3
"""
Examples of using blake2.py module
"""

from pathlib import Path
from pyblake2 import blake2b

import datasense as ds


def main():
    output_url = "blake2_hashing.html"
    header_title = "Blake2 hashing"
    header_id = "blake2-hashing"
    block_size = 65536
    original_stdout = ds.html_begin(
        output_url=output_url, header_title=header_title, header_id=header_id
    )
    ds.script_summary(script_path=Path(__file__), action="started at")
    # hash a single string with blake2
    string_01 = b"Nobody inspects"
    hash_object = blake2b()
    hash_object.update(string_01)
    print("hash a single string with Blake2")
    print("string_01:", string_01)
    print(hash_object.hexdigest())
    print()
    # hash an additional, single string
    string_02 = b" the spammish repetition"
    hash_object.update(string_02)
    print("hash an additional, single string")
    print("string_02:", string_02)
    print(hash_object.hexdigest())
    print()
    # hash two single strings
    hash_object = blake2b()
    string_01 = b"Nobody inspects"
    string_02 = b" the spammish repetition"
    hash_object.update(string_01)
    hash_object.update(string_02)
    print("hash two single strings with Blake2")
    print("string_01:", string_01)
    print("string_02:", string_02)
    print(hash_object.hexdigest())
    print()
    # hash the two single strings as one string
    hash_object = blake2b()
    string_01_02 = b"Nobody inspects the spammish repetition"
    hash_object.update(string_01_02)
    print("hash the two single strings as one string")
    print("string_01_02:", string_01_02)
    print(hash_object.hexdigest())
    print()
    # hash an svg file
    print("hash an svg file")
    path_svg_file = Path("<file>.svg")
    hash_object = blake2b()
    with open(file=path_svg_file, mode="rb") as f:
        hash_object.update(f.read(block_size))
    print(path_svg_file)
    print(hash_object.hexdigest())
    print()
    # hash a png file
    print("hash a png file")
    path_png_file = Path("<file>.png")
    hash_object = blake2b()
    with open(file=path_png_file, mode="rb") as f:
        hash_object.update(f.read(block_size))
    print(path_png_file)
    print(hash_object.hexdigest())
    print()
    # hash a pdf file
    print("hash a pdf file")
    path_pdf_file = Path("<file>.pdf")
    hash_object = blake2b()
    with open(file=path_pdf_file, mode="rb") as f:
        hash_object.update(f.read(block_size))
    print(path_pdf_file)
    print(hash_object.hexdigest())
    print()
    # hash an excel file
    print("hash an excel file")
    path_excel_file = Path("<file>.xlsx")
    hash_object = blake2b()
    with open(file=path_excel_file, mode="rb") as f:
        hash_object.update(f.read(block_size))
    print(path_excel_file)
    print(hash_object.hexdigest())
    print()
    # hash svg, png files
    print("hash svg, png files")
    path_svg_png_files = [path_svg_file, path_png_file]
    hash_object = blake2b()
    for path in path_svg_png_files:
        with open(file=path, mode="rb") as f:
            hash_object.update(f.read(block_size))
    print(path_svg_png_files)
    print(hash_object.hexdigest())
    print()
    # hash svg, png, pdf files
    print("hash svg, png, pdf files")
    path_svg_png_pdf_files = [path_svg_file, path_png_file, path_pdf_file]
    hash_object = blake2b()
    for path in path_svg_png_pdf_files:
        with open(file=path, mode="rb") as f:
            hash_object.update(f.read(block_size))
    print(path_svg_png_pdf_files)
    print(hash_object.hexdigest())
    print()
    # hash svg, png, pdf, Excel files
    print("hash svg, png, pdf, Excel files")
    path_svg_png_pdf_xlsx_files = [
        path_svg_file, path_png_file, path_pdf_file, path_excel_file
    ]
    hash_object = blake2b()
    for path in path_svg_png_pdf_xlsx_files:
        with open(file=path, mode="rb") as f:
            hash_object.update(f.read(block_size))
    print(path_svg_png_pdf_xlsx_files)
    print(hash_object.hexdigest())
    print()
    ds.script_summary(script_path=Path(__file__), action="finished at")
    ds.html_end(original_stdout=original_stdout, output_url=output_url)


if __name__ == "__main__":
    main()
