# !/bin/env python2
# -*- coding: utf-8 -*-

limit = 12000
rec = [2 * limit] * limit


def solve(product_now, sum_now, num_of_factors, start):
    k = product_now - sum_now + num_of_factors
    if k < limit:
        if product_now < rec[k]:
            rec[k] = product_now
        for i in range(start, 2 * limit // product_now):
            solve(product_now * i, sum_now + i,
                  num_of_factors + 1, i)


if __name__ == "__main__":
    solve(1, 1, 1, 2)
    print sum(set(rec[2:]))
