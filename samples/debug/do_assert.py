#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def foo(s):
    n = int(s)
    assert n != 0, 'n is zero!'
    return 10 / n


def foo2(s):
    n = int(s)
    assert n != 0, 'n is zero'
    return 10 / n


def main():
    print(foo2('1'))
    foo('0')


main()
