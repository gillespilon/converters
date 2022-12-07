#! /usr/bin/env python3
"""
Code to delete rows based on various criteria.

dropna works for pd.NaT, np.NaN, and None. It does not work for "" which
occurs in csv files from Excel.

isin in combination with loc works for pd.NaT, np.NaN, None, and "".`
"""

from pathlib import Path
import textwrap
import time

import datasense as ds
import pandas as pd
import numpy as np


def main():
    output_url = "delete_rows.html"
    header_title = "Delete rows"
    header_id = "delete-rows"
    columns_to_check = ["integers", "floats", "text"]
    empty_items = [np.NaN, pd.NaT, None, ""]
    start_time = time.perf_counter()
    original_stdout = ds.html_begin(
        output_url=output_url,
        header_title=header_title,
        header_id=header_id
    )
    ds.script_summary(
        script_path=Path(__file__),
        action="started at"
    )
    print("dropna")
    print("------")
    print()
    print(
        "dropna works for pd.NaT, np.NaN, and None. "
        "It does not work for '' which "
        "occurs in csv files from Excel."
    )
    print()
    df = pd.DataFrame(
        dict(
            integers=[1, 2, 3, 4, 5, 6, 7],
            floats=[1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0],
            text=["A", "B", "C", "D", "E", "F", "G"],
            dates=[
                pd.Timestamp("1956-06-08"), pd.Timestamp("1956-06-08"),
                pd.Timestamp("1956-06-08"), pd.Timestamp("1956-06-08"),
                pd.Timestamp("1956-06-08"), pd.Timestamp("1956-06-08"),
                pd.Timestamp("1956-06-08")
            ],
            all_nan=[np.NaN, np.NaN, np.NaN, np.NaN, np.NaN, np.NaN, np.NaN],
            all_nat=[pd.NaT, pd.NaT, pd.NaT, pd.NaT, pd.NaT, pd.NaT, pd.NaT],
            all_none=[None, None, None, None, None, None, None],
            all_space=["", "", "", "", "", "", ""],
            nan_space=[np.NaN, "", np.NaN, np.NaN, np.NaN, np.NaN, np.NaN],
            nan_none=[np.NaN, None, np.NaN, np.NaN, None, np.NaN, None],
            mixed=[None, np.NaN, pd.NaT, pd.NaT, None, np.NaN, pd.NaT]
        )
    )
    print(df)
    print()
    print("Delete columns where all elements are missing.")
    print()
    print(textwrap.dedent("""
        df = df.dropna(
            axis="columns",
            how="all"
        )
    """))
    df = df.dropna(
        axis="columns",
        how="all"
    )
    print(df)
    print()
    stop_time = time.perf_counter()
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
        output_url=output_url
    )


if __name__ == "__main__":
    main()
