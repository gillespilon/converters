#! /usr/bin/env python3
"""
Compare a text file of an ATS-friendly resume with a text file of a job
posting.
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
        "-pfcv",
        "--path_or_file_cv",
        default=Path("ats_resume.txt"),
        type=Path,
        required=False,
        help="path .txt resume (default: ats_resume.txt",
    )
    parser.add_argument(
        "-pfdk",
        "--path_or_file_delete_keywords",
        default=Path("ats_delete_keywords.txt"),
        type=Path,
        required=False,
        help="path .txt delete keywords (default: ats_delete_keywords.txt",
    )
    args = parser.parse_args()
    delete_keywords_path = args.path_or_file_delete_keywords
    resume_path = args.path_or_file_cv
    delete_substrings_path = Path("ats_delete_substrings.txt")
    clean_keywords_path = Path("ats_clean_keywords.txt")
    resume_keywords = [(line.rstrip()) for line in resume_path.open()]
    delete_keywords = [(line.rstrip()) for line in delete_keywords_path.open()]
    # read the substrings to delete file, create list of strings
    delete_substrings = [
        line.rstrip("\n") for line in delete_substrings_path.open()
    ]
    resume_keywords = ds.list_one_list_two_ops(
        list_one=resume_keywords, list_two=delete_keywords, action="list_one"
    )
    resume_keywords = [
        text.replace(substring, "")
        for text in resume_keywords
        for substring in delete_substrings
        if substring in text
    ]
    print(resume_keywords)
    with open(clean_keywords_path, "w") as file:
        for string in resume_keywords:
            file.write(string + "\n")


if __name__ == "__main__":
    main()
