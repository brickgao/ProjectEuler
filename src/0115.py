#!/bin/env python3
# -*- coding: utf-8 -*-


def solve():
    limit, i, dp = 1000000, 50, [1 for i in range(50)]
    while dp[-1] < limit:
        now = dp[i - 1] + 1
        for j in range(50, i):
            now += dp[i - j - 1]
        dp.append(now)
        i += 1
    return len(dp) - 1


if __name__ == "__main__":
    print(solve())
