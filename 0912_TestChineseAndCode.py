#!/usr/bin/python
# -*- coding: utf-8 -*-
# 测试中文字符的编码方式，以及如何输出中文字符


'''
这一块是用来测试不同的编码字符在 print 时的效果；
'''

testStr = '普通的 Str 中文' # 这样的话，它作为字节串格式的数据，储存的是具体的编码（utf-8）
str2Uni = testStr.decode('utf-8') # 解码后作为 Unicode 字符串储存
# s1 = u'前面加 U 的中文'
testUni = u'普通的 Unicode 中文'

print ('普通的 str 字符串如下：  %s') % testStr
print ('普通的 Unicode 字符串如下：  %s') % testUni.encode('utf-8') # Unicode 字符没法直接输出为字符串，必须经过编码才可以
print '\n'



'''
把不同的编码写入文件会有什么反应呢？
'''

allText = str(testStr + testUni.encode('utf-8'))


print allText

# ↑ 如果尝试直接输出 Unicode 作为字符串，会提示：UnicodeDecodeError: 'ascii' codec can't decode byte 0xe6 in position 0: ordinal not in range(128)




file = open('./Ref/testUTF-8.txt')
text = file.readlines()
file.close()

for eachLine in text:
	if eachLine:
		print eachLine,

	else:
		print "failed"


