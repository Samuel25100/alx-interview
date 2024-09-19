#!/usr/bin/python3
"""function: make_change"""
from typing import List


def makeChange(coins: List[int], total: int) -> int:
    """determine the fewest num of coins needed to meet a given amount total"""
    if total <= 0:
        return 0
    elif len(coins) == 0:
        return -1
    con = coins
    tot = total
    count = 0
    while (tot):
        maxc = max(con)
        if maxc <= tot:
            count += 1
            tot -= maxc
            if maxc > tot:
                con.pop(con.index(maxc))
        elif maxc > tot:
            con.pop(con.index(maxc))
        if len(con) == 0 and tot > 0:
            return -1
    return count
