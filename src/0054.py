# -*- coding: utf-8 -*-
# !/bin/env python2

from collections import Counter

mp = {
    "2": 2, "3": 3, "4": 4, "5": 5,
    "6": 6, "7": 7, "8": 8, "9": 9,
    "T": 10, "J": 11, "Q": 12, "K": 13,
    "A": 14,
}


def get_score(l):
    vals, suits = map(lambda _l: _l[0], l), map(lambda _l: _l[1], l)
    num_vals = map(lambda x: mp[x], vals)
    dict_vals = Counter(vals)

    if (set(vals) == set(["T", "A", "J", "K", "Q"]) and
            len(set(suits)) == 1):
        return 10, (0, )

    if (sorted(map(lambda x: x - min(num_vals),
                   num_vals)) == [0, 1, 2, 3, 4] and
            len(set(suits)) == 1):
        return 9, (max(num_vals), )

    if any(map(lambda x: x == 4, dict_vals.values())):
        result = 0
        for val in dict_vals.keys():
            if dict_vals[val] == 4:
                result = mp[val]
        return 8, (result, )

    if set(dict_vals.values()) == set([2, 3]):
        result = dict_vals.keys()
        if dict_vals[result[0]] == 2:
            result = result[::-1]
        return 7, tuple(map(lambda x: mp[x], result))

    if len(set(suits)) == 1:
        return 6, tuple(sorted(num_vals)[::-1])

    if sorted(map(lambda x: x - min(num_vals),
                  num_vals)) == [0, 1, 2, 3, 4]:
        return 5, (max(num_vals), )

    if any(map(lambda x: x == 3, dict_vals.values())):
        result = 0
        for val in dict_vals.keys():
            if dict_vals[val] == 3:
                result = mp[val]
        return 4, (result, )

    cnt_pair = []
    for val in dict_vals.keys():
        val_cnt = dict_vals[val]
        if val_cnt == 2:
            cnt_pair.append(mp[val])

    if len(cnt_pair) == 2:
        return 3, tuple(sorted(cnt_pair)[::-1])

    if len(cnt_pair) == 1:
        return 2, tuple(sorted(cnt_pair))

    return 1, (max(num_vals), )


def read_cards():
    result = 0
    with open("poker.txt", "r") as f:
        while True:
            line = f.readline()
            if line == "":
                break
            line = line.split()
            _player1, _player2 = line[:5], line[5:]
            player1_vals, player1_suits = (
                map(lambda s: s[:-1], _player1),
                map(lambda s: s[-1:], _player1)
            )
            player2_vals, player2_suits = (
                map(lambda s: s[:-1], _player2),
                map(lambda s: s[-1:], _player2)
            )
            player1, player2 = (
                zip(player1_vals, player1_suits),
                zip(player2_vals, player2_suits)
            )
            player1_score, player2_score = (
                get_score(player1),
                get_score(player2)
            )
            if player1_score[0] != player2_score[0]:
                if player1_score[0] > player2_score[0]:
                    result += 1
            else:
                if player1_score[1] == player2_score[1]:
                    player1_num_vals = sorted(map(lambda x: mp[x],
                                                  player1_vals))[::-1]
                    player2_num_vals = sorted(map(lambda x: mp[x],
                                                  player2_vals))[::-1]
                    if player1_num_vals > player2_num_vals:
                        result += 1
                elif player1_score[1] > player2_score[1]:
                    result += 1
    return result


if __name__ == "__main__":
    print read_cards()
