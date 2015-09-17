#!/usr/bin/python
# -*- coding: utf-8 -*-
# 测试中文字符的编码方式，以及如何输出中文字符

# 为了在每次输出字符串的时候打上时间戳，导入时间库
import time

# 用于获取时间戳的函数
def getTimeStamp():
	time_localtime = time.localtime(time.time()) # 注意 time.time() 是函数

	year = time_localtime.tm_year
	month = time_localtime.tm_mon
	day = time_localtime.tm_mday
	hour = time_localtime.tm_hour
	minute = time_localtime.tm_min

	if ( 1 <= month and 9 >= month):
		month = '0' + str(month)
		# print '%r, 1~9月，需要手动加0' % month

	timeStamp = '[%s_%s%s_%s:%s]' % (year, month, day, hour, minute)

	# print timeStamp
	return timeStamp

#
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

# ts = getTimeStamp()
allText = '%s\n%s\n%s\n\n' % (getTimeStamp(), testStr, testUni.encode('utf-8'))

str(getTimeStamp() + testStr + "\n" + testUni.encode('utf-8') + "\n" )

# 新建一个文件以供写入
outputFile = open('./Ref/testUnicodeOutput.txt', 'a+')
outputFile.write(allText)

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


