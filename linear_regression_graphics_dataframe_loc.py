#! /usr/bin/env python3
"""
Linear regression, scatter plot, fitted line on row subsets of the
independent variable

Requires:
- datasense: https://github.com/gillespilon/datasense
"""

from pathlib import Path
import time

import statsmodels.api as sm
import datasense as ds
import pandas as pd


def main():
    start_time = time.perf_counter()
    HEADER_ID = "Linear regression, scatter plot, fitted line on subsets"
    OUTPUT_URL = "linear_regression_graphics_dataframe_loc.html"
    HEADER_TITle = "Convert .csv to .feather"
    COLUMN_PREDICTIONS = "mean"
    COLUMN_SOLD_TO = "sold_to"
    COLUMN_SALES = "sales"
    COLUMN_DATE = "date"
    P_VALUE = "p value"
    SLOPE = "slope"
    DATA = {
        COLUMN_SOLD_TO: [1, 1, 1, 1, 1, 2, 2, 2, 2],
        COLUMN_DATE: [
            "2022-01", "2022-02", "2022-03", "2022-04", "2022-05",
            "2022-01", "2022-03", "2022-05", "2022-06",
        ],
        COLUMN_SALES: [1, 3, 2, 5, 7, 3, 6, 10, 15],
    }
    original_stdout = ds.html_begin(
        output_url=OUTPUT_URL,
        header_title=HEADER_TITle,
        header_id=HEADER_ID
    )
    ds.script_summary(
        script_path=Path(__file__),
        action="started at"
    )
    df = pd.DataFrame(data=DATA)
    df = ds.optimize_columns(df=df)
    sold_to_numbers = set(df[COLUMN_SOLD_TO])
    for sold_to in sold_to_numbers:
        y = (
            df.loc[df[COLUMN_SOLD_TO] == sold_to, [COLUMN_SALES]]
            .reset_index(drop=True).squeeze()
        )
        X = pd.Series(range(0, len(y)))
        X_plot = X
        X_dates = (
            df.loc[df[COLUMN_SOLD_TO] == sold_to, [COLUMN_DATE]]
            .reset_index(drop=True).squeeze()
        )
        X = sm.add_constant(X)
        fitted_model, predictions = ds.linear_regression(
            X=X,
            y=y,
            prediction_column=COLUMN_PREDICTIONS,
            print_model_summary=False
        )
        fig, ax = ds.plot_scatter_line_x_y1_y2(
            X=X_plot,
            y1=y,
            y2=predictions
        )
        scatter_plot_title = f"Scatter plot of sold to {sold_to}"
        ax.set_title(
            label=scatter_plot_title,
            fontsize=13
        )
        ax.set_ylabel(ylabel=COLUMN_SALES)
        ax.set_xlabel(xlabel="date")
        ax.set_xticks(ticks=X_plot.astype(float).values.tolist())
        ax.set_xticklabels(labels=X_dates.astype(str).values.tolist())
        text_to_plot = (
            f"{SLOPE:>9} {fitted_model.params[0]:<12,.3f}\n"
            f"{P_VALUE:>9} {fitted_model.pvalues[0]:<12,.3f}"
        )
        left, bottom, height = 0, 0, 1
        top = bottom + height
        ax.text(
            left, top, text_to_plot,
            horizontalalignment='left',
            verticalalignment='top',
            transform=ax.transAxes,
            family="monospace"
        )
        fig.autofmt_xdate()
        fig.savefig(
            fname=f"linear_regression_graphics_dataframe_{sold_to}.svg",
            format="svg"
        )
        ds.html_figure(
            file_name=f"linear_regression_graphics_dataframe_{sold_to}.svg",
            caption=f"linear_regression_graphics_dataframe_{sold_to}.svg"
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
        output_url=OUTPUT_URL
    )


if __name__ == "__main__":
    main()
