#!/usr/bin/env python3
"""
    A type-annotated function
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
        make_multiplier that takes a float multiplier as argument and
        returns a function that multiplies a float by multiplier
    """
    def multiply(value: float) -> float:
        return value * multiplier
    return multiply
