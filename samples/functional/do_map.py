#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def f(x):
    return x * x


print(list(map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])))


def f2(x):
    return x * x


print(list(map(f2, [1, 2, 3])))

print(list(map(str, [1, 2, 3])))
