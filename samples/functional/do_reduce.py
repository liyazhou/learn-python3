#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from functools import reduce


def add(x, y):
    return x + y


print(reduce(add, [1, 2, 3]))

CHAR_TO_INT = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9
}


def char2num(s):
    return CHAR_TO_INT[s]


def fn(x, y):
    return x * 10 + y


print(reduce(fn, map(char2num, '123')))


def str2int1(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))


def str2int(s):
    ints = map(lambda ch: CHAR_TO_INT[ch], s)
    return reduce(lambda x, y: x * 10 + y, ints)


print(str2int1('0'))
print(str2int1('12300'))
print(str2int1('0012345'))
print(str2int('0'))
print(str2int('12300'))
print(str2int('0012345'))

CHAR_TO_FLOAT = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '.': -1
}


def str2float(s):
    nums = map(lambda ch: CHAR_TO_FLOAT[ch], s)
    point = 0

    def to_float(f, n):
        nonlocal point
        if n == -1:
            point = 1
            return f
        if point == 0:
            return f * 10 + n
        else:
            point *= 10
            return f + n / point

    return reduce(to_float, nums, 0.0)


def str2float2(s):
    nums = map(lambda ch: CHAR_TO_FLOAT[ch], s)
    point = 0

    def to_float(f, n):
        nonlocal point
        if n == -1:
            point = 1
            return f
        if point == 0:
            return f * 10 + n
        else:
            point *= 10
            return f + n / point

    return reduce(to_float, nums, 0.0)


print(str2float('0'))
print(str2float('123.456'))
print(str2float('123.45600'))
print(str2float('0.1234'))
print(str2float('.1234'))
print(str2float('120.0034'))

print(str2float2('0'))
print(str2float2('123.456'))
print(str2float2('123.45600'))
print(str2float2('0.1234'))
print(str2float2('.1234'))
print(str2float2('120.0034'))
