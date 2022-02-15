#! /usr/bin/env python3
"""
Create an svg valentine for the woman I love.
"""

from pathlib import Path

import datasense as ds
import numpy as np


def main():
    path = Path("valentine")
    my_love = "my_love"
    more_love = "more_love"
    x = np.linspace(-3, 3, 1000)
    theta = np.linspace(0, 2 * np.pi, 1000)
    x = 13 * (np.sin(theta) ** 3)
    y = (
        13 * np.cos(theta)
        - 5 * np.cos(2 * theta)
        - 2 * np.cos(3 * theta)
        - np.cos(4 * theta)
    )
    fig, ax = ds.plot_line_x_y(
        X=x,
        y=y,
        markersize=0.1,
        colour="#ff0000",
        figsize=(8, 8),
        linewidth=10,
    )
    ax.set_xticks([])
    ax.set_yticks([])
    for spine in "right", "top", "bottom", "left":
        ax.spines[spine].set_visible(False)
    ax.text(
        x=0,
        y=0,
        s=f"J’aime {my_love}",
        fontsize="36",
        fontweight="black",
        color="#ff0000",
        horizontalalignment="center",
    )
    ax.text(
        x=0,
        y=-2,
        s=more_love,
        fontsize="12",
        fontweight="black",
        color="#ff0000",
        horizontalalignment="center",
    )
    fig.savefig(f"{path}_{my_love}.svg", format="svg")
    fig.savefig(f"{path}_{my_love}.png", format="png")


if __name__ == "__main__":
    main()
