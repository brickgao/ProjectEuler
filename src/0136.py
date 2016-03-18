#!/bin/env python3
# -*- coding: utf-8 -*-

import math


def get_prime(n):
    _is, result = [True if i >= 2 else False for i in range(n + 1)], [2]
    upper = math.ceil(math.sqrt(n))
    for i in range(4, n, 2):
        _is[i] = False
    for i in range(3, upper, 2):
        if _is[i]:
            step = i * 2
            result.append(i)
            for j in range(i * i, n, step):
                _is[j] = False
    while i < n:
        if _is[i]:
            result.append(i)
        i += 2
    return result


def solve():
    result, limit = 2, 50000000
    primes = get_prime(limit)
    for prime in primes[1:]:
        if prime < limit // 4:
            result += 1
        if prime < limit // 16:
            result += 1
        if (prime - 3) % 4 == 0:
            result += 1
    return result


if __name__ == "__main__":
    print(solve())
