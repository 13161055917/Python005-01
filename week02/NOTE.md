一、 TCP/IP协议与SOCKET编程的关系

​                               ![image-20201204192043900](C:\Users\jxncl\AppData\Roaming\Typora\typora-user-images\image-20201204192043900.png)

在网络当中每一个部分都是分层排布的。

物理层主要是去解决物理连接的事情的

数据链路层是去处理怎么连接在一起的

网络层是去处理网络互通的问题

应用层，最著名HTTP协议

打开网页非常缓慢，就要去传输层和网络层去找原因

TCP/IP模型也叫做TCP/IP协议簇 是一组协议

 

做客户端的时候基本上是应用层，

 ![image-20201204192108320](C:\Users\jxncl\AppData\Roaming\Typora\typora-user-images\image-20201204192108320.png)

Socket通信模型  

TCP/IP真正通讯时的过程

 ![image-20201204192121658](C:\Users\jxncl\AppData\Roaming\Typora\typora-user-images\image-20201204192121658.png)

Bind()是绑定指定端口，这样应用程序和关联端口之间建立一个关联关系

Listen()端口状态进入监听状态

Accept()可以接受用户请求

Socket()绑定对应的套接字

Connect()发起连接 这里就是tcp协议的三次握手

Close()可以关闭

Socet API 

Socket()

Bind()

Listen()

Accept()

Recv()

Send()

Close()

实战：不适用开源框架的前提下完成一个ECHO服务端和ECHO客户端

 

二、写一个socket客户端

三、Echo Server实战

Echo就是回显 就是所我客户端发送什么样的字符给服务端  服务端就会鸳鸯的发回给你的客户端

这时为了证明客户端和服务端TCP层面的连接时畅通的 

Ping是为了检查网络链路是否通 也可能会被防火墙阻拦 返回pang

 

四、WEB开发必备前端基础

 ![image-20201204192133245](C:\Users\jxncl\AppData\Roaming\Typora\typora-user-images\image-20201204192133245.png)

F12去查看源代码  左上角还有指针可以快速找到代码相对应的效果。

 

五、HTTP协议和浏览器的关系

继续看四中的图

写爬虫就是用编程模拟浏览器

除了浏览器接收的内容 也传输了一些其他的信息

调试界面选择network

Headers 是传输的头部信息

Request url 地址连接

Status code ：状态码 观察能否返回内容

1xx 信息响应

2xx 成功响应

3xx 重定向

4xx 客户端响应

5xx 服务端响应

 

Request method: 请求方式 get

一般用于请求网页内容

传输数据的时候就是post方式

一般用于用户和密码登录

当使用cookies时  就说明带着用户名和密码的信息向网页发起请求了

User-Agent 告诉你的服务器 使用什么浏览器的形式

这里会有反爬虫的设置。

 

文字一般时放在span标签里，连接一般是a标签里 图片一般是img标签

 

六、request库入门实战

1、提出需求

获取《豆瓣电影 Top 250》的内容

https://movie.douban.com/top250?start=0

要求：

获取电影名称、上映日期、评分

写入文本文件

2、编码

3、代码run起来

4、修复和完善

 

七、异常捕获处理

open with open 增加健壮性

异常捕获  也是增加健壮性

 

异常捕获

参考 https://docs.python.org/zh-cn/3.6/libary/exceptions.html

所有内置的非系统退出的异常都派生自exception类

 

Stoplteration 异常示例：

Gennuber = (I for I in range(0, 2))

Print(next(gennumber))

Print(next(gennumber))

Try:

Print(next(gennumber))

Except StopIteration:

Print(‘最后一个元素’)

 

异常处理机制的原理

异常也是一个类

异常捕获过程：

1、异常类把错误消息打包到一个对象

2、然后该对象会自动查找到调用栈

3、直到运行系统找到明确声明如何处理这些类异常的位置

 

所有异常继承自 BaseException

Traceback 显示了出错的位置，显示的顺序和异常信息对象传播的放行是相反的

 

八、重构：增加程序的健壮性

可以去看request库的网站文档

 

九、深入了解HTTP协议

主要是要实现爬虫的功能  后期的web开发也是需要的。

用requests实现比较复杂的爬虫

 

Import requests

r = requests.get(‘http://www.httpbin.org’)

r

r.text

r.url

payload = {‘key1’: ‘value, ‘key2’:[‘value2’, ‘value3’]’}

r = requests.get(‘http://www.httpbin.org’, params = payload)

r.url

头部重点：

1、cookie

2、HOST 主机名

3、referer 从哪一个页面转过来的

4、user-agent 浏览器的版本

 

十、深入了解POST方式和cookie

 

十一、使用Xpath匹配网页内容&实现翻页功能

 

十二、使用自顶向下的设计思维拆分项目代码

什么是自顶向下设计？

1、从整体分析一个比较复杂的大问题

2、分析方法可以重用

3、拆分到你能解决的范畴

实战讲爬虫代码超杰模拟Scrapy 框架

​    1、什么是Scrapy?

2、为什么要模拟Scrapy?

初期图

 ![image-20201204192148478](C:\Users\jxncl\AppData\Roaming\Typora\typora-user-images\image-20201204192148478.png)

目前图

 ![image-20201204192157238](C:\Users\jxncl\AppData\Roaming\Typora\typora-user-images\image-20201204192157238.png)

1、引擎是多线程 并发去向网站发起请求

2、如果一个请求被发起 提前处理加headers的处理 叫spiders，scrapy中的spiders处理更加多的功能，把爬虫的概念实例化

3、先发起后发起，更科学地发起请求 就需要用调度器scheduler

4、下载器download调用网页下载功能。相当于requests发起请求

5、保存文件用open 文字数字要数据库 图片要图床存储 下载地部分叫做广告 item pipelins包括保存

 

十三、 模拟Scrapy拆分爬虫框架