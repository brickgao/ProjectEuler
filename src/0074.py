# !/bin/env python2
# -*- coding: utf-8 -*-

fac_list = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]


def get_nxt(now):
    ret = 0
    while now > 0:
        ret += fac_list[now % 10]
        now = now // 10
    return ret


def solve():
    result, memo = 0, dict()
    for i in range(1000001):
        now, vis = i, set()
        while now not in vis and now not in memo:
            vis.add(now)
            now = get_nxt(now)
        memo[i] = memo[now] + len(vis) if now in memo else len(vis)
        if memo[i] == 60:
            result += 1
    return result


if __name__ == "__main__":
    print solve()
