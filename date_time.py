#! /usr/bin/env python3
"""
Explore date and time functions. Examples show f-string within the print
statement and within the variable definition.
"""

from dateutil.relativedelta import relativedelta
from datetime import date, datetime, timedelta


def main():
    start = date.today()
    print("Determine current date with `datetime.date.today()`")
    print(f"{start:%Y-%m-%d}")
    print()
    start = datetime.today()
    print("Determine current date with `datetime.today()`")
    print(f"{start:%Y-%m-%d}")
    print()
    start = \
        datetime.today().replace(month=1).replace(day=1) - timedelta(days=1)
    print("Set current month to January and determine the prior month")
    print(f"{start:%m}")
    print()
    start = date.today().replace(day=1) - timedelta(days=1)
    print("Set current month and determine one month prior")
    print(f"{start:%m}")
    print()
    start = f"{(date.today().replace(day=1) - timedelta(days=1)):%m}"
    print("Set current month and determine one month prior")
    print(start)
    print()
    start = (datetime.today() + relativedelta(months=-1))
    print("Set current month and determine one month prior with `relative`")
    print(f"{start:%m}")
    print()
    start = date.today().replace(day=13).replace(day=1) - timedelta(days=1)
    print(
        "Set today as the 13th and determine last day of prior prior month"
    )
    print(f"{start:%Y-%m-%d}")
    print()
    start = date.today().replace(day=13) + relativedelta(months=-1)
    print("Set today as the 13th and determine prior month with `relative`")
    print(f"{start:%Y-%m-%d}")
    print()
    start = date.today().replace(month=1).replace(day=13)
    print("Set today as the 13th of January")
    print(f"{start:%Y-%m-%d}")
    print()
    start = date.today().replace(month=3).replace(day=13)
    print("Set today as the 13th of March in a leap year")
    print(f"{start:%Y-%m-%d}")
    print()
    number_months_prior_start = 1
    number_months_prior_end = 12
    dates = [
        f"{(datetime.today() + relativedelta(months=-x)):%Y%m}"
        for x in range(number_months_prior_start, number_months_prior_end + 1)
    ]
    print("Determine 12 prior months")
    print(dates)
    print()
    current_year = datetime.today().year
    print("Determine the current year")
    print(current_year)
    print()
    current_month = datetime.today().month
    print("Determine the current month")
    print(current_month)
    print()
    current_day = datetime.today().day
    print("Determine the current day")
    print(current_day)
    print()
    start = (datetime.today().replace(day=1) + relativedelta(months=-1))
    print("Determine the date of the first day of the prior month")
    print(f"{start:%Y%m%d}")
    print()
    start = (datetime.today() + timedelta(days=1))
    print("Determine tomorrow's date")
    print(f"{start:%Y-%m-%d}")
    print()
    iso_date_and_time = f"{(datetime.now()):%FT%T}"
    print("Determine ISO date and time in a simpler way")
    print(iso_date_and_time)
    print()
    iso_date = f"{(datetime.now()):%F}"
    print("Determine ISO date in a simpler way")
    print(iso_date)
    print()
    iso_time = f"{(datetime.now()):%T}"
    print("Determine ISO time in a simpler way")
    print(iso_time)
    print()


if __name__ == "__main__":
    main()
