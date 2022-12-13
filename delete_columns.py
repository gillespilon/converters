#! /usr/bin/env python3
"""
Code to delete columns based on various criteria.
"""

from pathlib import Path
import textwrap
import time

# from tabulate import tabulate
import datasense as ds
import pandas as pd
import numpy as np


def main():
    output_url = "delete_columns.html"
    header_title = "Delete columns"
    header_id = "delete-columns"
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
    df = pd.DataFrame(
        data=dict(
            floats=[1.0, np.NaN, 3.0, np.NaN, 5.0, 6.0, np.NaN],
            text=["A", "B", "C", "D", "E", "F", np.NaN],
            dates=[
                "1956-06-08", "1956-06-08",
                "1956-06-08", "1956-06-08",
                "1956-06-08", "1956-06-08",
                pd.NaT
            ],
            all_nan=[np.NaN, np.NaN, np.NaN, np.NaN, np.NaN, np.NaN, np.NaN],
            all_nat=[pd.NaT, pd.NaT, pd.NaT, pd.NaT, pd.NaT, pd.NaT, pd.NaT],
            all_none=[None, None, None, None, None, None, None],
            all_space=["", " ", "", " ", "", "", ""],
            nan_space=[np.NaN, "", " ", np.NaN, np.NaN, np.NaN, np.NaN],
            nan_none=[np.NaN, None, np.NaN, np.NaN, None, np.NaN, None],
            mixed=[None, np.NaN, pd.NaT, pd.NaT, None, np.NaN, pd.NaT],
            integers=[1, 2, np.NaN, 4, 5, 6, np.NaN],
        )
    ).replace(
        r"^\s+$",
        np.NaN,
        regex=True
    ).replace(
        "",
        np.NaN,
        regex=True
    ).astype(
        dtype={
            "integers": "Int64",
            "floats": "float64",
            "text": "object",
            "dates": "datetime64[ns]",
            "all_nan": "float64",
            "all_nat": "datetime64[ns]",
            "all_none": "float64",
            "all_space": "float64",
            "nan_space": "float64",
            "nan_none": "float64",
            "mixed": "datetime64[ns]"
        }
    )
    print("DataFrame used in all code examples")
    print()
    print(df)
    print()
    print("Replace spaces and other missing value types in the DataFrame.")
    print(textwrap.dedent("""
        df.replace(
            r"^\s+$",
            np.NaN,
            regex=True
        ).replace(
            "",
            np.NaN,
            regex=True
        )
    """))
    print("Check the column data types")
    print()
    print("df.dtypes")
    print()
    print(df.dtypes)
    print()
    print("Check for the presence of null-type values")
    print()
    print("df.isna()")
    print()
    print(df.isna())
    print()
    print("Check for the presence of non-null-type values")
    print()
    print("df.notna()")
    print()
    print(df.notna())
    print()
    print("dropna")
    print("------")
    print()
    print("Delete columns where all elements are missing.")
    print(textwrap.dedent("""
        df = df.dropna(
            axis="columns",
            how="all"
        )
    """))
    dfa = df.copy()
    dfa = dfa.dropna(
        axis="columns",
        how="all"
    )
    print(dfa)
    print()
    print("Delete columns where at least one element missing.")
    dfa = df.copy()
    print(textwrap.dedent("""
        df = df.dropna(
            axis="columns",
            how="any"
        )
    """))
    dfa = dfa.dropna(
        axis="columns",
        how="any"
    )
    print(dfa)
    print()
    print(
        "Delete columns where there are less than five non-missing elements."
    )
    print()
    print(textwrap.dedent("""
        df = df.dropna(
            axis="columns",
            thresh=5
        )
    """))
    dfa = df.copy()
    dfa = dfa.dropna(
        axis="columns",
        thresh=5
    )
    print(dfa)
    print()
    print("loc, isna")
    print("---------")
    print()
    print("Delete columns where all elements are missing.")
    print()
    print("df.loc[:, ~df.isna().all()]")
    print()
    dfa = df.copy()
    dfa = dfa.loc[:, ~dfa.isna().all()]
    print(dfa)
    print()
    print("Delete columns where at least one element missing.")
    print(textwrap.dedent("""
        df.loc[:, ~df.isna().any()]
        df.loc[:, ~(df.isna().sum() != 0)]
    """))
    dfa = df.copy()
    dfa = dfa.loc[:, ~dfa.isna().any()]
    # df = df.loc[:, ~(df.isna().sum() != 0)]
    print(dfa)
    print()
    print("Delete columns where three or more elements are missing.")
    print()
    print("df.loc[:, ~(df.isna().sum() >= 3)]")
    print()
    dfa = df.copy()
    dfa = dfa.loc[:, ~(dfa.isna().sum() >= 3)]
    print(dfa)
    print()
    print("Keep columns where at least four elements are not missing.")
    print()
    print("df.loc[:, ((len(df) - df.isna().sum()) >= 4)]")
    print()
    dfa = df.copy()
    dfa = dfa.loc[:, ((len(dfa) - dfa.isna().sum()) >= 4)]
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
