#!/bin/env python3
# -*- coding: utf-8 -*-

import math
import itertools
from fractions import Fraction


def solve():
    N = 15
    p = Fraction(0)
    probability_list = [Fraction(1, i + 1) for i in range(1, N + 1)]
    order_list = [i for i in range(N)]
    half_N = 1 + N // 2
    for r in range(half_N, N + 1):
        for c in itertools.combinations(order_list, r):
            now, order_num = Fraction(1), 0
            for i in range(N):
                if order_num < r and c[order_num] == i:
                    now *= probability_list[i]
                    order_num += 1
                else:
                    now *= 1 - probability_list[i]
            p += now
    return math.floor((1 - p) / p) + 1


if __name__ == "__main__":
    print(solve())
