#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib2

'一般用 urllib 的库来进行抓取；抓取时需要完整的 URL 地址。'

html = urllib2.urlopen(url) # 打开网页
html.read() # 读取网页

# 但也可以先： 
req = urllib2.Request(‘url’)
# 再 
urllib2.urlopen(req) 
# 这样打开请求，这是推荐的使用方法。




'对于动态网页（比如登录界面），需要传送数据给它。'

数据传送分为 POST 与 GET：
GET 直接以链接的形式访问（不够安全），而 POST 则不会在网址上显示所有的参数。


<div class="embed-play-button" data-play-pause-button="1" data-player-src="http://audioboom.com/boos/2975604-03-star-wars-blaster-pistol.mp3">



