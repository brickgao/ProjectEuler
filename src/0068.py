# !/bin/env python2
# -*- coding: utf-8 -*-

import itertools


def solve():
    result = "0" * 16
    for l in itertools.permutations(list(range(1, 11))):
        if 10 not in l[:5]:
            continue
        tag = [(l[0], l[5], l[6]),
               (l[1], l[6], l[7]),
               (l[2], l[7], l[8]),
               (l[3], l[8], l[9]),
               (l[4], l[9], l[5])]
        pos, minn = 0, 11
        for i in range(5):
            if tag[i][0] < minn:
                minn, pos = tag[i][0], i
        tag = tag[pos:] + tag[:pos]
        line_sum = sum(tag[0])
        if all(map(lambda x: sum(x) == line_sum, tag)):
            s = "".join(map(lambda x: "".join(map(str, x)), tag))
            result = max(result, s)
    print result


if __name__ == "__main__":
    solve()
