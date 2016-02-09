# !/bin/env python2
# -*- coding: utf-8 -*-

import math
import urllib
import itertools


def is_square(num):
    return True if int(math.sqrt(num)) ** 2 == num else False


def solve():
    data = urllib.urlopen(
        "https://projecteuler.net/project/resources/p098_words.txt"
    ).read().split(",")
    words, words_pairs = [(w[1:-1], sorted(w[1:-1])) for w in data], []
    length, result = len(words), 0
    for i in range(length):
        for j in range(i, length):
            if words[i][1] == words[j][1] and words[i][0] != words[j][0]:
                words_pairs.append((words[i][0], words[j][0]))
    for word1, word2 in words_pairs:
        alphas = list(set(word1))
        for digitals in itertools.permutations("123456789", len(alphas)):
            alpha2digital = dict(zip(alphas, digitals))
            num1, num2 = (
                int("".join(alpha2digital[ch] for ch in word1)),
                int("".join(alpha2digital[ch] for ch in word2)),
            )
            if is_square(num1) and is_square(num2):
                result = max(result, num1, num2)
    return result


if __name__ == "__main__":
    print solve()
