#!/bin/env python3
# -*- coding: utf-8 -*-

import math


def get_prime(n):
    result = [2]
    for i in range(3, n + 1):
        tag = True
        for j in range(2, int(math.sqrt(i)) + 1):
            if i % j == 0:
                tag = False
                break
        if tag:
            result.append(i)
    return result


def solve():
    limit, primes = 10 ** 10, get_prime(300000)
    for n in range(0, len(primes), 2):
        a = primes[n]
        mod = a * a
        if 2 * a * (n + 1) % mod > limit:
            return n + 1


if __name__ == "__main__":
    print(solve())
