# !/bin/env python2
# -*- coding: utf-8 -*-

import math


def solve():
    l, count = 2, 0
    while count < 1000000:
        l += 1
        for w_add_h in range(3, 2 * l + 1):
            path_len_pow2 = w_add_h * w_add_h + l * l
            path_len = int(math.sqrt(path_len_pow2))
            if path_len * path_len == path_len_pow2:
                count += (
                    w_add_h / 2 if w_add_h <= l else 1 + l - (w_add_h + 1) / 2
                )
    return l

if __name__ == "__main__":
    print solve()
