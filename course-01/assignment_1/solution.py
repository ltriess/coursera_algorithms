#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Integer Multiplication """


import sys


def split_at(num: int, idx: int) -> (int, int):
    lm = len(str(num))
    if lm > 2:
        upper = int(str(num)[:-idx])
        lower = int(str(num)[-idx:])
    elif lm == 2:
        upper = int(str(num)[0])
        lower = int(str(num)[1])
    elif lm == 1:
        upper = 0
        lower = num
    else:
        raise AssertionError()

    return upper, lower


def karatsuba(x: int, y: int) -> int:
    # x = a * 10^(n/2) + b
    # y = c * 10^(n/2) + d
    # xy = ac * 10^n + (ad + bc) * 10^(n/2) + bd

    if x < 10 or y < 10:
        return x * y

    m = min(len(str(x)), len(str(y)))
    m = m // 2

    a, b = split_at(x, m)
    c, d = split_at(y, m)

    s0 = karatsuba(a, c)
    s1 = karatsuba(b, d)
    s3 = karatsuba(a + b, c + d)

    return s0 * 10 ** (2 * m) + (s3 - s0 - s1) * 10 ** m + s1


if __name__ == "__main__":
    sys.stdin = open("input.txt")

    _x = int(input())
    _y = int(input())
    print("{x} * {y} =".format(x=_x, y=_y))

    result = karatsuba(_x, _y)
    print(result)
