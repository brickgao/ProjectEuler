#!/bin/env python3
# -*- coding: utf-8 -*-


def solve():
    N = 200
    path, rec = [], [0 if i <= 1 else N + 1 for i in range(N + 1)]

    def dfs(u, depth):
        nonlocal path, rec, N
        path.append(u)
        for node in path[::-1]:
            if u + node <= N and rec[u + node] >= depth + 1:
                rec[u + node] = depth + 1
                dfs(u + node, depth + 1)
        path.pop()

    dfs(1, 0)
    return sum(rec)


if __name__ == "__main__":
    print(solve())
