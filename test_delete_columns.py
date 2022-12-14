import datasense as ds
import pandas as pd
import numpy as np


df_empty_test = pd.DataFrame(
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


def test_delete_empty_columns():
    """
    Test that all elements of a column:
    - are empty for all columns
    - are empty for specific columns
    """
    # Delete columns where all elements of a column are empty
    result1 = ds.delete_empty_columns(df=df_empty_test)
    expected1 = pd.DataFrame(
        data=dict(
            floats=[1.0, np.NaN, 3.0, np.NaN, 5.0, 6.0, np.NaN],
            text=["A", "B", "C", "D", "E", "F", np.NaN],
            dates=[
                "1956-06-08", "1956-06-08",
                "1956-06-08", "1956-06-08",
                "1956-06-08", "1956-06-08",
                pd.NaT
            ],
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
        }
    )
    assert result1.equals(other=expected1)
    # Delete columns using list_empty_columns
    list_empty_columns = ["mixed", "nan_none"]
    result2 = ds.delete_empty_columns(
        df=df_empty_test,
        list_empty_columns=list_empty_columns
    )
    expected2 = pd.DataFrame(
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
            "nan_space": "float64"
        }
    )
    assert result2.equals(other=expected2)
    # No not delete columns using list_empty_columns because
    # not all columns in list are empty
    list_empty_columns = ["mixed", "nan_none", "integers"]
    result3 = ds.delete_empty_columns(
        df=df_empty_test,
        list_empty_columns=list_empty_columns
    )
    expected3 = pd.DataFrame(
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
    assert result3.equals(other=expected3)
