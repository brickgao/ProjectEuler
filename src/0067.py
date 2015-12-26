# -*- coding: utf-8 -*-

mp = []  # Fill in mp
dp = [[0 for x in range(100)] for y in range(100)]
for i in range(100):
    dp[99][i] = mp[99][i]
for i in range(98, -1, -1):
    for j in range(i + 1):
        dp[i][j] = max(dp[i + 1][j], dp[i + 1][j + 1]) + mp[i][j]
print dp[0][0]
