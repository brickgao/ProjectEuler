# !/bin/env python2
# -*- coding: utf-8 -*-

from math import sqrt
from fractions import gcd


def solve():
    rec = [0 for i in range(1500000)]
    upper = int(sqrt(1500000 // 2))
    for m in range(2, upper):
        for n in range(1, m):
            if (m + n) % 2 == 1 and gcd(m, n) == 1:
                a, b, c = m * m + n * n, m * m - n * n, 2 * m * n
                tri_len = a + b + c
                for k in range(tri_len, 1500000, tri_len):
                    rec[k] += 1
    return len(filter(lambda x: x == 1, rec))


if __name__ == "__main__":
    print solve()
