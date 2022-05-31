#! /usr/bin/env python3
"""
Example of discrete-event simulation without using SimPy.

Pros: simple to understand and create
Cons: takes a long time to run for real-life situation
"""

from datetime import datetime
from typing import NoReturn
from pathlib import Path
import time

import datasense as ds
import pandas as pd
import numpy as np


class customer:
    def __init__(self):
        self.total_time_waiting_order = 0
        self.total_time_place_order = 0
        self.time_start_place_order = 0
        self.time_end_order_placing = 0
        self.time_order_delivered = 0
        self.time_arrive_system = 0
        self.time_arrive_queue = 0
        self.time_exit_system = 0
        self.customer_number = 0


def travel_wait(
    left: float = 1,
    mode: float = 2,
    right: float = 3
) -> NoReturn:
    time.sleep(np.random.triangular(left=left, mode=mode, right=right))


def main():
    path_file_save = Path("discrete_event_simulation_df.ods")
    output_url = "discrete_event_simulation.html"
    header_title = "Discrete event simulation"
    header_id = "discrete-event-simulation"
    total_time_place_order_list = []
    time_start_place_order_list = []
    time_end_order_placing_list = []
    time_order_delivered_list = []
    total_time_waiting_order = []
    time_arrive_system_list = []
    time_arrive_queue_list = []
    time_exit_system_list = []
    initial_time = time.time()
    customer_number_list = []
    model_run_time = 30
    customer_number = 0
    original_stdout = ds.html_begin(
        output_url=output_url, header_title=header_title, header_id=header_id
    )
    ds.script_summary(script_path=Path(__file__), action="started at")
    while time.time() < initial_time + model_run_time:

        # New customer instantiation
        new_customer = customer()
        new_customer.customer_number = customer_number + 1
        customer_number_list.append(new_customer.customer_number)

        # Customer arrives to system
        new_customer.time_arrive_system = time.time()
        time_arrive_system_list.append(
            datetime.fromtimestamp(new_customer.time_arrive_system)
            .strftime("%Y-%m-%dT%H:%M:%S")
        )

        # Customer walks to queue, times in float seconds
        travel_wait(left=1, mode=2, right=3)

        # Customer arrives to queue
        new_customer.time_arrive_queue = time.time()
        time_arrive_queue_list.append(
            datetime.fromtimestamp(new_customer.time_arrive_queue)
            .strftime("%m/%d/%Y, %H:%M:%S")
        )

        # Customer waiting time on queue
        travel_wait(left=2, mode=3, right=4)

        # Customer arrives to order point and starts placing order
        new_customer.time_start_place_order = time.time()
        time_start_place_order_list.append(
            datetime.fromtimestamp(new_customer.time_start_place_order)
            .strftime("%m/%d/%Y, %H:%M:%S")
        )

        # Time order being taken
        travel_wait(left=1, mode=2, right=3)

        # Customer ends placing order
        new_customer.time_end_order_placing = time.time()
        time_end_order_placing_list.append(
            datetime.fromtimestamp(new_customer.time_end_order_placing)
            .strftime("%m/%d/%Y, %H:%M:%S")
        )

        # Total time spent for placing the order
        new_customer.total_time_place_order = (
            new_customer.time_end_order_placing -
            new_customer.time_start_place_order
        )
        total_time_place_order_list.append(new_customer.total_time_place_order)

        # Time order being processed
        travel_wait(left=4, mode=5, right=6)

        # Customer recevies order
        new_customer.time_order_delivered = time.time()
        time_order_delivered_list.append(
            datetime.fromtimestamp(new_customer.time_order_delivered)
            .strftime("%m/%d/%Y, %H:%M:%S")
        )

        # Total time customer waited for the order to be recevied
        new_customer.total_time_waiting_order = (
            new_customer.time_order_delivered -
            new_customer.time_end_order_placing
        )
        total_time_waiting_order.append(
            new_customer.total_time_waiting_order
        )

        # Time customer spends validating order
        travel_wait(left=1, mode=2, right=3)

        # Customer exists order
        new_customer.time_exit_system = time.time()
        time_exit_system_list.append(
            datetime.fromtimestamp(new_customer.time_exit_system)
            .strftime("%m/%d/%Y, %H:%M:%S")
        )

        customer_number += 1

    df = pd.DataFrame(
        {
            "customer_number": customer_number_list,
            "time_arrive_system": time_arrive_system_list,
            "time_arrive_queue": time_arrive_queue_list,
            "time_start_place_order": time_start_place_order_list,
            "time_end_order_placing": time_end_order_placing_list,
            "time_order_delivered": time_order_delivered_list,
            "time_exit_system": time_exit_system_list,
            "time_placing_order": total_time_place_order_list,
            "time_waiting_for_order": total_time_waiting_order,
        }
    )

    df.set_index("customer_number", inplace=True)
    ds.save_file(df=df, file_name=path_file_save)
    print(df[["time_placing_order", "time_waiting_for_order"]].describe())
    ds.dataframe_info(df=df, file_in=path_file_save)

    ds.script_summary(script_path=Path(__file__), action="finished at")
    ds.html_end(original_stdout=original_stdout, output_url=output_url)


if __name__ == "__main__":
    main()
