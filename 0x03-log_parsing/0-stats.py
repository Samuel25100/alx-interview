#!/usr/bin/python3
"""reads stdin line by line and computes metrics"""
import sys


def log_parser():
    """Parse log, print stat and file size"""
    out = {'200': 0,
           '301': 0,
           '400': 0,
           '401': 0,
           '403': 0,
           '404': 0,
           '405': 0,
           '500': 0}
    file_size = 0
    count = 0
    try:
        for line in sys.stdin:
            li = line.split()
            if (len(li) == 9 and li[7].isdigit()):
                if (count == 9):
                    print(f"File size: {file_size}")
                    for key in out:
                        if (out[key]):
                            print(f"{key}: {out[key]}")
                    count = 0
                else:
                    count += 1
                out[li[7]] += 1
                file_size += int(li[8])
    except KeyboardInterrupt:
        print(f"File size: {file_size}")
        for key in out:
            if (out[key]):
                print(f"{key}: {out[key]}")


if __name__ == "__main__":
    log_parser()
