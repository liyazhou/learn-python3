#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3

# 连接到SQLite数据库
# 数据库文件是test.db
# 如果文件不存在，会自动在当前目录创建:
conn = sqlite3.connect('test.db')
# 创建一个Cursor:
cursor = conn.cursor()
# 执行一条SQL语句，创建user表:
cursor.execute('CREATE TABLE user (id VARCHAR(20) PRIMARY KEY, name VARCHAR(20))')
# 继续执行一条SQL语句，插入一条记录:
cursor.execute('INSERT INTO user (id, name) VALUES (\'1\', \'Michael\')')
# 通过rowcount获得插入的行数:
print('rowcount =', cursor.rowcount)
# 关闭Cursor:
cursor.close()
# 提交事务:
conn.commit()
# 关闭Connection:
conn.close()

# 查询记录：
conn = sqlite3.connect('test.db')
cursor = conn.cursor()
# 执行查询语句:
cursor.execute('SELECT * FROM user WHERE id=?', '1')
# 获得查询结果集:
values = cursor.fetchall()
print(values)
cursor.close()
conn.close()
