#! /usr/bin/env python3
'''
Explore functions using inspect.signature.
'''

from typing import List, Tuple, Union

import datasense as ds


def main():
    output_url = "explore_functions.html"
    header_title = "Explore functions"
    header_id = "explore-functions"
    functions = [function_name_syntax, function_name]
    original_stdout = ds.html_begin(
        output_url=output_url, header_title=header_title, header_id=header_id
    )
    function_name_syntax("1", 2, keyword_only_parameters=13.69)
    print()
    for function in functions:
        ds.explore_functions(function=function)
    ds.html_end(original_stdout=original_stdout, output_url=output_url)


def function_name_syntax(
    positional_only_parameters: str,
    /,
    positional_or_keyword_parameters: int,
    *,
    keyword_only_parameters: float
):
    """
    positional_only_parameters : str
        Positional-only parameter.
    positional_or_keyword_parameters : int
        Positional-or-keyword parameter.
    keyword_only_parameters : float
        Keyword-only parameter.
    """


def function_name(
    a: float,
    /,
    b: float,
    c: float = 6,
    d: Union[float, None] = None,
    e: Union[float, int, None] = None,
    *,
    f: float,
    g: float = 4,
    h: Union[float, None] = None,
    i: Union[float, int, None] = None,
    j: Union[List[str], Tuple[float, int], float, int, None] = None,
):
    pass


if __name__ == '__main__':
    main()