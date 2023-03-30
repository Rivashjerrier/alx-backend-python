#!/usr/bin/env python3
"""
    A type-annotated function
"""

from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
        returns the first element or None
        if the list is none
    """
    if lst:
        return lst[0]
    else:
        return None
