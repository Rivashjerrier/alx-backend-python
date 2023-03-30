#!/usr/bin/env python3
"""
    A type-annotated function
"""

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
        @k: a string
        @v: an integer or a float
        Returns: a tuple
    """
    return (k, float(v ** 2))
