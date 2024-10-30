#!/usr/bin/env python3

"""Module sum list"""


import typing


INPUT = typing.List[float]


def sum_list(input_list: INPUT) -> float:
    """returns sum of the list as float"""

    i = sum(input_list)
    return float(i)
