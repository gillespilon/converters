#! /usr/bin/env python3
"""
Diagnose a data file.

- Does not show all unique values because in a large file this could be huge.
- Reads .feather .csv files.
"""

from pathlib import Path
import time

import datasense as ds


def main():
    filetypes = [("csv and feather files", ".csv .CSV .feather .FEATHER")]
    path_in_title = "Select csv or feather file to read"
    initialdir = Path(__file__).parent.resolve()
    output_url = "describe_data_file.html"
    header_title = "Describe data file"
    header_id = "describe-data-file"
    original_stdout = ds.html_begin(
        output_url=output_url, header_title=header_title, header_id=header_id
    )
    path_in = ds.ask_open_file_name_path(
        title=path_in_title, initialdir=initialdir, filetypes=filetypes
    )
    start_time = time.time()
    data = ds.read_file(file_name=path_in)
    ds.dataframe_info(df=data, file_in=path_in, unique_bool=True)
    stop_time = time.time()
    ds.report_summary(
        start_time=start_time,
        stop_time=stop_time,
    )
    ds.html_end(original_stdout=original_stdout, output_url=output_url)


if __name__ == "__main__":
    main()
