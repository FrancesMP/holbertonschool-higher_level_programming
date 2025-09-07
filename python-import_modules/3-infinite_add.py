#!/usr/bin/python3
import sys

if __name__ == "__main__":
    add = 0
    for x in sys.argv[1:]:
        add += int(x)
    print(add)
