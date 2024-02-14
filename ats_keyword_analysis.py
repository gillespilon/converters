#! /usr/bin/env python3
"""
Compare a text file of an ATS-friendly cv with a text file of a job posting.
"""

from pathlib import Path
from os import chdir
import argparse
import time

import datasense as ds
import pandas as pd
import numpy as np


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
    path_clean_cv = args.path_or_file_cv_clean
    path_deletions = args.path_or_file_deletions
    path_substrings = args.path_or_file_substrings
    cv_raw = [(line.rstrip("\n")) for line in path_cv_raw.open()]
    print("cv_raw")
    print(cv_raw)
    deletions = [(line.rstrip("\n")) for line in path_deletions.open()]
    print("deletions")
    print(deletions)
    substrings = [line.rstrip("\n") for line in path_substrings.open()]
    print("substrings")
    print(substrings)
    # cv_keywords_less_delete_keywords = ds.list_one_list_two_ops(
    #     list_one=cv_keywords, list_two=delete_keywords, action="list_one"
    # )
    # print("unique cv_keywords")
    # print(cv_keywords_less_delete_keywords)
    # read the substrings to delete file, create list of strings
    # cv_keywords = [
    #     text.replace(substring, "")
    #     for text in cv_keywords
    #     for substring in delete_substrings
    #     if substring in text
    # ]
    # cv_keywords_less_substrings = [s.replace(st, "") for s in cv_keywords_less_delete_keywords for st in delete_substrings]
    # cv_keywords_less_substrings = [s for s in cv_keywords_less_delete_keywords if not any(st in s for st in delete_substrings)]
    # filtered_text_set = set(cv_keywords) - set(substring for substring in delete_substrings)
    # cv_keywords_less_substrings = list(filtered_text_set)
    # print(cv_keywords_less_substrings)
    # with open(clean_keywords_path, "w") as file:
    #     for string in cv_keywords_less_substrings:
    #         file.write(string + "\n")


if __name__ == "__main__":
    main()
