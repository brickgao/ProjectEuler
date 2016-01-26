# !/bin/env python2
# -*- coding: utf-8 -*-


def solve():
    p, n = [1], 1
    while True:
        now, delta, cnt = 0, 1, 0
        while delta <= n:
            sign = -1 if cnt % 4 > 1 else 1
            now = (now + sign * p[n - delta] + 1000000) % 1000000
            cnt += 1
            k = - (cnt / 2) - 1 if cnt % 2 else cnt / 2 + 1
            delta = k * (3 * k - 1) / 2
        p.append(now)
        if now == 0:
            return n
        n += 1
    return -1


if __name__ == "__main__":
    print solve()
