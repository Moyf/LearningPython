#!/usr/bin/python
# -*- coding: utf-8 -*-
# 注意用好正则表达式

# 导入正则表达式的库
import re

# -----------------------------------------------------------
# saveToThreeLists() - 将导入的文本每一行分别提取内容的函数
def saveToThreeLists(e, indexList, titleList, contentList):
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
		# print '在列表第 %i 个元素中无匹配项，已将内容 "%s" 添加至第 %d 点' % ((text.index(e)+1), e, theIndex)
		contentList[theIndex-1] = contentList[theIndex-1] + '  %s' % e
# -----------------------------------------------------------

# -----------------------------------------------------------
# importText() - 打开一个文本文件，导入所有内容（作为一个列表），关闭文件
def getImportedText(file):
	# 输入源文件
	file = open(file)
	# 获取文本内容（每行）
	text = file.readlines() # 保存下来的是一个列表
	file.close()
	return text
# -----------------------------------------------------------

# 导入文件内容
text = getImportedText('/Users/Moy/Documents/Code/Python/Ref/AET_test.txt')

# 三个列表，分别储存三部分的元组。把三个列表填充满了再统一格式化输出。
indexList = []
titleList = []
contentList = []


# 对每一行进行处理，得到填满的三个数组
for eachLine in text:
	saveToThreeLists(eachLine, indexList, titleList, contentList)

# 生成一个格式化的文本列表
outputLists = []

tipsCount = len(indexList)
i = 0 # 这个小 i 是计数君
while (i < tipsCount):
	tempOutputString = '| %d\t| %s\t|%s\t|\n' % (indexList[i], titleList[i], contentList[i])
	outputLists.append(tempOutputString)
	i = i + 1


# 打开待写入的文件
output = open('/Users/Moy/Documents/Code/Python/Ref/AET_Output.txt', 'w')
output.writelines(outputLists)
output.close()





'''
9月17日写的脚本，比较古早的方式。

# 导入每行的文件
for eachLine in text:
	if eachLine:
		lineNum = lineNum + 1
		# 单独获取第一列（标题列）
		title = re.search('^\d\.\s\*\*.*\S\*\*', eachLine) # 现在还是作为 re 类型的数据
		# title = re.search(r'^\d\.\s\S*', eachLine).group()
		
		# 单独获取标题内容，只提取找到了的行中文本
		if (title != None):
			# 在这里把标题重新格式化
			index = len(titleList)+1 # 用列表长度+1表示元素的序号
			title = re.sub(r'^\d\.',  str('|'+str(index)), title.group(0)) # 把原来的数字替换成标题序号
			title = re.sub(r'\*\*',  '\t|\t', title) # 把加粗的 ** 替换成表格的分隔符
			
			print '[line %r]: %s , type of title is %r' % (index, title, type(title))

			# titleString = str(title.group(0))
			titleList.append(title)
			#print titleString
	else:
		print "failed"

for i in titleList:
	output.write(i)


'''