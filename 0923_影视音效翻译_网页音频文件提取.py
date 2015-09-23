#!/usr/bin/python
# -*- coding: utf-8 -*-
# 这是一个用于获取特定网页音频资源的脚本

import urllib # 网页资源库
import urllib2 # 网页资源库
import re # 正则表达式的库

# 爬虫的类
class Spider:

	# 初始化，在这里设定网址
	def __init__(self):
		self.siteURL = 'http://www.empireonline.com/features/cinema-sound-secrets-foley-artist/'

	# 获取页面，这是一个转换网址序号为完整页面内容的函数
	def getPage(self, pageIndex):
		url = self.siteURL + 'p' + str(pageIndex)
		print url
		# 转换为网址请求及响应
		request = urllib2.Request(url) # 将网址字符串转为请求
		response = urllib2.urlopen(request).read() # 获取请求得到的响应
		print '页面长度： %i' % len(response)
		# print response.decode('utf-8')
		return response.decode('utf-8') # 得到完整的页面内容

	def getContents(self, pageIndex, downloadList):
		page = self.getPage(pageIndex)
		# 用于匹配的正则表达式
		pattern = re.compile(r'data-boourl="(.*?)/boos/(.*?)/embed/', re.I)
		items = re.findall(pattern, page) # 获取当前页面中所有符合正则表达式的内容
		for item in items:
			# print 'item[0] \n' + str(item[0]) + '\n\n AND item[1] \n\n' +str(item[1]) # 打印符合的内容
			mp3Link = '%s/boos/%s.mp3' % (item[0], item[1])
			
			linkIndex = len(downloadList)+1
			print ('[%i]: %s' % (linkIndex, mp3Link))
			downloadList.append(mp3Link)




def mkdir(self, path):
	path = path.strip()
	# 判断路径是否存在，返回值为 T/F
	isExists = os.path.exists(path)

	if not isExists:
		os.makedirs(path)
		return True
	else:
		return False

# 保存音频文件
def saveMp3(audioURL, fileName):
	u = urllib.urlopen(audioURL)
	data = u.read()
	f = open(fileName, 'wb')
	f.write(data)
	f.close()


spider = Spider()
mp3List = []

for i in range(1, 13):
	spider.getContents(i, mp3List)


for eachLink in mp3List:
	print eachLink
print '共发现 %s 个链接，准备下载...' % (len(mp3List)+1)

prePath = '/Users/Moy/Downloads/mp3Download/'


for eachLink in mp3List:
	ind = mp3List.index(eachLink)+1
	audioName = re.sub(r'http://.*?-', '', eachLink)
	fullPath = prePath + audioName

	print '[%i]: %s (%s)' % (ind, audioName, fullPath)
	saveMp3(eachLink, fullPath) # 前参数为音频文件链接，后参数为保存的文件路径










'''
# 1. 打开一个网页并且获取长度

html = urllib2.urlopen('http://image.baidu.com/').read()
print('size is %r' % len(html))

'''


'''
# 2. 直接打印整个网页

response = urllib2.urlopen('http://image.baidu.com')
print response
print response.read()

# Tip：字典的定义与用法

Dict = {'Name': 'Zara', 'Age': 7};
print('Name:%s' % Dict['Name'])

'''


'''
for i in rage(0, 10):
	u = url % (i)

	# 下载数据
	html = urllib2.urlopen(url+page).read()

	# 找到资源信息
	for x in find_re.findall(html):
		values = dict(
			category = x[0],
			name = x[1],
			magnet = x[2],
		)

'''









