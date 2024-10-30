#!/usr/bin/env python3

"""Sum mixed list"""

import typing

MXD = typing.List[typing.Union[int, float]]


def sum_mixed_list(mxd_lst: MXD) -> float:
    """sum mixed list and return in float"""

    i = sum(mxd_lst)
    return float(i)
