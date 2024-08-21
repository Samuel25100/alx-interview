#!/usr/bin/python3
"""function: validUTF8"""


def validUTF8(data):
    """"determine if the given data set represents a valid UTF-8 encoding"""
    for i in data:
        if (i < 0 or i > 127):
            return False
    return True
