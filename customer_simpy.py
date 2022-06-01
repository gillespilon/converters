#! /usr/bin/env python3
"""
waiter.py

The waiter (process) serves in a restaurant (environment).

The waiter takes orders from customers, gives orders to cooks, and serves food
to customers.

This is the second of three restaurant simulations.

References
https://towardsdatascience.com/simulate-real-life-events-in-python-using-simpy-e6d9152a102f
https://simpy.readthedocs.io/en/latest/contents.html
"""

import numpy as np
import simpy as sy


def customer(env, name, restaurant, **duration):
    while True:
        # There is a new customer between 0 and 10 minutes
        yield env.timeout(np.random.triangular(left=0, mode=5, right=10))
        print(
            f"{name} enters the restaurant and waits for the waiter to come at"
            f" {round(env.now, 2)}"
        )
        with restaurant.request() as req:
            yield req
            print(
                f"Seats are available. {name} is seated at {round(env.now, 2)}"
            )
            yield env.timeout(duration["get_seated"])
            print(f"{name} starts looking at the menu at {round(env.now, 2)}")
            yield env.timeout(duration["choose_food"])
            print(
                f"Waiters start getting the order from {name} at "
                f"{round(env.now, 2)}"
            )
            yield env.timeout(duration["give_order"])
            print(f"{name} starts waiting for food at {round(env.now, 2)}")
            yield env.timeout(duration["wait_for_meal"])
            print(f"{name} starts eating at {round(env.now, 2)}")
            yield env.timeout(duration["eat_food"])
            print(f"{name} starts paying at {round(env.now, 2)}")
            yield env.timeout(duration["pay_for_meal"])
            print(f"{name} leaves at {round(env.now, 2)}")


def main():
    env = sy.Environment()
    restaurant = sy.Resource(env, capacity=15)
    durations = {
        "get_seated": 1,
        "choose_food": 10,
        "give_order": 5,
        "wait_for_meal": 20,
        "eat_food": 45,
        "pay_for_meal": 10
    }
    for i in range(5):
        env.process(customer(env, f"Customer {i}", restaurant, **durations))
    env.run(until=120)


if __name__ == "__main__":
    main()
