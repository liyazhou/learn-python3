#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime

with open('test.txt', 'r', encoding='utf-8') as f:
    s = f.read()
    print('open for read...')
    print(s)

with open('test.txt', 'r', encoding='utf-8') as f:
    for line in f.readlines():
        print(line.strip())

with open('test.txt', 'r', encoding='utf-8', errors='ignore') as f:
    s = f.read()
    print(s)

with open('test.txt', 'rb') as f:
    s = f.read()
    print('open as binary for read...')
    print(s)

with open('test.txt', 'w', encoding='utf-8') as f:
    f.write('今天是 ')
    f.write(datetime.now().strftime('%Y-%m-%d'))
