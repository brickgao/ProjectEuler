#!/bin/env python3
# -*- coding: utf-8 -*-

import itertools
import collections


def solve():
    colin_record = []
    for p in itertools.product(range(1, 7), repeat=6):
        colin_record.append(sum(p))
    larger_counter, colin_counter = (
        collections.defaultdict(lambda: 0), collections.Counter(colin_record)
    )
    for k in range(4 * 9 + 1):
        for i in range(k):
            larger_counter[k] += colin_counter[i] if i in colin_counter else 0
    all_cnt, win_cnt = (4 ** 9) * len(colin_record), 0
    for p in itertools.product(range(1, 5), repeat=9):
        win_cnt += larger_counter[sum(p)]
    return "{:.7f}".format(win_cnt / all_cnt)


if __name__ == "__main__":
    print(solve())
