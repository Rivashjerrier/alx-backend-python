#!/usr/bin/env python3
"""
    1-concurrent_coroutines.py
"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
        Asynchronous routine that spawns wait_random n times with the specified max_delay,
        and returns the list of all the delays in ascending order
    """
    delay_list = []
    for x in range(n):
        delay_list.append(await wait_random(max_delay))
    return sorted(delay_list)
