#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print(list(map(lambda x: x * x, [1, 2, 3])))

f = lambda x: x * x
print(f)
print(f(1))


def build(x, y):
    return lambda: x * x + y * y


print(build)
print(build(1, 2))
print(build(1, 2)())
