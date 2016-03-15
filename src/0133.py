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
    limit, power, result = 10 ** 5, 10 ** 16, 0
    primes = get_prime(limit)
    for prime in primes:
        if pow(10, power, prime) != 1:
            result += prime
    return result


if __name__ == "__main__":
    print(solve())
