# !/bin/env python2
# -*- coding: utf-8 -*-


def solve():
    rec, result, limit = {89: True, 1: False}, 0, 9 * 9 * 7 + 1
    for i in range(1, limit):
        now, process = i, []
        while now not in rec:
            process.append(now)
            now = sum(map(lambda x: x * x, map(int, str(now))))
        for num in process:
            rec[num] = rec[now]
    for i in range(1, 10000001):
        now = i
        while now not in rec:
            tmp, now = now, 0
            while tmp > 0:
                tmp, digital = tmp / 10, tmp % 10
                now += digital * digital
        if rec[now]:
            result += 1
    return result


if __name__ == "__main__":
    print solve()
