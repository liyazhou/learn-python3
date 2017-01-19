#!/usr/bin/evn python3
# -*- coding: utf-8 -*-


class Student(object):
    name = 'orginal_student'


s = Student()

print(s.name)
print(Student.name)
s.name = 'new_name'
print(s.name)
print(Student.name)
del s.name
print(s.name)
print(Student.name)
