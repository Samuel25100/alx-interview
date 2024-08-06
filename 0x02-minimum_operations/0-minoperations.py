#!/usr/bin/python3
"""minoperations function"""
from typing import List


def minOperations(n: int) -> int:
    """calculates the fewest number of operations needed to result in exactly n"""
    if n <= 0 or type(n) is not int:
        return 0
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
    print('div:', divlt, 'n:', n)
    if (len(divlt) == 1 and divlt[0] == n):
        return n
    return sum(divlt)
