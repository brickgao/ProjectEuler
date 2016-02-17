# !/bin/env python2
# -*- coding: utf-8 -*-


def solve():
    N = 12

    c = [[0 for i in range(N + 1)] for j in range(N + 1)]
    for i in range(N + 1):
        c[i][0] = c[i][i] = 1
        for j in range(1, i):
            c[i][j] = c[i - 1][j] + c[i - 1][j - 1]

    def get_catalan_num(n):
        return c[2 * n][n] / (n + 1)

    result = 0
    for i in range(2, N // 2 + 1):
        result += c[N][i] * c[N - i][i] / 2 - get_catalan_num(i) * c[N][i * 2]
    return result


if __name__ == "__main__":
    print solve()
