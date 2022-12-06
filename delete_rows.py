#! /usr/bin/env python3
"""
Code to delete rows based on various criteria.
"""

from pathlib import Path
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
