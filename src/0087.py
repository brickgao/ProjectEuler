# !/bin/env python2
# -*- coding: utf-8 -*-

import math


def get_primes():
    result = []
    for i in range(2, 7100):
        tag = False if i > 2 and i % 2 == 0 else True
        if tag:
            for j in range(3, int(math.sqrt(i)) + 1, 2):
                if i % j == 0:
                    tag = False
                    break
        if tag:
            result.append(i)
    return result


def solve():
    primes = get_primes()
    primes_pow = []
    for prime in primes:
        tmp_list = [prime * prime]
        for i in range(2):
            tmp_list.append(tmp_list[-1] * prime)
        primes_pow.append(tmp_list)
    result, primes_len = set(), len(primes)
    for i in range(primes_len):
        for j in range(primes_len):
            for k in range(primes_len):
                num = primes_pow[i][0] + primes_pow[j][1] + primes_pow[k][2]
                if num > 50000000:
                    break
                result.add(num)
    return len(result)


if __name__ == "__main__":
    print solve()
