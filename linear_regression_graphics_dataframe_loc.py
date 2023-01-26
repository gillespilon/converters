#! /usr/bin/env python3
"""
Linear regression, scatter plot, fitted line on row subsets of the
independent variable

Requires:
- datasense: https://github.com/gillespilon/datasense
- statsmodels: https://www.statsmodels.org/dev/index.html
"""

from pathlib import Path
import time

import datasense as ds
import pandas as pd


def main():
    start_time = time.perf_counter()
    HEADER_TITle = "Linear regression, scatter plot, fitted line on subsets"
    HEADER_ID = "Linear regression, scatter plot, fitted line on subsets"
    GRAPHICS_FILE_PREFIX = "linear_regression_graphics_dataframe"
    OUTPUT_URL = "linear_regression_graphics_dataframe_loc.html"
    SCATTER_PLOT_TITLE = "Scatter plot of subset"
    LABELLEGENDCI = "Confidence interval"
    LABELLEGENDPI = "Prediction interval"
    COLOUR_SHADING = "#888888"
    COLUMN_SUBSETS = "subset"
    COLUMN_Y = "dependent"
    COLUMN_DATE = "date"
    P_VALUE = "p value"
    SLOPE = "slope"
    DATA = {
        COLUMN_SUBSETS: [
            1, 1, 1, 1, 1,
            2, 2, 2, 2
        ],
        COLUMN_DATE: [
            "2022-01", "2022-02", "2022-03", "2022-04", "2022-05",
            "2022-01", "2022-03", "2022-05", "2022-06",
        ],
        COLUMN_Y: [
            1, 3, 2, 5, 7,
            3, 6, 10, 15
        ],
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
    df = pd.DataFrame(data=DATA).sort_values(by=[COLUMN_SUBSETS, COLUMN_DATE])
    df = ds.optimize_columns(df=df)
    column_subsets = set(df[COLUMN_SUBSETS])
    for column_subset in column_subsets:
        y = (
            df.loc[df[COLUMN_SUBSETS] == column_subset, [COLUMN_Y]]
            .reset_index(drop=True).squeeze()
        )
        X = pd.Series(data=range(0, len(y)))
        X_plot = X
        X_dates = (
            df.loc[df[COLUMN_SUBSETS] == column_subset, [COLUMN_DATE]]
            .reset_index(drop=True).squeeze()
        )
        (
            fitted_model, predictions, confidence_interval_lower,
            confidence_interval_upper, prediction_interval_lower,
            prediction_interval_upper
        ) = ds.linear_regression(
            X=X,
            y=y
        )
        fig, ax = ds.plot_scatter_line_x_y1_y2(
            X=X_plot,
            y1=y,
            y2=predictions
        )
        scatter_plot_title = f"{SCATTER_PLOT_TITLE} {column_subset}"
        ax.set_title(
            label=scatter_plot_title,
            fontsize=13
        )
        ax.set_ylabel(ylabel=COLUMN_Y)
        ax.set_xlabel(xlabel="date")
        ax.set_xticks(ticks=X_plot.astype(float).values.tolist())
        ax.set_xticklabels(labels=X_dates.astype(str).values.tolist())
        ax.fill_between(
            X_plot,
            y1=confidence_interval_lower,
            y2=confidence_interval_upper,
            color=COLOUR_SHADING,
            alpha=0.4,
            label=LABELLEGENDCI
        )
        ax.fill_between(
            x=X_plot,
            y1=prediction_interval_lower,
            y2=prediction_interval_upper,
            color=COLOUR_SHADING,
            alpha=0.2,
            label=LABELLEGENDPI
        )
        ax.legend(
            loc="lower right",
            frameon=False
        )
        text_to_plot = (
            f"{SLOPE:>9} {fitted_model.params[0]:<12,.3f}\n"
            f"{P_VALUE:>9} {fitted_model.pvalues[0]:<12,.3f}"
        )
        left, bottom, height = 0, 0, 1
        top = bottom + height
        ax.text(
            x=left,
            y=top,
            s=text_to_plot,
            horizontalalignment='left',
            verticalalignment='top',
            transform=ax.transAxes,
            family="monospace"
        )
        fig.autofmt_xdate()
        fig.savefig(
            fname=f"{GRAPHICS_FILE_PREFIX}_{column_subset}.svg",
            format="svg"
        )
        ds.html_figure(
            file_name=(
                f"{GRAPHICS_FILE_PREFIX}_{column_subset}.svg"
            ),
            caption=(
                f"{GRAPHICS_FILE_PREFIX}_{column_subset}.svg"
            )
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
