#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def is_odd(n):
    return n % 2 == 1


def is_even(n):
    return n % 2 == 0


L = range(100)

print(list(filter(is_odd, L)))
print(list(filter(is_even, L)))


def not_empty(s):
    return s and s.strip()


def not_empty_2(s):
    return s and s.strip()


print(list(filter(not_empty, ['A', '', 'B', None, 'C', '  '])))
print(list(filter(not_empty_2, ['A', '', 'B', None, 'C', '  '])))
