#!/usr/bin/env python3

"""annotate this module"""

import typing

TYPE = typing.List[typing.Tuple[typing.Sequence, int]]


def element_length(lst: typing.Iterable[typing.Sequence]) -> TYPE:
    """annotate typing Sequence"""

    return [(i, len(i)) for i in lst]
