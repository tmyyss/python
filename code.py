#!/usr/bin/python
#coding:utf8

s="中文"
print s
if isinstance(s,unicode):
	print s.encode('gb2312')
else:
	print s.decode('utf-8').encode('gb2312')
