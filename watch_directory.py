#! /usr/bin/env python3
"""
Watch a directory for file changes. Print changes.

If desired to loop many times:
- add while True loop

start_hour, stop_hour = 8, 17
while True:
    current code below
    if len(files_finish) == 0:
        continue
    else:
        # do stuff to files
    if datetime.now().hour > start_hour and datetime.now().hour < stop_hour:
        continue
    else:
        ds.exit_script(
            original_stdout=original_stdout,
            output_url=output_url
        )
"""

from pathlib import Path
from os import chdir
import time

import datasense as ds


def main():
    chdir(Path(__file__).parent.resolve())  # required for cron
    output_url = "watch_directory.html"
    path = Path().home() / "downloads"
    header_title = "Watch directory"
    header_id = "watch-directory"
    patterns = [".txt", ".TXT"]
    time_delay = 30
    original_stdout = ds.html_begin(
        output_url=output_url, header_title=header_title, header_id=header_id
    )
    ds.script_summary(script_path=Path(__file__), action="started at")
    print("watched directory: ", path)
    print()
    files_start = sorted(
        ds.directory_file_list(directory=path, patterns=patterns)
    )
    print("files start")
    files_start_names = [f.name for f in files_start]
    print(files_start_names)
    print()
    files_start_mtime = [f.stat().st_mtime for f in files_start]
    time.sleep(time_delay)
    print("slept for ", time_delay, "s")
    print()
    files_finish = sorted(
        ds.directory_file_list(directory=path, patterns=patterns)
    )
    files_finish = sorted(
        ds.directory_file_list(directory=path, patterns=patterns)
    )
    files_new_modified = [
        f.name for f in files_finish
        if f.stat().st_mtime not in files_start_mtime
    ]
    print("files finish")
    print(files_new_modified)
    print()
    # enter code to do things with new, modified files
    # examples
    # convert .csv to .feather
    # convert .mkd to .html
    ds.script_summary(script_path=Path(__file__), action="finished at")
    ds.html_end(original_stdout=original_stdout, output_url=output_url)


if __name__ == "__main__":
    main()
