# !/bin/env python2
# -*- coding: utf-8 -*-

import itertools
from operator import add, sub, mul, truediv


def solve():
    maxn, result = 0, ()
    for digitals in itertools.combinations(range(1, 10), 4):
        s = set()
        for nums in itertools.permutations(digitals):
            for op in itertools.product([add, sub, mul, truediv], repeat=4):
                tmp = op[0](op[1](nums[0], nums[1]), op[2](nums[2], nums[3]))
                if int(tmp) == tmp:
                    s.add(tmp)
                tmp = op[0](op[1](op[2](nums[0], nums[1]), nums[2]), nums[3])
                if int(tmp) == tmp:
                    s.add(tmp)
        cnt = 1
        while cnt in s:
            cnt += 1
        if cnt - 1 > maxn:
            maxn, result = cnt - 1, digitals
    return "".join(map(str, sorted(result)))


if __name__ == "__main__":
    print solve()
