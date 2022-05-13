#! /usr/bin/env python3
"""
Extract a date from a string.:w
"""

import re


def main():
    text = "Hello world 06/08/1956 to new life."
    regex = r"\d{1,2}\/\d{1,2}\/\d{2,4}"
    extracted_date = re.search(regex, text)
    print(extracted_date.group(0))
    text = "Hello world 1956-06-08 to new life."
    regex = r"\d{2,4}-\d{1,2}-\d{1,2}"
    extracted_date = re.search(regex, text)
    print(extracted_date.group(0))

if __name__ == "__main__":
    main()
