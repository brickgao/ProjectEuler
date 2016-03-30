#!/bin/env python3
# -*- coding: utf-8 -*-


def solve():
    result, n = 0, 1000
    tri, limit = [], n * (n + 1) // 2
    line, line_total, cnt = [], 1, 0
    t, pow_2_19, pow_2_20 = 0, 1 << 19, 1 << 20
    while cnt < limit:
        t = (615949 * t + 797807) % pow_2_20
        s_now = t - pow_2_19
        line.append(s_now)
        if len(line) == line_total:
            tri.append(line)
            line, line_total = [], line_total + 1
        cnt += 1
    sum_tri = [[0] for i in range(n)]
    for x in range(n):
        for y in range(1, x + 2):
            sum_tri[x].append(sum_tri[x][-1] + tri[x][y - 1])
    for x in range(n):
        for y in range(x + 1):
            _sum = 0
            for _x in range(x, n):
                _sum += sum_tri[_x][y + _x - x + 1] - sum_tri[_x][y]
                result = min(_sum, result)
    return result


if __name__ == "__main__":
    print(solve())
