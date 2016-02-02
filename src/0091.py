# !/bin/env python2
# -*- coding: utf-8 -*-

from fractions import gcd


def solve(n):
    result = 3 * n * n
    for x in range(1, n + 1):
        for y in range(1, n + 1):
            factor = gcd(x, y)
            result += min(factor * x / y, factor * (n - y) / x) * 2
    return result


if __name__ == "__main__":
    print solve(50)
