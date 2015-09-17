#!/usr/bin/python
# -*- coding: utf-8 -*-
# 测试中文字符的编码方式，以及如何输出中文字符

s0 = '普通的中文'
s0.decode('utf-8')
# s1 = u'前面加 U 的中文'

print s0
#print s1


file = open('/Users/Moy/Documents/Code/Python/Ref/test.txt')
text = file.readlines()


for eachLine in text:
	if eachLine:
		print eachLine

	else:
		print "failed"


