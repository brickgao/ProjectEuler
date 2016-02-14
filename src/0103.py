# !/bin/env python2
# -*- coding: utf-8 -*-

import math
from itertools import combinations, product


def solve():
    LEN = 7
    result, sum_result, possible = [], 0XFFFFFFF, [20, 31, 38, 39, 40, 42, 45]
    for delta in product(range(-3, 4), repeat=LEN):
        _possible = [possible[i] + delta[i] for i in range(len(possible))]
        if len(set(_possible)) != LEN:
            continue
        _sum_possible = sum(_possible)
        if _sum_possible < sum_result:
            _possible.sort()
            _sum1, _sum2 = _possible[0], 0
            tag = True
            for i in range(int(math.ceil(LEN / 2))):
                _sum1 += _possible[i + 1]
                _sum2 += _possible[LEN - i - 1]
                if _sum1 <= _sum2:
                    tag = False
                    break
            if not tag:
                continue
            for length1 in range(LEN):
                for c1 in combinations(_possible, length1 + 1):
                    _nxt = set(_possible) - set(c1)
                    _nxt_len = len(_nxt)
                    _sum1 = sum(c1)
                    if _nxt_len == 0:
                        continue
                    for length2 in range(_nxt_len):
                        for c2 in combinations(_nxt, length2 + 1):
                            _sum2 = sum(c2)
                            if _sum1 == _sum2:
                                tag = False
                                break
                        if not tag:
                            break
                    if not tag:
                        break
                if not tag:
                    break
            if tag:
                result, sum_result = _possible, sum(_possible)
    return "".join(map(str, result))


if __name__ == "__main__":
    print solve()
