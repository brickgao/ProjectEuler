# !/bin/env python2
# -*- coding: utf-8 -*-


def solve():
    primes, result, i = [2], 2, 3
    while True:
        tag = True
        for prime in primes:
            if i % prime == 0:
                tag = False
                break
        if tag:
            primes.append(i)
            if result * i > 1000000:
                return result
            else:
                result *= i
        i += 1
    return -1


if __name__ == "__main__":
    print solve()
