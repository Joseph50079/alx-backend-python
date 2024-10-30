#!/usr/bin/env python3

"""module to_kv"""

import typing


def to_kv(k: str, v: typing.Union[int, float]) -> typing.Tuple[str, float]:
    """returns tuple of string and square of two possible values"""

    i = v ** 2
    ans = [k, i]
    return tuple(ans)
