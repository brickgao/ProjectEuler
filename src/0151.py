#!/bin/env python3
# -*- coding: utf-8 -*-


def solve():
    rec = {}

    def dfs(now):
        nonlocal rec
        if now not in rec:
            result = 0.0
            if len(now) > 0:
                for i in range(len(now)):
                    selected, nxt = now[i], list(now[:i] + now[i + 1:])
                    for j in range(selected + 1, 6):
                        nxt.append(j)
                    nxt = tuple(sorted(nxt))
                    result += dfs(nxt)
                result /= len(now)
                result += 1.0 if len(now) == 1 else 0.0
            rec[now] = result
        return rec[now]

    return "{:.6f}".format(dfs((1, )) - 2)


if __name__ == "__main__":
    print(solve())
