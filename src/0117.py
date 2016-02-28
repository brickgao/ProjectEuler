#!/bin/env python3
# -*- coding: utf-8 -*-


def solve():
    dp = [1, 1, 2, 4, 8] + [0 for i in range(46)]
    for i in range(5, 51):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3] + dp[i - 4]
    return dp[50]


if __name__ == "__main__":
    print(solve())
