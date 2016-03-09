#!/bin/env python3
# -*- coding: utf-8 -*-

import math


def solve():
    limit = 120000
    result, rad = 0, [1 for i in range(limit)]
    for i in range(2, limit):
        if rad[i] == 1:
            rad[i] = i
            for j in range(i * 2, limit, i):
                rad[j] *= i
    _rad = sorted([(rad[i], i) for i in range(1, limit)])
    for c in range(3, limit):
        rad_c, half_c = rad[c], c // 2
        for rad_a, a in _rad:
            if rad_a * rad_c > half_c:
                break
            if a >= half_c:
                continue
            b = c - a
            if rad_a * rad[b] * rad[c] < c and math.gcd(rad_a, rad[b]) == 1:
                result += c
    return result


if __name__ == "__main__":
    print(solve())
