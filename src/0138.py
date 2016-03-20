#!/bin/env python3
# -*- coding: utf-8 -*-


def solve():
    # https://www.alpertron.com.ar/QUAD.HTM
    result, x, y = 0, 0, -1
    for i in range(12):
        _x, _y = -9 * x - 4 * y + 4, -20 * x - 9 * y + 8
        x, y = _x, _y
        result += abs(y)
    return result


if __name__ == "__main__":
    print(solve())
