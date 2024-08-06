#!/usr/bin/python3
"""minoperations function"""
from typing import List


def minOperations(n: int) -> int:
    """
    calculates the fewest number of operations needed to result in exactly n
    H characters in the file
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    dividor: int = 0
    divlt: List[int] = []
    remainder: int = 0
    val: int = n
    while (val):
        if (val == 1):
            break
        for i in range(2, val + 1):
            if val % i == 0:
                dividor = i
                break
        if dividor == 0:
            dividor = val
        remainder = int(val / dividor)
        val = remainder
        divlt.append(dividor)
    if (len(divlt) == 1 and divlt[0] == n):
        return n
    result = sum(divlt)
    if n % 2 == 0:
        return result
    return result + 1
