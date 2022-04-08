#! /usr/bin/env python3
"""
Yeo-Johnson normality plot
"""

from pathlib import Path
import time

from matplotlib import rcParams as rc
import matplotlib.pyplot as plt
from scipy import stats
import datasense as ds


def main():
    start_time = time.perf_counter()
    colour1 = "#0077bb"
    output_url = "yeo_johnson_plot.html"
    rc["axes.labelweight"] = "bold"
    rc["axes.titleweight"] = "bold"
    header_title = "Yeo-Johnson Plot"
    header_id = "yeo_johnson_plot"
    rc["xtick.labelsize"] = 10
    rc["ytick.labelsize"] = 10
    rc["axes.labelsize"] = 12
    rc["axes.titlesize"] = 15
    la, lb = -15, 15
    original_stdout = ds.html_begin(
        output_url=output_url,
        header_title=header_title,
        header_id=header_id
    )
    ds.script_summary(
        script_path=Path(__file__),
        action="started at"
    )
    # replace next line(s) with your data Series
    # df = ds.read_file(file_name=Path("us_mpg.csv"))
    # s = df.iloc[:, 0]
    # comment out next line if reading your own file
    s = stats.loggamma.rvs(5, size=500) + 5
    fig, ax = plt.subplots(nrows=1, ncols=1)
    stats.yeojohnson_normplot(x=s, la=la, lb=lb, plot=ax)
    ax.get_lines()[0].set(color=colour1, marker=".", markersize=4)
    yeojohson, maxlog = stats.boxcox(x=s)
    ax.axvline(maxlog, color=colour1, label=f"λ      = {maxlog:7.3f}")
    ax.set_ylabel(ylabel="Correlation Coefficient")
    ax.legend(frameon=False, prop={"family": "monospace", "size": 8})
    ds.despine(ax=ax)
    fig.savefig(fname=Path("yeo_johnson_plot.svg", format="svg"))
    print(f"λ: {maxlog:7.3f}")
    print()
    stop_time = time.perf_counter()
    ds.script_summary(script_path=Path(__file__), action="finished at")
    ds.report_summary(start_time=start_time, stop_time=stop_time)
    ds.html_end(original_stdout=original_stdout, output_url=output_url)
    # plt.show()


if __name__ == "__main__":
    main()
