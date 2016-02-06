# !/bin/env python2
# -*- coding: utf-8 -*-


def solve():
    limit = 10 ** 6
    nxt = [1 for i in range(limit)]
    for factor in range(2, limit // 2):
        for num in range(2 * factor, limit, factor):
            nxt[num] += factor

    max_len, result = 0, 0
    for num in range(2, limit):
        now, chain = num, [num]
        while now < limit:
            nxt[now], now = limit + 1, nxt[now]
            if now in chain:
                pos = chain.index(now)
                if len(chain) > max_len:
                    result, max_len = min(chain[pos:]), len(chain) - pos
            else:
                chain.append(now)
    return result


if __name__ == "__main__":
    print solve()
