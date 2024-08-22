#!/usr/bin/python3
"""function: validUTF8"""


def validUTF8(data):
    """determine if the given data set represents a valid UTF-8 encoding"""
    for i in data:
        if (i >= 0 and i <= 127):
            continue
        elif (i >= 2048 and i <= 1114111):
            continue
        else:
            return False
    return True
