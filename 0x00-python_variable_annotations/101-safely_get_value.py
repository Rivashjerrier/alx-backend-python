#!/usr/bin/env python3
"""
    0x00-python_variable_annotations
"""

from typing import TypeVar, Mapping, Any, Union

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None]=None) -> Union[T, Any]:
    """
        Retrieves the value of a key in a dictionary safely
    """
    if key in dct:
        return dct[key]
    else:
        return default
