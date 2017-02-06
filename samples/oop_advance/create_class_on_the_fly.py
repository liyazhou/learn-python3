#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def fn(self, name='world'): # 先定义函数
    print('Hello, %s.' % name)

Hello = type('Hello', (object,), dict(hello=fn)) # 创建Hello class

h = Hello()
print('call h.hello():')
h.hello()
print('type(Hello) =', type(Hello))
print('type(h) =', type(h))


def fn2(self, name='lyz'):
    print('hello, %s.' % name)


World = type('World', (object,), dict(test=fn2))

w = World()
print('call w.test():')
w.test()
print(type(World))
print(type(w))
