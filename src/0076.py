# -*- coding: utf-8 -*-
# !/bin/env python2


def solve():
    dp = [1 if not i else 0 for i in range(101)]
    for i in range(1, 100):
        for j in range(i, 101):
            dp[j] += dp[j - i]
    return dp[100]


if __name__ == "__main__":
    print solve()
