#!/bin/env python3
# -*- coding: utf-8 -*-


def solve():
    result = 0
    for length in range(2, 5):
        dp = [1 if i < length else 0 for i in range(51)]
        for i in range(length, 51):
            dp[i] += dp[i - 1] + dp[i - length]
        result += dp[50] - 1
    return result


if __name__ == "__main__":
    print(solve())
