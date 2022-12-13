#! /usr/bin/env python3
"""
Code to delete rows based on various criteria.
"""

from pathlib import Path
import textwrap
import time

import datasense as ds
import pandas as pd
import numpy as np


def main():
    columns_to_check = ["integers", "floats", "text"]
    look_in_columns = ["floats", "text", "dates"]
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
    print(
        "Delete rows where all elements are missing."
    )
    print(textwrap.dedent("""
        df = df.dropna(
            axis="index",
            how="all"
        )
    """))
    dfa = df.copy()
    dfa = dfa.dropna(
        axis="index",
        how="all"
    )
    print(dfa)
    print()
    print("Delete rows where at least one element missing.")
    print(textwrap.dedent("""
        df = df.dropna(
            axis="index",
            how="any"
        )
    """))
    dfa = df.copy()
    dfa = dfa.dropna(
        axis="index",
        how="any"
    )
    print(dfa)
    print()
    print("Delete rows where there are less than four non-missing elements.")
    print(textwrap.dedent("""
        df = df.dropna(
            axis="index",
            thresh=4
        )
    """))
    dfa = df.copy()
    dfa = dfa.dropna(
        axis="index",
        thresh=4
    )
    print(dfa)
    print()
    print("Delete rows where all elements are missing, in specific columns.")
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
        "in specific columns."
    )
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
    print("loc, isna")
    print("---------")
    print()
    print("Delete rows where all elements are missing.")
    print(textwrap.dedent("""
        df.loc[~(df.shape[1] == df.isna().sum(axis=1)), :]
    """))
    dfa = df.copy()
    dfa = dfa.loc[~(dfa.shape[1] == dfa.isna().sum(axis=1)), :]
    print(dfa)
    print()
    print("Delete rows where 8 or more elements are missing missing.")
    print(textwrap.dedent("""
        df.loc[~((df.isna().sum(axis=1)) >= 8), :]
    """))
    dfa = df.copy()
    dfa = dfa.loc[~((dfa.isna().sum(axis=1)) >= 8), :]
    print(dfa)
    print()
    print("Keep rows where at least four elements are not missing.")
    print(textwrap.dedent("""
        df.loc[((df.shape[1] - df.isna().sum(axis=1)) >= 4), :]
    """))
    dfa = df.copy()
    dfa = dfa.loc[((dfa.shape[1] - dfa.isna().sum(axis=1)) >= 4), :]
    print(dfa)
    print()
    print(
        "Delete rows where all elements are missing in specific columns of "
        "those rows."
    )
    print(textwrap.dedent("""
        look_in_columns = ["floats", "text", "dates"]
        df.loc[
            ~((df[look_in_columns].isna().sum(axis=1)) ==
              (len(look_in_columns))),
            :
        ]
    """))
    dfa = df.copy()
    dfa = dfa.loc[
        ~((dfa[look_in_columns].isna().sum(axis=1)) ==
          (len(look_in_columns))),
        :
    ]
    print(dfa)
    print()
    print(
        "Delete rows where at least one element is missing in specific "
        "columns of those rows."
    )
    print(textwrap.dedent("""
        number_missing = 1
        look_in_columns = ["floats", "text", "dates"]
        df.loc[
            ~((df[look_in_columns].isna().sum(axis=1)) >=
              number_missing),
            :
        ]
    """))
    dfa = df.copy()
    number_missing = 1
    dfa = dfa.loc[
            ~((dfa[look_in_columns].isna().sum(axis=1)) >=
              number_missing),
            :
        ]
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
