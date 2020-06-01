#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Counting inversions. """


def merge_and_count(first, second):
    f_max = len(first)
    s_max = len(second)
    f, s = 0, 0
    inversion = 0
    out = []
    for _ in range(f_max + s_max):
        if f >= f_max:
            out.append(second[s])
            s += 1
        elif s >= s_max:
            out.append(first[f])
            f += 1
        else:
            if first[f] < second[s]:
                out.append(first[f])
                f += 1
            else:
                out.append(second[s])
                s += 1
                inversion += f_max - f

    return out, inversion


def sort_and_count(a):
    n = len(a)
    if n <= 1:
        return a, 0
    else:
        b, x = sort_and_count(a[: n // 2])
        c, y = sort_and_count(a[n // 2 :])
        d, z = merge_and_count(b, c)
        return d, x + y + z


def count_inversions(array):
    _, inversions = sort_and_count(array)
    return inversions


if __name__ == "__main__":
    fname = "input.txt"

    with open(fname, mode="r") as fin:
        data = fin.readlines()
    data = [int(x.strip()) for x in data if x.strip()]

    result = count_inversions(data)
    print("result:", result)
