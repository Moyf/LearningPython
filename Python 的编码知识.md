<h2>关于字符串的基础知识</h2>str 是<b><i>字节串</i></b>，由 Unicode 经过编码（encode）的字节组成；<div>Unicode 才是真正的字符串，由字符组成，直接输出会显示成&nbsp;<u>’\xe4’</u>&nbsp;这样的形式；</div><div><br></div><div>如果在字符串前面加 u，像是： <u>u’中文'</u></div>那么它会被识别为 Unicode 字符串（类型是 <i>unicode</i>），无法直接 Print，而是会提示 [UnicodeEncodeError: 'ascii' codec can't encode characters in position 0-1: ordinal not in range(128)] ，需要人工在它后面加上 <u>.encode(‘utf-8’)</u> 才行——那样的话就会编码为&nbsp;<u>str</u> 类型；<div><br></div><div>str 类型的数据如果直接按原样输出（使用 %r ）会显示为 ’/xe4’ ，但是作为字符串输出则会正常显示；</div><div><br></div><div>str 类型通过解码会变成 unicode 类型；</div><div>unicode 类型通过编码可以变为 str 类型；</div><div><br></div><div>在文件处理的时候，一般在入口全部转为 unicode，然后在转出的时候再转为想要的编码。</div><div>即，将 unicode 作为中转站。</div><div><br></div><div><br></div><div>现在的难点问题就在于，List 中的中文字符在输出时，会显示成utf-8的编码，即 /xe5 这样的形式。</div><div>这个玩意儿其实就是16进制的 UTF编码。</div><div><br></div><div>而它虽然没办法用 print 正常显示（好吧，也有办法），但输出文件的时候是正确的中文汉字。</div><div>要解决也成，你每个对象（字符串）单独输出，即：</div><div><br></div><div><div>for e in lineList:</div><div><span class="Apple-tab-span" style="white-space:pre">	</span>print e</div></div><div><br></div>
<h1>关于字符编码的知识</h1><div>ASCII 码将英语字符与二进制位一一对应，用一个字节表示一个字符，一共有128个字符，本质是二进制/数字。</div><div>每个字节(byte)都是8个二进制位，1 byte = 8 bit，共256个状态。</div><div><br></div><div>中文常用编码方式是 GB2312， 用两个字节(16 bit)表示一个字符；它与 UTF-8 / Unicode 毫无关系。</div><div><br></div><div>Unicode 是为了统一世界上各种编码而诞生的，是一个非常大的集合。</div><div>它只是一个符号集，规定[某个符号的二进制代码]，相当于一个映射表，但没有确定的储存方式，所以有多种二进制格式；另外，它很耗内存。</div><div><br></div><div>UTF-8 是 Unicode 的一种<b>实现方式</b>。</div><div>它的特点是可变长编码，可以用1~4个字节来表示字符。</div><div>而且对于英文字母，与 ASCII 表示方法相同；</div><div><br></div><div>举个例子，汉字”严“的 Unicode 是 4E25&nbsp;（100111000100101），根据推算可以得到 UTF-8 编码是&nbsp;"11100100 10111000 10100101”，转为16进制即 E4B8A5。</div><div>总结来说，Unicode 是映射表，用字节表示字符，而 UTF-8 是具体的储存格式。</div><div><br></div><div><br></div>
<h1>文件读写的知识</h1><div>一定要先有一个<u>文件对象</u>才能对它进行相应的读写操作。</div><div><br></div><div>open (“file”, type)</div><div>type 主要类型如下：</div><div><ul><li>r 只读方式打开（默认模式）</li><li>r+ 用于读写，<span style="font-family: 'Open Sans', 'Helvetica Neue', Helvetica, Arial, STHeiti, 'Microsoft Yahei', sans-serif; font-size: 12px; line-height: normal; widows: 1; background-color: rgb(255, 255, 255);">文件指针将会放在文件的开头。</span></li><li>w 纯写入，如果已经存在的话会覆盖</li><li>w+ 用于读写，如果已经存在的话会覆盖</li><li>a 追加内容，新的内容会写在原文之后</li><li><span style="line-height: 1.4;">a+ 用于读写，新的内容会写在原文之后&nbsp;</span><br></li></ul><div>另一种解释：</div></div><div><pre class="prettyprint lang-bsh" style="box-sizing: inherit; border-width: 0px 0px 0px 3px; border-left-style: solid; border-left-color: rgb(204, 204, 204); margin-top: 1em; margin-bottom: 1em; padding: 0.5em; overflow: auto; word-wrap: normal; line-height: 1.55; widows: 1; background-color: rgb(240, 240, 240);"><font face="Monaco"><span class="pln" style="box-sizing: inherit; color: rgb(0, 0, 0);">r</span><span class="pun" style="box-sizing: inherit; color: rgb(102, 102, 0);">或</span><span class="pln" style="box-sizing: inherit; color: rgb(0, 0, 0);">rt  </span><span class="pun" style="box-sizing: inherit; color: rgb(102, 102, 0);">默认模式，文本模式读</span><span class="pln" style="box-sizing: inherit; color: rgb(0, 0, 0);">
rb     </span><span class="pun" style="box-sizing: inherit; color: rgb(102, 102, 0);">二进制文件</span><span class="pln" style="box-sizing: inherit; color: rgb(0, 0, 0);">
 
