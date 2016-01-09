# -*- coding: utf-8 -*-
# !/bin/env python2

import math


def solve_pell(n):
    first = int(math.sqrt(n))
    if first * first == n:
        return -1
    m, d, a = 0, 1, first
    x, y, pre_x, pre_y = first, 1, 1, 0
    while x * x - n * y * y != 1:
        m = d * a - m
        d = (n - m * m) / d
        a = (first + m) / d
        x, pre_x = a * x + pre_x, x
        y, pre_y = a * y + pre_y, y
    return x


def solve():
    maxn, result = -1, 0
    for i in range(1001):
        x = solve_pell(i)
        if x > maxn:
            maxn, result = x, i
    print result


if __name__ == "__main__":
    solve()
