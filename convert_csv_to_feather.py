#! /usr/bin/env python3
"""
Convert a directory of csv files to feather files.

Requires
- https://github.com/gillespilon/datasense
"""

from pathlib import Path
import time

import datasense as ds


def main():
    # define parameters
    TITLE_ASK_DIRECTORY_FEATHER = "Directory of feather files?"
    TITLE_ASK_DIRECTORY_CSV = "Directory of csv files?"
    initialdir = Path(__file__).parent.resolve()
    OUTPUT_URL = "convert_csv_to_feather.html"
    HEADER_TITLE = "Convert .csv to .feather"
    HEADER_ID = "convert-csv-to-feather"
    EXTENSION_OUT = ".feather"
    EXTENSION_IN = [".csv"]
    # create html report
    original_stdout = ds.html_begin(
        output_url=OUTPUT_URL,
        header_title=HEADER_TITLE,
        header_id=HEADER_ID
    )
    ds.script_summary(
        script_path=Path(__file__),
        action="started at"
    )
    directory_csv_files = ds.ask_directory_path(
        title=TITLE_ASK_DIRECTORY_CSV,
        initialdir=initialdir,
        print_bool=True
    )
    directory_feather_files = ds.ask_directory_path(
        title=TITLE_ASK_DIRECTORY_FEATHER,
        initialdir=directory_csv_files,
        print_bool=True,
    )
    start_time = time.perf_counter()
    # create list of paths to read
    path_csv = Path(directory_csv_files)
    paths_in = ds.list_files(
        directory=path_csv,
        pattern_extension=EXTENSION_IN
    )
    print("List of .csv files")
    print(paths_in)
    print()
    # create list of paths to save
    paths_out = [
        Path(
            directory_feather_files,
            paths_in[count].name
        ).with_suffix(suffix=EXTENSION_OUT)
        for count, element in enumerate(paths_in)
    ]
    print("List of .feather files")
    print()
    print(paths_out)
    print()
    # convert csv to feather
    ds.convert_csv_to_feather(
        paths_in=paths_in,
        paths_out=paths_out
    )
    stop_time = time.perf_counter()
    # Save html file
    ds.script_summary(
        script_path=Path(__file__),
        action="finished at"
    )
    ds.report_summary(
        start_time=start_time,
        stop_time=stop_time
    )
    ds.html_end(
        original_stdout=original_stdout,
        output_url=OUTPUT_URL
    )


if __name__ == "__main__":
    main()
