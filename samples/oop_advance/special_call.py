#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Student(object):
    def __init__(self, name='student'):
        self.name = name

    def __call__(self):
        print('My name is %s.' % self.name)


s = Student('Michael')
s()


class Teacher(object):
    def __init__(self, name='teacher'):
        self.name = name

    def __call__(self):
        print('teacher name is %s.' % self.name)


t = Teacher('liyazhou')
t()

print(callable(Student()))
print(callable(Teacher()))
print(callable([1, 2, 3]))
print(callable('123'))
print(callable(max))
