# -*- coding: utf-8 -*-

mp = []  # Fill in mp

dp = [[0 for x in range(15)] for y in range(15)]
for i in range(15):
    dp[14][i] = mp[14][i]
for i in range(13, -1, -1):
    for j in range(i + 1):
        dp[i][j] = max(dp[i + 1][j], dp[i + 1][j + 1]) + mp[i][j]
print dp[0][0]
