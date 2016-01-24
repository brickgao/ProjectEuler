# -*- coding: utf-8 -*-
# !/bin/env python2

import urllib


def solve():
    response = urllib.urlopen(
        "https://projecteuler.net/project/resources/p082_matrix.txt"
    )
    mp, line = [], response.readline()[:-1]
    while line != "":
        mp.append(map(int, line.split(",")))
        line = response.readline()[:-1]
    m, n = len(mp), len(mp[0])
    dp = [[0] * n for i in range(m)]
    for i in range(m):
        dp[i][0] = mp[i][0]
    for j in range(1, n):
        dp[0][j] = dp[0][j - 1] + mp[0][j]
        for i in range(1, m):
            dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + mp[i][j]
        for i in range(m - 2, -1, -1):
            dp[i][j] = min(dp[i][j], dp[i + 1][j] + mp[i][j])
    return min(map(lambda l: l[-1], dp))


if __name__ == "__main__":
    print solve()
