#! /usr/bin/env python3
"""
Convert a directory of csv files to feather files.
"""

from pathlib import Path
import time

import datasense as ds


def main():
    # define parameters
    title_ask_directory_feather = "Directory of feather files?"
    title_ask_directory_csv = "Directory of csv files?"
    initialdir = Path(__file__).parent.resolve()
    output_url = "convert_csv_to_feather.html"
    header_title = "Convert .csv to .feather"
    header_id = "convert-csv-to-feather"
    extension_out = ".feather"
    extension_in = [".csv"]
    # create html report
    original_stdout = ds.html_begin(
        output_url=output_url, header_title=header_title, header_id=header_id
    )
    ds.script_summary(script_path=Path(__file__), action="started at")
    directory_csv_files = ds.ask_directory_path(
        title=title_ask_directory_csv, initialdir=initialdir, print_bool=True
    )
    directory_feather_files = ds.ask_directory_path(
        title=title_ask_directory_feather,
        initialdir=directory_csv_files,
        print_bool=True,
    )
    start_time = time.perf_counter()
    # create list of paths to read
    path_csv = Path(directory_csv_files)
    paths_in = ds.list_files(
        directory=path_csv, patterns=extension_in
    )
    print("List of .csv files")
    print(paths_in)
    print()
    # create list of paths to save
    paths_out = [
        Path(
            directory_feather_files, paths_in[count].name
        ).with_suffix(extension_out)
        for count, element in enumerate(paths_in)
    ]
    print("List of .feather files")
    print()
    print(paths_out)
    print()
    # convert csv to feather
    for path_in, path_out in zip(paths_in, paths_out):
        df = ds.read_file(file_name=path_in)
        ds.save_file(df=df, file_name=path_out)
    stop_time = time.perf_counter()
    # Save html file
    ds.script_summary(script_path=Path(__file__), action="finished at")
    ds.report_summary(start_time=start_time, stop_time=stop_time)
    ds.html_end(original_stdout=original_stdout, output_url=output_url)


if __name__ == "__main__":
    main()
