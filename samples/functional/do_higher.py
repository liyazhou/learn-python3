#!/usr/bin/evn python3
# -*- coding: utf-8 -*-


def add(x, y, fc):
    return fc(x) + fc(y)


print(add(5, -6, abs))

print(abs(-10))
print(abs)
f = abs
print(f)
print(f(10))


def neg(x):
    return -x


print(add(5, -6, neg))
