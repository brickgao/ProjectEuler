#!/bin/env python3
# -*- coding: utf-8 -*-


def solve():
    limit = 100 * 10 ** 6
    result, x, y = 0, 1, 1
    while x + y < limit:
        _x, _y = 3 * x + 4 * y, 2 * x + 3 * y
        x, y = _x, _y
        result += limit // (x + y)
    return result


if __name__ == "__main__":
    print(solve())
