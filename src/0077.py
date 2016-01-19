# -*- coding: utf-8 -*-
# !/bin/env python2

import math


def is_prime(num):
    for i in range(2, int(math.sqrt(num) + 1)):
        if num % i == 0:
            return False
    return True if num >= 2 else False


def solve():
    dp = [1 if not i else 0 for i in range(101)]
    for i in range(1, 100):
        if is_prime(i):
            for j in range(i, 101):
                dp[j] += dp[j - i]
    for i in range(101):
        if dp[i] > 5000:
            return i
    return -1


if __name__ == "__main__":
    print solve()
