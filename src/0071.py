# !/bin/env python2
# -*- coding: utf-8 -*-


def solve():
    upper, delta = 1000000, float(3) / float(7)
    result, minn = -1, ""
    for i in range(upper, upper - 7, -1):
        if i % 7 == 0:
            continue
        numerator = int(float(i) * delta)
        frac = float(numerator) / float(i)
        if abs(frac - delta) < minn:
            minn, result = abs(frac - delta), "{0} / {1}".format(numerator, i)
    print result


if __name__ == "__main__":
    solve()
