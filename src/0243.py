#!/bin/env python3
# -*- coding: utf-8 -*-

import math
import fractions


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
    primes, limit = get_prime(100), fractions.Fraction(15499, 94744)
    n, tmp = 1, fractions.Fraction(1, 1)
    for prime in primes:
        n, tmp = n * prime, tmp * fractions.Fraction(prime - 1, prime)
        if tmp < limit:
            for i in range(1, prime):
                if tmp * fractions.Fraction(n * i, n * i - 1) < limit:
                    return n * i


if __name__ == "__main__":
    print(solve())
