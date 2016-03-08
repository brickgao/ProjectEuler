#!/bin/env python3
# -*- coding: utf-8 -*-


def get_cube_layer_cost(x, y, z, n):
    return 2 * (x * y + y * z + x * z) + 4 * (x + y + z + n - 2) * (n - 1)


def solve():
    limit, x, result = 30000, 1, 1
    rec = [0] * (limit + 1)
    while get_cube_layer_cost(x, x, x, 1) <= limit:
        y = x
        while get_cube_layer_cost(x, x, y, 1) <= limit:
            z = y
            while get_cube_layer_cost(x, y, z, 1) <= limit:
                n = 1
                while get_cube_layer_cost(x, y, z, n) <= limit:
                    rec[get_cube_layer_cost(x, y, z, n)] += 1
                    n += 1
                z += 1
            y += 1
        x += 1
    while rec[result] != 1000:
        result += 1
    return result


if __name__ == "__main__":
    print(solve())
