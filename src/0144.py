#!/bin/env python3
# -*- coding: utf-8 -*-

import math


def solve():
    result = 0
    A, O = (0, 10.1), (1.4, -9.6)
    while O[0] > 0.01 or O[0] < -0.01 or O[1] < 0:
        slopeA = (O[1] - A[1]) / (O[0] - A[0])
        slopeO = - 4 * O[0] / O[1]
        _slope = (slopeA - slopeO) / (1 + slopeA * slopeO)
        slopeB = (slopeO - _slope) / (1 + _slope * slopeO)
        interceptB = O[1] - slopeB * O[0]

        a = 4 + slopeB * slopeB
        b = 2 * slopeB * interceptB
        c = interceptB * interceptB - 100

        _x1 = (-b + math.sqrt(b * b - 4 * a * c)) / (2 * a)
        _x2 = (-b - math.sqrt(b * b - 4 * a * c)) / (2 * a)

        A = O

        Ox = _x1 if abs(_x1 - O[0]) > abs(_x2 - O[0]) else _x2
        O = (Ox, Ox * slopeB + interceptB)

        result += 1
    return result


if __name__ == "__main__":
    print(solve())
