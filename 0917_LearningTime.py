#!/usr/bin/python
# -*- coding: utf-8 -*-
# 临时开的分支，学习时间相关函数和对象

import time


'''
# 要求就是搞清楚几个函数：time.asctime(time.localtime(time.time())) 的意思
# 另外， 把时间按照 [2015_0917_18:11] 的格式输出来，作为时间戳
# 最后，封装称函数，实现“输出当前时间的格式化字符串”的功能
'''

time_time = time.time()	# 1970纪元后经过的浮点秒数
time_localtime = time.localtime(time_time) # 格式化时间戳为本地的时间。 如果sec参数未输入，则以当前时间为转换标准。 
time_asctime = time.asctime(time.localtime(time_time))

print '''Hi, Let's see the times
time.time : %s
time.localtime : %s
time.asctime : %s
''' % (time_time, time_localtime, time_asctime)


'''
# time.time 表示从公元 1970 年到现在经过的秒数（浮点数）；
# 用 time.localtime(sec) 将上述秒数转为本地的时间，无参数则自动转化当前的时间；
# 再用 time.asctime(timeObject) 可以把它作为格式化的字符串输出；
'''


# 接下来开始格式化导出，手动提取时间格式对象的各个元组

def getTimeStamp():

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

print getTimeStamp()
