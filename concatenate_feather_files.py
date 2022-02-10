#! /usr/bin/env python3
"""
Concatenate a folder of feather files to create a single feather file.
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
    title_ask_directory_feather = "Directory of feather files?"
    header_title = "Concatenate directory of feather files"
    initialdir = Path(__file__).parent.resolve()
    directory_feather_files = ds.ask_directory_path(
        title=title_ask_directory_feather,
        initialdir=initialdir,
        print_bool=True
    )
    output_url = "concatenate_feather_files.html"
    path_file_out = Path("concatenate_feather_files.feather").resolve()
    header_id = "concatenate-feather-files"
    extension = ".feather"
    skiprows = 0
    header = 0
    start_time_1 = time.time()
    original_stdout = ds.html_begin(
        output_url=output_url, header_title=header_title, header_id=header_id
    )
    ds.script_summary(script_path=Path(__file__), action="started at")
    # create list of paths to read
    files = ds.directory_file_list(
        directory=directory_feather_files, patterns=[extension]
    )
    # create DataFrame from list of paths
    df = (
        pd.concat(
            objs=[
                ds.read_file(file_name=item, header=header, skiprows=skiprows)
                for item in files
            ]
        )
        .drop_duplicates()
        .dropna(how="any")
    )
    # save as feather file
    ds.save_file(
        df=df, file_name=path_file_out.with_suffix(extension), index=False
    )
    print("path_directory_files_in:")
    print(directory_feather_files)
    print()
    files_sorted = [x.name for x in files]
    print("Files in directory", directory_feather_files)
    print(files_sorted)
    print()
    print("path_file_out:")
    print(path_file_out)
    size_int = ds.file_size(path=path_file_out)
    size_str = ds.byte_size(num=size_int)
    print("is", size_str, "with", df.shape[0], "rows.")
    print()
    stop_time_1 = time.time()
    ds.script_summary(script_path=Path(__file__), action="finished at")
    print(f"Execution time: {round(stop_time_1 - start_time_1, 6)} s")
    print()
    ds.html_end(original_stdout=original_stdout, output_url=output_url)


if __name__ == "__main__":
    main()
