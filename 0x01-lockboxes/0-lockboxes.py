#!/usr/bin/python3
"""Determine all locked list of list boxes can be open"""


def canUnlockAll(boxes):
    """Check all boxes can be unlocked"""
    if len(boxes) == 1:
        return True
    leng = len(boxes)
    keys = set(boxes[0])
    unlok = set([0])

    while (keys):
        key = keys.pop()
        if (key not in unlok and key < leng):
            unlok.add(key)
            futrky = set(boxes[key])
            if (not futrky.issubset(unlok)):
                keys = set(boxes[key])

    if (leng == len(unlok)):
        return True
    return False
