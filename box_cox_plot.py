#! /usr/bin/env python3
"""
Box-Cox normality plot

Requirements
- Series must be > 0

Reference
https://www.itl.nist.gov/div898/handbook/eda/section3/eda336.htm
"""

from pathlib import Path
import time

import matplotlib.pyplot as plt
from scipy import stats
import datasense as ds


def main():
    start_time = time.perf_counter()
    colour1, colour2 = "#0077bb", "#33bbee"
    output_url = 'box_cox_plt.html'
    header_title = 'Box-Cox Plot'
    header_id = 'box_cox_plot'
    la, lb = -2, 2
    original_stdout = ds.html_begin(
        output_url=output_url,
        header_title=header_title,
        header_id=header_id
    )
    ds.script_summary(
        script_path=Path(__file__),
        action='started at'
    )
    # replace next line(s) with your data Series
    df = ds.read_file(file_name='us_mpg.csv')
    s = df.iloc[:, 0]
    # s = stats.loggamma.rvs(5, size=500) + 5
    fig, ax = plt.subplots(nrows=1, ncols=1)
    # create a tuple of two ndarrays
    # fix this so the arrays are series and probl is replace with fig, ax
    stats.boxcox_normplot(x=s, la=la, lb=lb, plot=ax)
    ax.get_lines()[0].set(color=colour1, marker='.', markersize=4)
    boxcox, lmax_mle, (min_ci, max_ci) = stats.boxcox(x=s, alpha=0.05)
    ax.axvline(lmax_mle, color=colour1, label=f'lmax_mle = {lmax_mle:.3f}')
    ax.legend(frameon=False)
    print(f"lmax_mle     : {lmax_mle:.3f}")
    print(f"min_ci       : {min_ci  :.3f}")
    print(f"max_ci       : {max_ci  :.3f}")
    print()
    stop_time = time.perf_counter()
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
    plt.show()


if __name__ == '__main__':
    main()
