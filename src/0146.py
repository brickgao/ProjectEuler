#!/bin/env python3
# -*- coding: utf-8 -*-

import math
import random
import functools


@functools.lru_cache(maxsize=None)
def is_probably_prime(n, k=10):
    if n <= 3:
        return [False, False, True, True][n]
    else:
        s, d, x = 0, n - 1, 0
        while d % 2 == 0:
            s, d = s + 1, d >> 1
        for i in range(k):
            a = random.randrange(2, n)
            x = pow(a, d, n)
            if x == 1:
                continue
            tag = False
            for j in range(s - 1):
                if x == n - 1:
                    tag = True
                    break
                x = x * x % n
            if tag:
                continue
            else:
                if x != n - 1:
                    return False
        return True


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
    result, limit = 0, 150 * 10 ** 6
    primes, rec = get_prime(5000), []
    adds1, adds2 = [1, 3, 7, 9, 13, 27], [19, 21]
    for prime in primes:
        add_maybe_prime = []
        for i in range(prime):
            add_maybe_prime.append(True)
            for add in adds1:
                if (i * i + add) % prime == 0:
                    add_maybe_prime[-1] = False
                    break
        rec.append((prime, tuple(add_maybe_prime)))
    for i in range(10, limit, 10):
        square_i, j = i * i, 0
        while j < len(rec) and square_i > primes[j]:
            if not rec[j][1][i % primes[j]]:
                break
            j += 1
        else:
            for add in adds2:
                if is_probably_prime(square_i + add):
                    break
            else:
                for add in adds1:
                    if not is_probably_prime(square_i + add):
                        break
                else:
                    result += i
    return result


if __name__ == "__main__":
    print(solve())
