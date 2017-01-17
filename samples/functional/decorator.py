#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import functools


def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)

    return wrapper


@log
def now():
    print('2015-3-25')


now()


def log2(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)

    return wrapper


def now2():
    print('2016-10-01')


print('log2')
f = log2(now2)
f()


@log2
def now3():
    print('2017年01月17日')


now3()


def logger(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)

        return wrapper

    return decorator


@logger('DEBUG')
def today():
    print('2015-3-25')


today()
print(today.__name__)


def logger2(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kwargs)

        return wrapper

    return decorator


@logger2('debug')
def today2():
    print('2017年01月18日')


today2()
print(today2.__name__)
