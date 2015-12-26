# -*- coding: utf-8 -*-
# !/bin/env python2


def solve():
    i = 1
    while True:
        i1, i2, i3 = str(i * 1), str(i * 2), str(i * 3)
        i4, i5, i6 = str(i * 4), str(i * 5), str(i * 6)
        if (
            len(i1) == len(i2) == len(i3) == len(i4) and
            len(i4) == len(i5) == len(i6)
        ):
            l1, l2, l3 = sorted(i1), sorted(i2), sorted(i3)
            l4, l5, l6 = sorted(i4), sorted(i5), sorted(i6)
            if l1 == l2 == l3 == l4 == l5 == l6:
                return i
        i += 1


if __name__ == "__main__":
    print solve()
