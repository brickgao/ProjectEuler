#!/bin/env python2
# -*- coding: utf-8 -*-

import urllib


class Path(object):

    def __init__(self, u, v, c):
        self.u, self.v, self.c = u, v, c

    def __repr__(self):
        return str((self.u, self.v, self.c))


def solve():
    response = urllib.urlopen(
        "https://projecteuler.net/project/resources/p107_network.txt"
    )
    l, line, x = [], response.readline(), 0
    while line != "":
        line = line[:-1] if line.endswith("\n") else line
        data = line.split(",")
        for y in range(len(data)):
            if data[y] != "-":
                l.append(Path(x + 1, y + 1, int(data[y])))
        line, x = response.readline(), x + 1

    l, n, m = sorted(l, key=lambda x: x.c), x, len(l)
    parent, rk = [i for i in range(0, n + 1)], [0 for i in range(0, n + 1)]

    def getparent(x):
        if parent[x] == x:
            return x
        else:
            parent[x] = getparent(parent[x])
            return parent[x]

    def unionset(x, y):
        if rk[x] > rk[y]:
            parent[y] = x
        else:
            parent[x] = y
            if rk[x] == rk[y]:
                rk[y] += 1

    def mst():
        vis, result, cnt = [False for i in range(m)], 0, 0
        for i in range(m):
            x, y = getparent(l[i].v), getparent(l[i].u)
            if x != y:
                unionset(x, y)
                cnt, result = cnt + 1, result + l[i].c
                vis[i] = True
                if cnt == n - 1:
                    break
        return result

    return sum(map(lambda x: x.c, l)) / 2 - mst()


if __name__ == "__main__":
    print solve()
