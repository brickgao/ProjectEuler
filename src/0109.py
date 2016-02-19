#!/bin/env python2
# -*- coding: utf-8 -*-

from itertools import chain, combinations


def solve():
    result, limit = 0, 100
    scores, doubles = [25, 50], [50]
    for i in range(1, 21):
        scores.extend([i, i * 2, i * 3])
        doubles.append(i * 2)
    for score3 in doubles:
        result += 1 if score3 < limit else 0
    for score2 in scores:
        for score3 in doubles:
            result += 1 if score2 + score3 < limit else 0
    for score12 in chain(combinations(scores, 2), zip(scores, scores)):
        for score3 in doubles:
            result += 1 if sum(score12) + score3 < limit else 0
    return result


if __name__ == "__main__":
    print solve()
