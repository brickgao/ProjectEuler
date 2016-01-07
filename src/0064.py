# -*- coding: utf-8 -*-
# !/bin/env python2

import math


def gcd(a, b):
    a, b = abs(a), abs(b)
    if b > a:
        a, b = b, a
    while b != 0:
        a, b = b, a % b
    return a


def solve():
    """
    i1 * sqrt(i) + i2
    -----------------
    i3 * sqrt(i) + i4
    """
    result = 0
    for i in range(10000):
        first = int(math.sqrt(i))
        if first * first == i:
            continue
        cnt, vis = 0, set()
        i1, i2 = 0, 1
        i3, i4 = 1, - first
        _i1, _i2 = - i1 * i4 + i2 * i3, - i2 * i4 + i1 * i3 * i
        _i3, _i4 = 0, i3 * i3 * i - i4 * i4
        now = _i2 // _i4 + 1
        i1, i2 = 0, _i4
        i3, i4 = _i1, _i2 - now * _i4
        divsor = gcd(gcd(i2, i3), gcd(i3, i4))
        i2, i3, i4 = i2 / divsor, i3 / divsor, i4 / divsor
        _sqrt_i = math.sqrt(i)
        while (i1, i2, i3, i4) not in vis:
            vis.add((i1, i2, i3, i4))
            cnt += 1
            _i1, _i2 = - i1 * i4 + i2 * i3, - i2 * i4 + i1 * i3 * i
            _i3, _i4 = 0, i3 * i3 * i - i4 * i4
            now = int(math.floor((i1 * _sqrt_i + i2) / (i3 * _sqrt_i + i4)))
            i1, i2 = 0, _i4
            i3, i4 = _i1, _i2 - now * _i4
            divsor = gcd(gcd(i2, i3), gcd(i3, i4))
            i2, i3, i4 = i2 / divsor, i3 / divsor, i4 / divsor
        if cnt % 2:
            result += 1
    print result


if __name__ == "__main__":
    solve()
