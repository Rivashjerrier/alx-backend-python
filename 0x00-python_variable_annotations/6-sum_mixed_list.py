#!/usr/bin/env python3
"""
    A type-annotated function
"""

from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """
        sum_mixed_list which takes a list mxd_lst of integers and floats
        and returns their sum as a float
    """
    return sum(mxd_lst)
