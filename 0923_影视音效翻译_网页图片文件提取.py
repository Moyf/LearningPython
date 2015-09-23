#!/usr/bin/python
# -*- coding: utf-8 -*-
# 这是一个用于获取特定网页音频资源的脚本

import urllib # 网页资源库
import urllib2 # 网页资源库
import re # 正则表达式的库
import os

# 爬虫的类
class Spider:

	# 初始化，在这里设定网址
	def __init__(self):
		self.siteURL = 'http://www.empireonline.com/features/cinema-sound-secrets-foley-artist/'

	# 获取页面，这是一个转换网址序号为完整页面内容的函数
	def getPage(self, pageIndex):
		url = self.siteURL + 'p' + str(pageIndex)
		print '[Info] 当前处理的网址为： ' + url

		# 转换为网址请求及响应
		request = urllib2.Request(url) # 将网址字符串转为请求
		response = urllib2.urlopen(request).read() # 获取请求得到的响应，并读取页面文件
		print '[Info] 页面长度： %i' % len(response)
		print response.decode('utf-8')
		return response.decode('utf-8') # 得到完整的页面内容

	def mkdir(self, path):
		path = path.strip()
		# 判断路径是否存在，返回值为 T/F
		isExists = os.path.exists(path)

		if not isExists:
			os.makedirs(path)
			return True
		else:
			return False

	


	def getContents(self, pageIndex, downloadList):
		page = self.getPage(pageIndex)
		# 用于匹配的正则表达式
		# 原标签：<img alt="" src="/images/uploaded/STA039TD.jpg" style="width: 775px; height: 454px;">
		pattern = re.compile(r'/images/uploaded/(.*?)"', re.I)
		
		# 获取当前页面中所有符合正则表达式的内容
		items = re.findall(pattern, page)
		print '[Info] 本页提取到的文件列表：'
		for item in items:
			imgLink = 'http://www.empireonline.com/images/uploaded/%s' % (item)
			'''这里注意！！ 不要不小心打成 item[0] ——那就只有第一个字母了！你应该用 item 才对！！(除非保存的就是好几个数组，但是这里只有一个！)'''

			linkIndex = len(downloadList)+1
			print ('[%i]: %s' % (linkIndex, imgLink))
			downloadList.append(imgLink)

def mkdir(path):
	path = path.strip()
	# 判断路径是否存在，返回值为 T/F
	isExists = os.path.exists(path)

	if not isExists:
		os.makedirs(path)
		return True
	else:
		return False

# 保存文件
def saveFile(fileURL, fileName):
	mkdir(fileURL)
	u = urllib.urlopen(fileURL)
	data = u.read()
	f = open(fileName, 'wb')
	f.write(data)
	f.close()


spider = Spider()
allFileList = []

for i in range(1, 13):
	spider.getContents(i, allFileList)


for eachLink in allFileList:
	print eachLink
print '共发现 %s 个链接，准备下载...' % (len(allFileList)+1)

prePath = '/Users/Moy/Downloads/Pics/'

gapFlag = False

for eachLink in allFileList:
	if gapFlag:
		ind = allFileList.index(eachLink)+2
	else:
		ind = allFileList.index(eachLink)+1

	if 13 == ind:
		ind = ind+1
		gapFlag = True

	audioName = re.sub(r'http://.*/', '', eachLink)
	audioName = '%s-%s' % (ind, audioName)
	fullPath = prePath + audioName

	print '[%i]: %s (%s)' % (ind, audioName, fullPath)
	saveFile(eachLink, fullPath) # 前参数为音频文件链接，后参数为保存的文件路径

