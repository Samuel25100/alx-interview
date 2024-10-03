#!/usr/bin/python3
"""functions: isWinner"""


def isWinner(x, nums):
    """determine who the winner is in prime game"""
    ben = 0
    maria = 0
    for round in range(0, x):
        game = sieveErato(nums[round])
        if (len(game) % 2 == 0):
            ben += 1
        else:
            maria += 1
    if (maria > ben):
        return "Maria"
    elif (maria == ben):
        return None
    else:
        return "Ben"


def sieveErato(n):
    """take list of numbers and return only prime list"""
    array = [True for i in range(n + 1)]
    final = []
    p = 2
    while (p * p <= n):
        if array[p] is True:
            for i in range(p * p, n + 1, p):
                array[i] = False
        p += 1
    for j in range(2, n + 1):
        if array[j]:
            final.append(array[j])
    return final
