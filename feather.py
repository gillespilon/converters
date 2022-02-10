#! /usr/bin/env python3
"""
Explore reading and writing the feather file format.

Feather is a language-agnostic data frame file format. It was designed by
Wes McKiney (the creator of pandas) and Hadley Wickham (chief scientist at
RStudio). Wes created bindings for Python and Hadley created bindings for R.

https://github.com/wesm/feather
https://arrow.apache.org/
"""

from pathlib import Path
import time

import datasense as ds


def main():
    start_time = time.time()
    # define parameters
    feather_file = 'feather.feather'
    header_title = 'Feather tests'
    output_url = 'feather.html'
    number_rows = 1000000
    header_id = 'feather'
    # create html report
    original_stdout = ds.html_begin(
        output_url=output_url,
        header_title=header_title,
        header_id=header_id
    )
    ds.script_summary(
        script_path=Path(__file__),
        action='started at'
    )
    path_feather = Path(feather_file)
    # create DataFrame
    df = ds.create_dataframe_norm(row_count=number_rows)
    # save df to feather
    ds.save_file(df=df, file_name=feather_file)
    print("path feather file out:")
    print(path_feather)
    size_int = ds.file_size(path=path_feather)
    size_str = ds.byte_size(num=size_int)
    print(
        "is", size_str, "with", df.shape[0], "rows by", df.shape[1], "columns"
    )
    print()
    # read feather file into DataFrame
    df = ds.read_file(file_name=path_feather)
    print("path feather file in:")
    print(path_feather)
    size_int = ds.file_size(path=path_feather)
    size_str = ds.byte_size(num=size_int)
    print(
        "is", size_str, "with", df.shape[0], "rows by", df.shape[1], "columns"
    )
    print()
    stop_time = time.time()
    # Save html file
    ds.script_summary(
        script_path=Path(__file__),
        action='finished at'
    )
    ds.report_summary(
        start_time=start_time,
        stop_time=stop_time
    )
    ds.html_end(
        original_stdout=original_stdout,
        output_url=output_url
    )


if __name__ == '__main__':
    main()
