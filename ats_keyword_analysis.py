#! /usr/bin/env python3
"""
Compare a text file of an ATS-friendly cv with a text file of a job posting.
"""

from pathlib import Path
from os import chdir
import argparse
import re

import datasense as ds


def main():
    chdir(Path(__file__).parent.resolve())  # required for cron
    parser = argparse.ArgumentParser(description="ATS Keyword Analysis")
    parser.add_argument(
        "-pfcvr",
        "--path_or_file_cv_raw",
        default=Path("ats_cv.txt"),
        type=Path,
        required=False,
        help="path .txt cv (default: ats_cv.txt)",
    )
    parser.add_argument(
        "-pfdk",
        "--path_or_file_deletions",
        default=Path("ats_deletions.txt"),
        type=Path,
        required=False,
        help="path .txt deletions (default: ats_deletions.txt)",
    )
    parser.add_argument(
        "-pfst",
        "--path_or_file_substrings",
        default=Path("ats_substrings.txt"),
        type=Path,
        required=False,
        help="path .txt substrings (default: ats_substrings.txt)",
    )
    parser.add_argument(
        "-pfcvc",
        "--path_or_file_cv_clean",
        default=Path("ats_cv_clean.txt"),
        type=Path,
        required=False,
        help="path .txt cv clean (default: ats_cv_clean.txt)",
    )
    args = parser.parse_args()
    path_cv_raw = args.path_or_file_cv_raw
    path_cv_clean = args.path_or_file_cv_clean
    path_deletions = args.path_or_file_deletions
    # might not be needed if done with regex
    # path_substrings = args.path_or_file_substrings
    cv_raw = [(line.rstrip("\n")) for line in path_cv_raw.open()]
    deletions = [(line.rstrip("\n")) for line in path_deletions.open()]
    # might not be needed if done with regex
    # substrings = [line.rstrip("\n") for line in path_substrings.open()]
    cv_deletions = ds.list_one_list_two_ops(
        list_one=cv_raw, list_two=deletions, action="list_one"
    )
    cv_substrings = [
        re.sub(r"^Skills: |^\s{4}\• ", "", st) for st in cv_deletions
    ]
    with open(path_cv_clean, "w") as f:
        for s in cv_substrings:
            f.write(s + "\n")


if __name__ == "__main__":
    main()
