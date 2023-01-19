#! /usr/bin/env python3
"""
Concatenate a folder of feather files to create a single feather file.

Requires
- https://github.com/gillespilon/datasense
"""

# code to prevent shell from closing on error when using cron, Task Scheduler
import sys


def excepthook(*args, **kwargs):
    """
    Diagnose missing packages.
    This is used because the main script is executed by Task Scheduler.
    """
    print(*args, kwargs)
    from traceback import print_tb

    print_tb(args[2])
    input("Press <Enter> to exit.")


sys.excepthook = excepthook


from pathlib import Path
from os import chdir
import time

import datasense as ds
import pandas as pd


def main():
    # required for cron
    chdir(Path(__file__).parent.resolve())
    # define parameters
    PATH_FILE_OUT = Path("concatenate_feather_files.feather").resolve()
    TITLE_ASK_DIRECTORY_FEATHER = "Directory of feather files?"
    HEADER_TITLE = "Concatenate directory of feather files"
    OUTPUT_URL = "concatenate_feather_files.html"
    HEADER_ID = "concatenate-feather-files"
    EXTENSION = ".feather"
    SKIPROWS = 0
    HEADER = 0
    initialdir = Path(__file__).parent.resolve()
    directory_feather_files = ds.ask_directory_path(
        title=TITLE_ASK_DIRECTORY_FEATHER,
        initialdir=initialdir,
        print_bool=True
    )
    start_time_1 = time.perf_counter()
    original_stdout = ds.html_begin(
        output_url=OUTPUT_URL,
        header_title=HEADER_TITLE,
        header_id=HEADER_ID
    )
    ds.script_summary(
        script_path=Path(__file__),
        action="started at"
    )
    # create list of paths to read
    files = ds.list_files(
        directory=directory_feather_files,
        pattern_extension=[EXTENSION]
    )
    # create DataFrame from list of paths
    df = (
        pd.concat(
            objs=[
                ds.read_file(
                    file_name=item,
                    header=HEADER,
                    skiprows=SKIPROWS
                )
                for item in files
            ]
        )
        .drop_duplicates()
        .dropna(
            axis="index",
            how="any"
        )
    )
    # save as feather file
    ds.save_file(
        df=df,
        file_name=PATH_FILE_OUT.with_suffix(suffix=EXTENSION),
        index=False
    )
    print("path_directory_files_in:")
    print(directory_feather_files)
    print()
    files_sorted = [x.name for x in files]
    print("Files in directory", directory_feather_files)
    print(files_sorted)
    print()
    print("path_file_out:")
    print(PATH_FILE_OUT)
    size_int = ds.file_size(path=PATH_FILE_OUT)
    size_str = ds.byte_size(num=size_int)
    print("is", size_str, "with", df.shape[0], "rows.")
    print()
    stop_time_1 = time.perf_counter()
    ds.script_summary(
        script_path=Path(__file__),
        action="finished at"
    )
    print(f"Execution time: {round(stop_time_1 - start_time_1, 6)} s")
    print()
    ds.html_end(
        original_stdout=original_stdout,
        output_url=OUTPUT_URL
    )


if __name__ == "__main__":
    main()
