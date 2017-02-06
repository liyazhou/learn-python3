#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# metaclass是创建类，所以必须从`type`类型派生：
class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)


# 指示使用ListMetaclass来定制类
class MyList(list, metaclass=ListMetaclass):
    pass


L = MyList()
L.add(1)
L.add(2)
L.add(3)
L.add('END')
print(L)


class ListMetaclass2(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)


class MyList2(list, metaclass=ListMetaclass2):
    pass


l2 = MyList2()
l2.add('lyz')
print(l2)