w</span><span class="pun" style="box-sizing: inherit; color: rgb(102, 102, 0);">或</span><span class="pln" style="box-sizing: inherit; color: rgb(0, 0, 0);">wt </span><span class="pun" style="box-sizing: inherit; color: rgb(102, 102, 0);">文本模式写，打开前文件存储被清空</span><span class="pln" style="box-sizing: inherit; color: rgb(0, 0, 0);">
wb    </span><span class="pun" style="box-sizing: inherit; color: rgb(102, 102, 0);">二进制写，文件存储同样被清空</span><span class="pln" style="box-sizing: inherit; color: rgb(0, 0, 0);">
 
a   </span><span class="pun" style="box-sizing: inherit; color: rgb(102, 102, 0);">追加模式，只能写在文件末尾</span><span class="pln" style="box-sizing: inherit; color: rgb(0, 0, 0);">
a</span><span class="pun" style="box-sizing: inherit; color: rgb(102, 102, 0);">+</span><span class="pln" style="box-sizing: inherit; color: rgb(0, 0, 0);">  </span><span class="pun" style="box-sizing: inherit; color: rgb(102, 102, 0);">可读写模式，写只能写在文件末尾</span><span class="pln" style="box-sizing: inherit; color: rgb(0, 0, 0);">
 
w</span><span class="pun" style="box-sizing: inherit; color: rgb(102, 102, 0);">+</span><span class="pln" style="box-sizing: inherit; color: rgb(0, 0, 0);"> </span><span class="pun" style="box-sizing: inherit; color: rgb(102, 102, 0);">可读写，与</span><span class="pln" style="box-sizing: inherit; color: rgb(0, 0, 0);">a</span><span class="pun" style="box-sizing: inherit; color: rgb(102, 102, 0);">+的区别是要清空文件内容</span><span class="pln" style="box-sizing: inherit; color: rgb(0, 0, 0);">
r</span><span class="pun" style="box-sizing: inherit; color: rgb(102, 102, 0);">+</span><span class="pln" style="box-sizing: inherit; color: rgb(0, 0, 0);"> </span><span class="pun" style="box-sizing: inherit; color: rgb(102, 102, 0);">可读写，与</span><span class="pln" style="box-sizing: inherit; color: rgb(0, 0, 0);">a</span><span class="pun" style="box-sizing: inherit; color: rgb(102, 102, 0);">+的区别是可以写到文件任何位置</span></font></pre></div><div>用 r 的时候，文件必须存在，否则报错；w 和 a 可以自动新建文件夹；</div><div><br></div><div><br></div><div>几个属性：</div><div><ul><li>file.closed 是否已被关闭</li><li>file.mode 文件的访问模式</li><li>file.name 文件的名称</li><li>file.softspace 用 print 输出后是否必须跟一个空格符</li></ul><div><br></div></div><div>几个方法：</div><div><ul><li>fileObject.close() 关闭文件，随后不能再写入</li><li>fileObject.wrtie(string) 写入文件，不回在字符串的结尾加换行符</li><li>fileObject.read() 读取文件</li><li>fileObject.tell() 获取当前在文件内的位置，下一次读写会在这么多字节之后<br></li><li>fileObject.seek(offset [,from]) 设定指针的位置，将作为开始读写的参考值；from 的值如下：<br></li><ul><li>0 开头</li><li>1 当前位置</li><li>2 末尾</li></ul></ul><div><br></div></div><div>参考资料：<a href="http://www.runoob.com/python/python-files-io.html" style="line-height: 1.4;">http://www.runoob.com/python/python-files-io.html</a></div><div><br></div><div><br></div><div><br></div>
<h1>时间的知识</h1><div>首先，导入时间库：</div><div>`import time`</div><div><br></div><div>然后，time.time() 表示从公元 1970 年到现在经过的<u>秒数</u>（浮点数）</div><div>用 time.localtime(sec) 可以将上述秒数转为本地的时间，无参数则自动转化当前的时间；</div><div>再用 time.asctime(timeObject) 可以把它作为格式化的字符串输出</div><div><br></div><div>想要格式化的话可以自己手动提取元组：

```
序号	属性	值
0	tm_year	2008
1	tm_mon	1 到 12
2	tm_mday	1 到 31
3	tm_hour	0 到 23
4	tm_min	0 到 59
5	tm_sec	0 到 61 (60或61 是闰秒)
6	tm_wday	0到6 (0是周一)
7	tm_yday	1 到 366(儒略历)
8	tm_isdst	-1, 0, 1, -1是决定是否为夏令时的旗帜
```


Tip：<div>如果在源代码中出现了中文，那么在开头必须声明字符集</div>





```
#!/usr/bin/python
# -*- coding: utf-8 -*-
```

一般用格式化输出来使用 print， 而非一次次地转换格式，像这样：
print '%s -  %s, len = %d' % (type(s), s, len(s))

另外，Python 会自动在行尾加上回车，不过不想加回车可以在 print 参数的末尾加上","（英文逗号），像这样：
print '%s -  %s, len = %d' % (type(s), s, len(s)),
