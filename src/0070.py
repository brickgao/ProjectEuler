# !/bin/env python2
# -*- coding: utf-8 -*-

import math


def get_primes():
    upper, primes = 5000, []
    for i in range(2, upper):
        tag = True
        for j in range(2, int(math.sqrt(i)) + 1):
            if i % j == 0:
                tag = False
        if tag:
            primes.append(i)
    return primes


def solve():
    primes, minn, result = get_primes(), 10000000.0, -1
    for i in range(len(primes)):
        for j in range(i):
            n, phi_n = primes[i] * primes[j], (primes[i] - 1) * (primes[j] - 1)
            if n >= 10000000:
                continue
            if sorted(str(phi_n)) == sorted(str(n)):
                if float(n) / float(phi_n) < minn:
                    minn, result = float(n) / float(phi_n), n
    return result


if __name__ == "__main__":
    print solve()
