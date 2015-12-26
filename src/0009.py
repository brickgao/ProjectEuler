# -*- coding: utf-8 -*-


def go():
    for i in range(1, 1000):
        for j in range(1, 1000 - i):
            k = 1000 - i - j
            _ = [i, j, k]
            _.sort()
            if _[0] ** 2 + _[1] ** 2 == _[2] ** 2:
                print _[0] * _[1] * _[2]
                return


go()
