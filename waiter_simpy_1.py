#! /usr/bin/env python3
"""
waiter.py

The waiter (process) serves in a restaurant (environment).

The waiter takes orders from customers, gives orders to cooks, and serves food
to customers.

This is the first of three restaurant simulations.

References
https://towardsdatascience.com/simulate-real-life-events-in-python-using-simpy-e6d9152a102f
https://simpy.readthedocs.io/en/latest/contents.html
"""

import numpy as np
import simpy as sy


def waiter(env):
    while True:
        print(f"Start taking orders from customers at {env.now:.3f}")
        take_order_duration = np.random.triangular(left=3, mode=5, right=7)
        yield env.timeout(take_order_duration)
        print(f'Start giving the orders to the cooks at {env.now:.3f}')
        give_order_duration = np.random.triangular(left=1, mode=2, right=3)
        yield env.timeout(give_order_duration)
        print(f'Start serving customers food at {env.now:.3f}\n')
        serve_order_duration = np.random.triangular(left=3, mode=5, right=7)
        yield env.timeout(serve_order_duration)


def main():
    # Environment() is the execution environment for an event-based simulation.
    # The passing of time is simulated by stepping from event to event.
    # Create the environment where the waiter lives.
    env = sy.Environment()
    # process is an event-yielding generator.
    # Pass the waiter to the environment.
    env.process(waiter(env))
    # Execute until the criterion is met.
    # Run simulation until 30 s.
    env.run(until=30)


if __name__ == "__main__":
    main()
