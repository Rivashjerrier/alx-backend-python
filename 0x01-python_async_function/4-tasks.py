#!/usr/bin/env python3
"""
    4-tasks.py
"""

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
        Asynchronous routine that spawns wait_random n times with the
        specified max_delay.
        returns the list of all the delays in ascending order
    """
    delay_list = []
    for x in range(n):
        delay_list.append(await task_wait_random(max_delay))
    return sorted(delay_list)
