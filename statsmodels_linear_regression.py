#! /usr/bin/env python3
"""
Demonstrate linear regression, confidence interval, and prediction
interval with statsmodels
"""

import datasense as ds
import pandas as pd


def main():
    output_url = "statsmodels_linear_regression.html"
    header_title = "Statsmodels linear regression"
    header_id = "statsmodels-linear-regression"
    labellegendci = "Confidence interval"
    labellegendpi = "Prediction interval"
    labellegendy2 = "Linear regression"
    lower_ci_column = "mean_ci_lower"
    upper_ci_column = "mean_ci_upper"
    lower_pi_column = "obs_ci_lower"
    upper_pi_column = "obs_ci_upper"
    title = "Regression analysis"
    colour_shading = "#888888"
    graphname = "y_vs_x.svg"
    xlabel = "X axis label"
    ylabel = "Y axis label"
    labellegendy1 = "Data"
    figsize = (8, 6)
    x_column = "x"
    y_column = "y"
    original_stdout = ds.html_begin(
        output_url=output_url,
        header_title=header_title,
        header_id=header_id
    )
    df = pd.DataFrame(
        data={
            x_column: [10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5],
            y_column: [
                8.04, 6.95, 7.58, 8.81, 8.33, 9.96, 7.24, 4.26, 10.84, 4.82,
                5.68
            ]
        }
    ).sort_values(by=x_column)
    (
        fitted_model, predictions, confidence_interval_lower,
        confidence_interval_upper, prediction_interval_lower,
        prediction_interval_upper
    ) = ds.linear_regression(
        X=df[x_column],
        y=df[y_column],
    )
    ds.style_graph()
    fig, ax = ds.plot_scatter_line_x_y1_y2(
        X=df[x_column],
        y1=df[y_column],
        y2=predictions,
        figsize=figsize,
        labellegendy1=labellegendy1,
        labellegendy2=labellegendy2
    )
    ax.fill_between(
        df[x_column],
        y1=confidence_interval_lower,
        y2=confidence_interval_upper,
        color=colour_shading,
        alpha=0.4,
        label=labellegendci
    )
    ax.fill_between(
        x=df[x_column],
        y1=prediction_interval_lower,
        y2=prediction_interval_upper,
        color=colour_shading,
        alpha=0.2,
        label=labellegendpi
    )
    ax.set_title(
        label=title,
        fontsize=15
    )
    ax.set_xlabel(
        xlabel=xlabel,
        fontsize=12
    )
    ax.set_ylabel(
        ylabel=ylabel,
        fontsize=12
    )
    ax.legend(
        loc="upper left",
        frameon=False
    )
    fig.savefig(
        fname=graphname,
        format="svg"
    )
    ds.html_figure(file_name=graphname)
    ds.html_end(
        original_stdout=original_stdout,
        output_url=output_url
    )


if __name__ == "__main__":
    main()
