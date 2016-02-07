# !/bin/env python2
# -*- coding: utf-8 -*-

import queue
import urllib


def solve():
    response = urllib.urlopen(
        "https://projecteuler.net/project/resources/p096_sudoku.txt"
    )
    line, result = response.readline(), 0
    while line != "":
        mp = [response.readline() for i in range(9)]
        if mp[-1].endswith("\n"):
            mp = map(lambda x: x[:-1], mp)
        else:
            mp = map(lambda x: x[:-1], mp[:-1]) + mp[-1:]
        q = queue.Queue()
        q.put("".join(mp))
        while not q.empty():
            now = q.get()
            pos = now.find("0")
            row, col = pos // 9, pos % 9
            availables = {"1", "2", "3", "4", "5", "6", "7", "8", "9"}
            for i in range(9):
                tmp_pos = i * 9 + col
                if now[tmp_pos] in availables:
                    availables.remove(now[tmp_pos])
                tmp_pos = row * 9 + i
                if now[tmp_pos] in availables:
                    availables.remove(now[tmp_pos])
            box_row, box_col = row // 3, col // 3
            for x in range(3):
                for y in range(3):
                    tmp_pos = (box_row * 3 + x) * 9 + box_col * 3 + y
                    if now[tmp_pos] in availables:
                        availables.remove(now[tmp_pos])
            tag = False
            for available in availables:
                nxt = now[:pos] + available + now[pos + 1:]
                if nxt.find("0") == -1:
                    result, tag = result + int(nxt[:3]), True
                    break
                q.put(nxt)
            if tag:
                break
        line = response.readline()
    return result


if __name__ == "__main__":
    print solve()
