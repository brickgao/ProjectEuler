#!/bin/env python3
# -*- coding: utf-8 -*-


def solve():
    result = 0
    for a in range(3, 1001):
        now, mod = max(2, a * 2), a * a
        for n in range(3, a * 2 + 1, 2):
            now = max(now, 2 * a * n % mod)
        result += now
    return result


if __name__ == "__main__":
    print(solve())
