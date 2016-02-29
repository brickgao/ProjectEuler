#!/bin/env python3
# -*- coding: utf-8 -*-

import math
import itertools
import functools

result, l = 0, []


@functools.lru_cache(maxsize=None)
def is_primes(num):
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True if num >= 2 else False


def dfs(left, last="0"):
    global result, l
    if left == "":
        result += 1
    else:
        _last = int(last)
        for i in range(len(last), len(left) + 1):
            now, _now = left[:i], int(left[:i])
            if _now > _last and is_primes(_now):
                l.append(_now)
                dfs(left[i:], now)
                l.pop()


def solve():
    for digtals in itertools.permutations("123456789"):
        dfs("".join(digtals))
    return result


if __name__ == "__main__":
    print(solve())
