# !/bin/env python2
# -*- coding: utf-8 -*-

import Queue
import urllib
from collections import defaultdict


def solve():
    response = urllib.urlopen(
        "https://projecteuler.net/project/resources/p083_matrix.txt"
    )
    mp, _mp, line = defaultdict(lambda: []), [], response.readline()[:-1]
    while line != "":
        _mp.append(map(int, line.split(",")))
        line = response.readline()[:-1]
    m, n, cnt = len(_mp), len(_mp[0]), 0
    moves = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    for i in range(m):
        for j in range(n):
            _mp[i][j] = (cnt, _mp[i][j])
            cnt += 1
    for x in range(m):
        for y in range(n):
            for move in moves:
                nx, ny = x + move[0], y + move[1]
                if nx < 0 or nx >= m or ny < 0 or ny >= n:
                    continue
                mp[_mp[x][y][0]].append(_mp[nx][ny])
    return spfa(0, mp, _mp[0][0][1])


def spfa(root, mp, start_v):
    n, q = len(mp), Queue.Queue()
    vis = [False for i in range(n)]
    in_q = [0 for i in range(n)]
    dist = [0xFFFFFFFF for i in range(n)]
    vis[root], dist[root], in_q[root] = False, start_v, 1
    q.put(root)
    while not q.empty():
        u = q.get()
        vis[u] = False
        for son in mp[u]:
            v, w = son[0], son[1]
            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                if not vis[v]:
                    in_q[v] += 1
                    if in_q[v] > n:
                        return -1
                    vis[v] = True
                    q.put(v)
    return dist[-1]


if __name__ == "__main__":
    print solve()
