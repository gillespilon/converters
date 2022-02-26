#! /usr/bin/env python3
"""
Get country codes, names, domains from Wikipedia table and create file.
"""

#  code to prevent shell from closing on error when using cron, Task Scheduler
import sys


def excepthook(*args, **kwargs):
    """
    Diagnose missing packages.
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
    wiki_url = "https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2"
    output_url = "country_codes_names_domains.html"
    header_title = "Country codes, names, domains"
    column_labels = ["Code", "Country", "Domain"]
    path_file_out = Path("country_codes.feather")
    # path_file_out = Path("country_codes.csv")
    header_id = "country-codes-names-domains"
    drop_columns = ["Year", "Notes"]
    original_stdout = ds.html_begin(
        output_url=output_url, header_title=header_title, header_id=header_id
    )
    ds.script_summary(script_path=Path(__file__), action="started at")
    start_time = time.perf_counter()
    # create DataFrame from Wikipedia table
    data = (
        pd.DataFrame(
            data=pd.read_html(
                io=wiki_url,
                attrs={"class": "wikitable sortable"},
                keep_default_na=False,
            )[0]
        )
        .drop(labels=drop_columns, axis="columns")
        .set_axis(labels=column_labels, axis="columns")
    )
    # save DataFrame as csv file
    ds.save_file(df=data, file_name=path_file_out)
    print(data)
    print()
    stop_time = time.perf_counter()
    ds.script_summary(script_path=Path(__file__), action="finished at")
    ds.report_summary(
        start_time=start_time,
        stop_time=stop_time,
        save_file_names=path_file_out.resolve(),
    )
    ds.html_end(original_stdout=original_stdout, output_url=output_url)


if __name__ == "__main__":
    main()
