#!/bin/env python3
# -*- coding: utf-8 -*-

import math


def solve():
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43]
    exponents, limit = [0 for i in range(len(primes))], 2 * 4000000 - 1

    def get_twos(limit):
        exponents[0], divisors = 0, 1
        for exponent in exponents:
            divisors *= exponent * 2 + 1
        exponents[0] = (limit / divisors - 1) // 2
        while divisors * (2 * exponents[0] + 1) < limit:
            exponents[0] += 1

    def get_number():
        ret = 1
        for i in range(len(primes)):
            if exponents[i] > math.log(limit, primes[i]) + 1:
                return float("Inf")
            ret *= math.pow(primes[i], exponents[i])
        return int(ret)

    result, cnt = 1, 1
    for prime in primes:
        result *= prime
    while True:
        get_twos(limit)
        if exponents[0] < exponents[1]:
            cnt += 1
        else:
            num, cnt = get_number(), 1
            result = num if num < result else result
        if cnt >= len(primes):
            break
        exponents[cnt] += 1
        for i in range(cnt):
            exponents[i] = exponents[cnt]
    return result


if __name__ == "__main__":
    print(solve())
