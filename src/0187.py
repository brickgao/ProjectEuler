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


def binary_search(nums, x):
    l, r = 0, len(nums)
    while l < r:
        mid = (l + r) >> 1
        if x < nums[mid]:
            r = mid
        elif x > nums[mid]:
            l = mid + 1
        elif x == nums[mid]:
            return mid
    return l - 1


def solve():
    result, limit = 0, 10 ** 8 - 1
    primes, sqrt_limit = get_prime(limit // 2), math.sqrt(limit)
    for index, prime in enumerate(primes):
        if prime > sqrt_limit:
            break
        last = binary_search(primes, limit // prime)
        result += last + 1 - index
    return result

if __name__ == "__main__":
    print(solve())
