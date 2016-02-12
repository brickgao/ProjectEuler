# !/bin/env python2
# -*- coding: utf-8 -*-


def func(n):
    return (
        1 - n + n ** 2 - n ** 3 + n ** 4 - n ** 5 + n ** 6 - n ** 7 +
        n ** 8 - n ** 9 + n ** 10
    )


def solve():
    # https://en.wikipedia.org/wiki/Lagrange_polynomial
    func_results, ret = [1.0], 1.0
    for i in range(2, 11):
        func_results.append(func(i))
        for j in range(len(func_results)):
            _tmp = 1.0
            for k in range(1, i + 1):
                if k != j + 1:
                    _tmp *= float(i + 1 - k)
                if k != j + 1:
                    _tmp /= float(j + 1 - k)
            ret += _tmp * func_results[j]
    return ret


if __name__ == "__main__":
    print solve()
