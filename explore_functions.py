#! /usr/bin/env python3
'''
Explore functions using inspect.signature.
'''

from typing import List, Tuple, Union

import datasense as ds


def function_name_syntax(
    positional_only_parameters,
    /,
    positional_or_keyword_parameters,
    *,
    keyword_only_parameters
):
    pass


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


def main():
    functions = [function_name_syntax, function_name]
    for function in functions:
        ds.explore_functions(function=function)


if __name__ == '__main__':
    main()
