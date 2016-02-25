#!/bin/env python3
# -*- coding: utf-8 -*-


def solve():
    dp = [1 for i in range(60)]
    for i in range(3, 51):
        dp[i] = dp[i - 1] + 1
        for j in range(3, i):
            dp[i] += dp[i - j - 1]
    return dp[50]


if __name__ == "__main__":
    print(solve())
