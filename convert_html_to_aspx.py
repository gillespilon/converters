#! /usr/bin/env python3
"""
Convert html files to aspx files using shutil.copyfile.
Convert internal .html URLs to .aspx.
Leave external .html URLs as is.
"""

from shutil import copyfile
from pathlib import Path
import time

import datasense as ds


def main():
    header_title = "Convert html files to aspx files"
    title_ask_directory = "Directory of html files?"
    header_id = "convert-html-files-to-aspx-files"
    output_url = "convert_html_to_aspx.html"
    pattern_in_line = "job_aid_"
    patterns_aspx = [".aspx"]
    patterns_html = [".html"]
    new_extension = ".aspx"
    old_extension = ".html"
    path_html_files = ds.ask_directory_path(
        title=title_ask_directory, print_bool=True
    )
    start_time = time.time()
    original_stdout = ds.html_begin(
        output_url=output_url, header_title=header_title, header_id=header_id
    )
    ds.script_summary(script_path=Path(__file__), action="started at")
    html_files = ds.directory_file_list(
        directory=path_html_files, patterns=patterns_html
    )
    html_files = [x for x in html_files if x.stem.startswith(pattern_in_line)]
    print(html_files)
    print()
    for f in html_files:
        copyfile(src=f, dst=Path(f).with_suffix(new_extension))
    aspx_files = ds.directory_file_list(
        directory=path_html_files, patterns=patterns_aspx
    )
    for f in aspx_files:
        fr = open(f, "r")
        t = fr.readlines()
        fr.close()
        fw = open(f, "w")
        for line in t:
            if pattern_in_line in line and old_extension in line:
                line = line.replace(old_extension, new_extension)
                fw.write(line)
            else:
                fw.write(line)
        fw.close()
    stop_time = time.time()
    ds.script_summary(script_path=Path(__file__), action="finished at")
    ds.report_summary(start_time=start_time, stop_time=stop_time)
    ds.html_end(original_stdout=original_stdout, output_url=output_url)


if __name__ == "__main__":
    main()
