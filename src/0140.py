#!/bin/env python3
# -*- coding: utf-8 -*-


def solve():
    l, rec = [], [
        (0, -1), (0, 1), (-3, -2), (-3, 2),
        (-4, -5), (-4, 5), (2, -7), (2, 7)
    ]
    for x, y in rec:
        for i in range(30):
            x, y = -9 * x - 4 * y - 14, -20 * x - 9 * y - 28
            if x > 0 and x not in l:
                l.append(x)
    l.sort()
    return sum(l[:30])


if __name__ == "__main__":
    print(solve())
