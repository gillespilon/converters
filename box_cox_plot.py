#! /usr/bin/env python3
"""
Box-Cox normality plot

Requirements
- Series must be > 0
- https://github.com/gillespilon/datasense

Reference
- https://www.itl.nist.gov/div898/handbook/eda/section3/eda336.htm
"""

from pathlib import Path
import time

import matplotlib.pyplot as plt
from scipy import stats
import datasense as ds


def main():
    START_TIME = time.perf_counter()
    PATH_BOX_COX_TRANSFORMED = Path("box_cox_transformed.svg", format="svg")
    PATH_BOX_COX_ORIGINAL = Path("box_cox_original.svg", format="svg")
    PATH_BOX_COX = Path("box_cox_plot.svg", format="svg")
    COLOUR1, COLOUR2 = "#0077bb", "#33bbee"
    AXES_LABEL = "Normal Probability Plot"
    YLABEL1 = "Correlation Coefficient"
    OUTPUT_URL = "box_cox_plot.html"
    XLABEL = "Theoretical Quantiles"
    HEADER_TITLE = "Box-Cox Plot"
    HEADER_ID = "box-cox-plot"
    YLABEL2 = "Ordered Values"
    LA, LB = -20, 20
    original_stdout = ds.html_begin(
        output_url=OUTPUT_URL,
        header_title=HEADER_TITLE,
        header_id=HEADER_ID
    )
    ds.script_summary(
        script_path=Path(__file__),
        action="started at"
    )
    ds.style_graph()
    # replace next line(s) with your data Series
    # df = ds.read_file(file_name=Path("us_mpg.csv"))
    # s = df.iloc[:, 0]
    # comment out next line if reading your own file
    s = stats.loggamma.rvs(5, size=500) + 5
    # create the Box-Cox normality plot
    fig, ax = plt.subplots(
        nrows=1,
        ncols=1
    )
    stats.boxcox_normplot(
        x=s,
        la=LA,
        lb=LB,
        plot=ax
    )
    ax.get_lines()[0].set(
        color=COLOUR1,
        marker=".",
        markersize=4
    )
    boxcox, lmax_mle, (min_ci, max_ci) = stats.boxcox(
        x=s,
        alpha=0.05
    )
    ax.axvline(
        x=min_ci,
        color=COLOUR2,
        label=f"min CI = {min_ci:7.3f}"
    )
    ax.axvline(
        x=lmax_mle,
        color=COLOUR1,
        label=f"λ      = {lmax_mle:7.3f}"
    )
    ax.axvline(
        x=max_ci,
        color=COLOUR2,
        label=f"max CI = {max_ci:7.3f}"
    )
    ax.set_ylabel(ylabel=YLABEL1)
    ax.legend(
        frameon=False,
        prop={"family": "monospace", "size": 8}
    )
    ds.despine(ax=ax)
    fig.savefig(fname=PATH_BOX_COX)
    ds.html_figure(file_name=PATH_BOX_COX)
    # create the plot of the untransformed data
    fig, ax = ds.probability_plot(data=s)
    ax.set_title(label=f"{AXES_LABEL}")
    ax.set_xlabel(xlabel=XLABEL)
    ax.set_ylabel(ylabel=YLABEL2)
    fig.savefig(fname=PATH_BOX_COX_ORIGINAL)
    ds.html_figure(file_name=PATH_BOX_COX_ORIGINAL)
    # create the plot of the transformed data
    fig, ax = ds.probability_plot(data=boxcox)
    ax.set_title(label=f"{AXES_LABEL}")
    ax.set_xlabel(xlabel=XLABEL)
    ax.set_ylabel(ylabel=YLABEL2)
    fig.savefig(fname=PATH_BOX_COX_TRANSFORMED)
    ds.html_figure(file_name=PATH_BOX_COX_TRANSFORMED)
    stop_time = time.perf_counter()
    ds.script_summary(
        script_path=Path(__file__),
        action="finished at"
    )
    ds.report_summary(
        start_time=START_TIME,
        stop_time=stop_time
    )
    ds.html_end(
        original_stdout=original_stdout,
        output_url=OUTPUT_URL
    )


if __name__ == "__main__":
    main()
