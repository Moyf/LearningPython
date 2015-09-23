#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
注意！！！
这个源文件是专门为了对付不带 **标题** 的第三个笔记写的！！
'''

# 导入正则表达式的库
import re

# -----------------------------------------------------------
# saveToThreeLists() - 将导入的文本每一行分别提取内容的函数
def saveToThreeLists(e, indexList, titleList, contentList):
	matchResult = re.search(r'(^\d{1,2}\.\s)(\S*)(.*)', e, re.M) 
	''' ↑↑↑ 这里可以用 [\S*] 去一直匹配到遇到空格为止'''

	# 这个 [matchResult] 已经是匹配完的 re 类型数据（结果）
	if matchResult:
		count = len(matchResult.groups()) # 匹配出来的元组数量，正常情况下是3组 
		i = 0
		tempIndex = int(re.match(r'\d{1,2}', matchResult.group(1)).group(0))
		# print '这次获取的序号为 %i' % tempIndex
		indexList.append(tempIndex)

		tempTitle = re.sub(r'\*\*',  '', matchResult.group(2))
		titleList.append(tempTitle)

		tempContent = matchResult.group(3)
		# tempContent = re.sub('\n', tempContent, '')
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



def transFiles(textFile, outputFile):

	# 导入文件内容
	text = getImportedText(textFile)

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
		tempOutputString = '%d. **%s** %s\n' % (indexList[i], titleList[i], contentList[i])
		outputLists.append(tempOutputString)
		i = i + 1


	# 打开待写入的文件
	output = open(outputFile, 'w')
	output.writelines(outputLists)
	output.close()


# transFiles('./Ref/AET_01_原文.txt', './Ref/AET_01_导出.md')
# transFiles('./Ref/AET_02_原文.txt', './Ref/AET_02_导出.md')
transFiles('./Ref/AET_03_原文.txt', './Ref/AET_03_特殊导出.md')

