# -*- coding: utf-8 -*-

e = [1, 2, 5, 10, 20, 50, 100, 200]
dp = [0 for x in range(210)]
dp[0] = 1
for i in e:
    for j in range(i, 201):
        dp[j] += dp[j - i]
print dp[200]
