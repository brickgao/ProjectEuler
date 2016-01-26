# !/bin/env python2
# -*- coding: utf-8 -*-

import random


def solve():
    cnts = [0 for i in range(40)]
    pos, round, cnt_equal = 0, 0, 0
    cc = {
        1: 0,
        2: 10
    }
    ch = {
        1: 0,
        2: 10,
        3: 11,
        4: 24,
        5: 39,
        6: 5,
    }
    R, U = [5, 15, 25, 35], [12, 28]
    while round < 1000000:
        val1, val2 = random.randint(1, 4), random.randint(1, 4)
        cnt_equal = cnt_equal + 1 if val1 == val2 else 0
        if cnt_equal >= 3:
            pos, cnt_equal = 10, 0
        pos = (pos + val1 + val2) % 40
        if pos == 30:
            pos = 10
        if pos == 2 or pos == 17 or pos == 33:
            dice = random.randint(1, 16)
            if dice in cc:
                pos = cc[dice]
        if pos == 7 or pos == 22 or pos == 36:
            dice = random.randint(1, 16)
            if dice in ch:
                pos = ch[dice]
            if dice == 7 or dice == 8:
                for nxt in R:
                    if nxt > pos:
                        break
                pos = nxt if nxt > pos else R[0]
            if dice == 9:
                for nxt in U:
                    if nxt > pos:
                        break
                pos = nxt if nxt > pos else U[0]
            if dice == 10:
                pos = (pos - 3 + 40) % 40
        cnts[pos] += 1
        round += 1
    rec = sorted(zip(
        map(lambda x: x / 1000000., cnts),
        range(0, 40)
    ))
    return "".join(map(str, map(lambda l: l[1], rec[:-4:-1])))


if __name__ == "__main__":
    print solve()
