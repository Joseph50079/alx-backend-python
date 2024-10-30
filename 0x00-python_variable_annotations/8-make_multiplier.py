#!/usr/bin/env python3

"""make a multiplier module"""

import typing


def make_multiplier(multiplier: float) -> typing.Callable[[float], float]:
    """returns the fuction that multiplies with multiplier"""

    def fun(n: float) -> float:
        """return value in float"""

        return float(multiplier * n)
    return fun
