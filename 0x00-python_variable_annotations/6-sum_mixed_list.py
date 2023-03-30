#!/usr/bin/env python3
"""
    A type-annotated function
"""

from typing import List


def sum_mixed_list(mxd_lst: List[int]) -> float:
    """
        sum_mixed_list which takes a list mxd_lst of integers and floats
        and returns their sum as a float
    """

    return sum(mxd_lst)
