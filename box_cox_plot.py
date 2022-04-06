#! /usr/bin/env python3
"""
Box-Cox probability plot

Requirements
- Series must be > 0
"""

from pathlib import Path
import time

import matplotlib.pyplot as plt
from scipy import stats
import datasense as ds


def main():
    start_time = time.perf_counter()
    output_url = 'box_cox_plt.html'
    header_title = 'Box-Cox Plot'
    header_id = 'box_cox_plot'
    original_stdout = ds.html_begin(
        output_url=output_url,
        header_title=header_title,
        header_id=header_id
    )
    ds.script_summary(
        script_path=Path(__file__),
        action='started at'
    )
    # replace next line with your data Series
    # s = ds.random_data(name="random normal data", loc=69, scale=13)
    s = stats.loggamma.rvs(5, size=500) + 5
    fig, ax = plt.subplots(nrows=1, ncols=1)
    # create a tuple of two ndarrays
    # fix this so the arrays are series and probl is replace with fig, ax
    prob = stats.boxcox_normplot(x=s, la=-20, lb=20, plot=ax)
    # print(type(prob).__name__)
    # print(prob)
    y, lmax_mle = stats.boxcox(x=s)
    lmax_pearsonr = stats.boxcox_normmax(x=s)
    ax.axvline(lmax_mle, color='r', label=f'lmax_mle = {lmax_mle:.3f}')
    ax.axvline(
        lmax_pearsonr, color='g', ls='--',
        label=f'lmax_pearsonr = {lmax_pearsonr:.3f}'
    )
    ax.legend(frameon=False)
    print(f"lmax_mle     : {lmax_mle:.3f}")
    print(f"lmax_pearsonr: {lmax_pearsonr:.3f}")
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
