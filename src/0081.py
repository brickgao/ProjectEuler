# -*- coding: utf-8 -*-
# !/bin/env python2

import urllib


def solve():
    response = urllib.urlopen(
        "https://projecteuler.net/project/resources/p081_matrix.txt"
    )
    mp, line = [], response.readline()[:-1]
    while line != "":
        mp.append(map(int, line.split(",")))
        line = response.readline()[:-1]
    m, n = len(mp), len(mp[0])
    dp = [[0] * n for i in range(m)]
    for i in range(m):
        for j in range(n):
            if i == 0 and j == 0:
                dp[i][j] = mp[i][j]
            elif i == 0:
                dp[i][j] = dp[i][j - 1] + mp[i][j]
            elif j == 0:
                dp[i][j] = dp[i - 1][j] + mp[i][j]
            else:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + mp[i][j]
    return dp[m - 1][n - 1]


if __name__ == "__main__":
    print solve()
