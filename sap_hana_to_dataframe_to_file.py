#! /usr/bin/env python3
"""
Create a dataframe and feather file from an SAP HANA view.

This script requires editing in order to enter your SAP HANA information.

Requires my datasense package:
    https://github.com/gillesilon/datasense
Requires SAP HANA HDB client for Windows.
"""

from typing import IO, List, Tuple
from datetime import date, timedelta
from pathlib import Path
import time

from hdbcli import dbapi
import datasense as ds
import pandas as pd


def main():
    start_time = time.perf_counter()
    # usually set to prior month
    start_date = int((
        date.today().replace(day=1) - timedelta(days=1)
    ).strftime("%Y%m"))
    # usually set to prior month
    end_date = int((
        date.today().replace(day=1) - timedelta(days=1)
    ).strftime("%Y%m"))
    params = [start_date, end_date]
    query, conn, original_stdout, output_url, file_name = setup(
        start_date=start_date,
        end_date=end_date
    )
    # create dataframe from SAP HANA view
    df = create_dataframe(
        sql=query,
        con=conn,
        params=params
    )
    # save dataframe
    ds.save_file(
        df=df,
        file_name=file_name
    )
    conn.close()
    stop_time = time.perf_counter()
    ds.report_summary(
        start_time=start_time,
        stop_time=stop_time
    )
    ds.script_summary(script_path=Path(__file__))
    print('path of saved file:', file_name)
    ds.html_end(
        original_stdout=original_stdout,
        output_url=output_url
    )


def setup(
    *,
    start_date: int,
    end_date: int,
    directory: str = '<path>',
    extension: str = '.feather',
    query: str = (
        r'''
        SELECT * FROM "<path_of_SAP_HANA_view>"
        WHERE "CALMONTH" BETWEEN ? AND ?
        '''
    ),
    conn: dbapi.Connection = dbapi.connect(
        address='<server_name>',
        port=<enter_port_number>
    ),
    output_url: str = 'sap_hana_df.html',
    header_title: str = 'SAP HANA DataFrame',
    header_id: str = 'sap-hana-df',
) -> Tuple[str, dbapi.Connection, IO[str], str, Path]:
    '''
    Establish parameters.

    Parameters
    ----------
    start_date : int
        The start date (yyyymm) of the data.
    end_date : int
        The end date (yyyymm) of the data.
    directory : str = '<path>'
        The directory containing the csv files.
    extension : str = '.feather'
        The extension of the csv file.
    query: str = (
        r"""
        SELECT * FROM "<path_of_SAP_HANA_vew>"
        WHERE "CALMONTH" BETWEEN ? AND ?
        """
    ),
        The SQL query.
    conn: dbapi.Connection = dbapi.connect(
        address="<server_name>",
        port=<port_number>
    ),
        The connection to the SAP HANA view.
    output_url : str = 'sap_hana_df.html'
        The file name for the html report.
    header_title : str =
    'SAP HANA Supplier Dataframe'
        The header title.
    header_id : str = 'sap-hana-df'
        The header ID.
    )
        The Path of the csv file.

    Returns
    ----------
    query : str
        The SQL query.
    conn : dbapi.Connection
        The connection to the SAP HANA view.
    original_stdout: IO[str]
        A file object for the output of print().
    output_url : str
        The file name for the html report.
    file_name : Path
        The path of the saved csv file.

    Example
    -------
    >>> start_date = 202105
    >>> end_date = 202105
    >>> query, conn, original_stdout, output_url, file_name = setup(
    >>>     start_date=start_date,
    >>>     end_date=end_date
    >>> )
    '''
    original_stdout = ds.html_begin(
        output_url=output_url,
        header_title=header_title,
        header_id=header_id
    )
    file_name = Path.cwd() / directory / \
        (str(start_date) + '_' + str(end_date) + extension)
    return (query, conn, original_stdout, output_url, file_name)


def create_dataframe(
    *,
    sql: str,
    con: dbapi.Connection,
    params: List[int]
) -> pd.DataFrame:
    '''
    Create a dataframe from the SAP HANA view.

    Parameters
    ---------
    query : str
        The SQL query.
    conn : dbapi.Connection
        The connection to the SAP HANA view.
    params : List[int]
        The start date and time, end date and time.

    Returns
    -------
    df : pd.DataFrame
        The dataframe of the SAP HANA view.

    Example
    -------
    >>> df = create_dataframe(
    >>>     sql=query,
    >>>     con=conn
    >>> )
    '''
    df = pd.read_sql(
        sql=sql,
        con=con,
        params=params
    )
    return df


if __name__ == '__main__':
    main()
