#! /usr/bin/env python3
"""
Code to delete rows based on various criteria.

dropna works for pd.NaT, np.NaN, and None. It does not work for "" which
occurs in csv files from Excel.

isna and notna work for pd.NaT, np.NaN, and None. They do not work for "".

isin in combination with loc works for pd.NaT, np.NaN, None, and "".`
"""

from pathlib import Path
import textwrap
import time

import datasense as ds
import pandas as pd
import numpy as np


def main():
    columns_to_check = ["integers", "floats", "text"]
    empty_items = [np.NaN, pd.NaT, None, ""]
    output_url = "delete_rows.html"
    header_title = "Delete rows"
    header_id = "delete-rows"
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
    print(
        "Delete rows where all elements are missing. It fails to delete row 3."
    )
    print()
    df = pd.DataFrame(
        dict(
            integers=[1, 2, 3, None, 5, 6, np.NaN],
            floats=[1.0, None, 3.0, np.NaN, 5.0, 6.0, np.NaN],
            text=["A", "B", "C", "", "", "F", None],
            dates=[
                pd.Timestamp("1956-06-08"), pd.Timestamp("1956-06-08"),
                pd.Timestamp("1956-06-08"), pd.NaT,
                pd.Timestamp("1956-06-08"), pd.Timestamp("1956-06-08"),
                None
            ],
            all_nan=[np.NaN, np.NaN, np.NaN, np.NaN, np.NaN, np.NaN, np.NaN],
            all_nat=[pd.NaT, pd.NaT, pd.NaT, pd.NaT, pd.NaT, pd.NaT, pd.NaT],
            all_none=[None, None, None, None, None, None, None],
            # all_space=["", "", "", "", "", "", ""],
            nan_space=[np.NaN, np.NaN, np.NaN, "", np.NaN, np.NaN, np.NaN],
            nan_none=[np.NaN, None, np.NaN, np.NaN, None, np.NaN, None],
            mixed=[None, np.NaN, pd.NaT, pd.NaT, None, np.NaN, pd.NaT]
        )
    )
    print(df)
    print()
    print(textwrap.dedent("""
        df = df.dropna(
            axis="index",
            how="all"
        )
    """))
    df = df.dropna(
        axis="index",
        how="all"
    )
    print(df)
    print()
    print(
        "Delete rows where at least one element missing. "
        "It fails to delete rows 2 and 4."
    )
    print()
    df = pd.DataFrame(
        dict(
            integers=[1, 2, "", None, 5, 6, np.NaN],
            floats=[1.0, None, "", np.NaN, 5.0, 6.0, np.NaN],
            text=["A", "B", "", pd.NaT, "", "F", None]
        )
    )
    print(df)
    print()
    print(textwrap.dedent("""
        df = df.dropna(
            axis="index",
            how="any"
        )
    """))
    df = df.dropna(
        axis="index",
        how="any"
    )
    print(df)
    print()
    print(
        "Delete rows where there are less than four non-missing elements. "
        "It fails to delete row 4."
    )
    print()
    df = pd.DataFrame(
        dict(
            integers=[1, 2, 3, None, 5, 6, np.NaN],
            floats=[1.0, None, 3.0, 4.0, 5.0, 6.0, np.NaN],
            text=["A", "B", "C", "D", "", "F", "G"],
            dates=[
                pd.Timestamp("1956-06-08"), pd.Timestamp("1956-06-08"),
                pd.Timestamp("1956-06-08"), pd.Timestamp("1956-06-08"),
                pd.Timestamp("1956-06-08"), pd.Timestamp("1956-06-08"),
                None
            ],
        )
    )
    print(df)
    print()
    print(textwrap.dedent("""
        df = df.dropna(
            axis="index",
            thresh=4
        )
    """))
    df = df.dropna(
        axis="index",
        thresh=4
    )
    print(df)
    print()
    print(
        "Delete rows where all elements are missing, in specific columns. "
        "It fails to delete rows 1 and 3."
    )
    print()
    df = pd.DataFrame(
        dict(
            integers=[1, np.NaN, 3, 4, 5, 6, np.NaN],
            floats=[1.0, np.NaN, 3.0, 4.0, 5.0, 6.0, np.NaN],
            text=["A", "", "C", "", "E", "F", None],
            dates=[
                pd.Timestamp("1956-06-08"), pd.NaT,
                pd.Timestamp("1956-06-08"), pd.Timestamp("1956-06-08"),
                pd.NaT, pd.Timestamp("1956-06-08"),
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
    print(textwrap.dedent("""
        columns_to_check = ["integers", "floats", "text"]
        df = df.dropna(
            how="all",
            subset=columns_to_check
        )
    """))
    dfa = df.copy()
    dfa = dfa.dropna(
        how="all",
        subset=columns_to_check
    )
    print(dfa)
    print()
    print(
        "Delete rows where at least one element is missing, "
        "in specific columns. It fails to delete row 3."
    )
    print()
    print(df)
    print()
    print(textwrap.dedent("""
        columns_to_check = ["integers", "floats", "text"]
        df = df.dropna(
            how="any",
            subset=columns_to_check
        )
    """))
    dfa = df.copy()
    dfa = dfa.dropna(
        how="any",
        subset=columns_to_check
    )
    print(dfa)
    print()
    print("isna, notna")
    print("------")
    print()
    print(
        "isna works for pd.NaT, np.NaN, and None. "
        "It does not work for ''. "
        "all_space and non_space should be all True."
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
    print(textwrap.dedent("""
        df = df.isna()
    """))
    dfa = df.copy()
    dfa = dfa.isna()
    print(dfa)
    print()
    print(
        "notna works for pd.NaT, np.NaN, and None. "
        "It does not work for ''. "
        "all_space and non_space should be all False."
    )
    print()
    print(df)
    print()
    print(textwrap.dedent("""
        df = df.notna()
    """))
    dfa = df.copy()
    dfa = dfa.notna()
    print(dfa)
    print()
    print("loc, isin")
    print("---------")
    print()
    print("Delete rows where all elements are missing.")
    print()
    df = pd.DataFrame(
        dict(
            integers=[1, 2, 3, 4, 5, np.NaN, 7],
            floats=[1.0, 2.0, 3.0, 4.0, 5.0, np.NaN, 7.0],
            text=["A", "", "", "D", "", "", "G"],
            dates=[
                pd.Timestamp("1956-06-08"), pd.Timestamp("1956-06-08"),
                pd.NaT, pd.Timestamp("1956-06-08"),
                pd.Timestamp("1956-06-08"), pd.NaT,
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
    print(textwrap.dedent("""
        df.loc[~(df.shape[1] == df.isin(empty_items).sum(axis=1)), :]
    """))
    dfa = df.copy()
    dfa = dfa.loc[~(dfa.shape[1] == dfa.isin(empty_items).sum(axis=1)), :]
    print(dfa)
    print()
    print("Delete rows where 8 or more elements are missing missing.")
    print()
    print(df)
    print()
    print(textwrap.dedent("""
        df.loc[~((df.isin(empty_items).sum(axis=1)) >= 8), :]
    """))
    dfa = df.copy()
    dfa = dfa.loc[~((dfa.isin(empty_items).sum(axis=1)) >= 8), :]
    print(dfa)
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