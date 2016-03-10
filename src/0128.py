#!/bin/env python3
# -*- coding: utf-8 -*-

import math
import functools


@functools.lru_cache(maxsize=None)
def is_primes(num):
    if num < 0:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True if num >= 2 else False


def solve():
    layer, cnt, limit = 0, 0, 2000
    while cnt < limit:
        if (
            is_primes(6 * layer - 1) and
            is_primes(6 * layer + 1) and
            is_primes(12 * layer + 5)
        ):
            cnt += 1
            if cnt == limit:
                return 3 * layer * layer - 3 * layer + 2
        if (
            is_primes(6 * layer - 1) and
            is_primes(6 * layer + 5) and
            is_primes(12 * layer - 7)
        ):
            cnt += 1
            if cnt == limit:
                return 3 * layer * layer + 3 * layer + 1
        layer += 1
    return -1


if __name__ == "__main__":
    print(solve())
