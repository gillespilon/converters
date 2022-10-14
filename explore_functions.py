#! /usr/bin/env python3
'''
Explore functions using inspect.signature.
'''

from typing import List, Tuple, Union

from sklearn.compose import make_column_transformer
from sklearn.pipeline import make_pipeline
import datasense as ds


def main():
    # Explore a list of functions within a script and external
    functions = [
        function_name_syntax,
        function_name,
        make_column_transformer,
        make_pipeline
    ]
    output_url = "explore_functions.html"
    header_title = "Explore functions"
    header_id = "explore-functions"
    original_stdout = ds.html_begin(
        output_url=output_url, header_title=header_title, header_id=header_id
    )
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
    Basic function example.

    Parameters
    ----------
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
    """
    Intermediate function example.

    Parameters
    ----------
    a : float
        Parameter a.
    b : float
        Parameter b.
    c : float = 6
        Paameter c.
    d : Union[float, None] = None,
        Parameter d.
    e : Union[float, int, None] = None,
        Parameter e.
    f : float,
        Parameter f.
    g : float = 4,
        Parameter g.
    h : Union[float, None] = None,
        Parameter h.
    i : Union[float, int, None] = None,
        Parameter i.
    j : Union[List[str], Tuple[float, int], float, int, None] = None,
        Parameter j.
    """


if __name__ == '__main__':
    main()
