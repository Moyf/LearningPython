#!/usr/bin/python
# -*- coding: utf-8 -*-
# 这里是 Python 中各种正则表达式的实验场

# 导入正则表达式的库
import re

# 判断是否为字符串类型
def isString(s):
	return isinstance(s, basestring)

# 默认的文本
line = '''
1. **标题一** 正文1，以及
正文1补充
2. **标题二** 正文2
3. **标题三** 正文3
'''


lineList = ['1. **标题一** 正文1，以及', '正文1补充', '2. **标题二** 正文2', '3. **标题三** 正文3']

print '原始文本:\n %s\n\n' % line

# 三个列表，分别储存三部分的元组。把三个列表填充满了再统一格式化输出。
indexList = []
titleList = []
contentList = []

for e in lineList:
	# print e
	matchResult = re.search(r'(^\d\.\s)(\*\*.*\*\*)(.*)', e, re.M)

	# 这个 [matchResult] 已经是匹配完的 re 类型数据（结果）
	if matchResult:
		count = len(matchResult.groups()) # 匹配出来的元组数量，正常情况下是3组 
		i = 0
		tempIndex = int(re.match(r'\d', matchResult.group(1)).group(0))
		# print '这次获取的序号为 %i' % tempIndex
		indexList.append(tempIndex)

		tempTitle = re.sub(r'\*\*',  '', matchResult.group(2))
		titleList.append(tempTitle)

		tempContent = matchResult.group(3)
		contentList.append(tempContent)

		while (i < count):
			i = i+1
			# print '第 %i 点，元组 %i ：%s \n' % (tempIndex, i, matchResult.group(i)),
	else:
		theIndex = len(indexList) # 需要添加到前一点的末尾中
		print '在列表第 %i 个元素中无匹配项，已将内容 "%s" 添加至第 %d 点' % ((lineList.index(e)+1), e, theIndex)
		contentList[theIndex-1] = contentList[theIndex-1] + '  %s' % e


tipsCount = len(indexList)
i = 0 # 这个小 i 是计数君
while (i < tipsCount):
	print '| %d\t| %s\t|%s\t|' % (indexList[i], titleList[i], contentList[i])
	i = i + 1

'''
for i in indexList:
	print i

for t in titleList:
	print t

for c in contentList:
	print c
'''

# 提取标题（如果有）
# title = re.search(r'^\d\. \*\*(.*)\*\* (.*)', line, re.I).groups()

# 提取各个元组的成分，包括标题和后面的正文，并且要能把换行的正文重新加入
'''
matchResult = re.search(r'(^\d\.\s)(\*\*.*\*\*)(.*)', line, re.M)

if matchResult:
	count = len(matchResult.groups())
	i = 0
	while (i < count):
		i = i+1
		print '组 %i ：%s \n' % (i, matchResult.group(i))

'''

# if (title != None):
	
# findO = re.match(r'\d\. \*\*(.*)\*\* (.*)', line, re.I)
# replace = str('| ' + str(findO.group(1)) + ' |')
# print 'Title: ' + title


# output = re.sub('\d\. \*\*(.*)\*\*', replace, str(findO))

#print findO.group(0)

'''
if findO:
	print "groups(): ", findO.groups()
	thisLine = (findO.group(0) + 'XXX' + findO.group(1))
	formatted.append(thisLine)

else:
	print "No Match!"

print 'Output: ' + str(findO.groups())
print 'formatted: ' + formatted[0]
'''

# if matchObj:
#    print "matchObj.group() : ", matchObj.group()
#    print "matchObj.group(0) : ", matchObj.group(0)
#    print "matchObj.group(1) : ", matchObj.group(1)
#    print "matchObj.group(2) : ", matchObj.group(2)
#    print "matchObj.groups() : ", matchObj.groups()
# else:
#    print "No match!!"



def writeToFile(text):
	outputFile = open('./Ref/PyReLab_Output.txt', 'a')
	outputFile.write(text)





