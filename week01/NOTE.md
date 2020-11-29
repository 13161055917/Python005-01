学习笔记

一、如何正确区分python的版本

 

1、关于python解释器版本的选择，

  区分不同python版本差异

Python2，一般用2.7版本

Python3，一般用3.7和3.8

两个不完全兼容

  了解不同版本的python特性

 

专业人士需要去细节了解python不同版本的变化，因为有会向后不兼容

从docs.python.org中去了解

工作中都在用哪个把版本，一般是python3.7

官方文档：https://docs.python.org/zh-cn/3.7/whatsnew/3.7.html

 

安装包的版本差异

http://www.python.org/downloads/

还有哪些差异需要关注

1、操作系统平台差异

2、操作系统32位和64位差异

 

二、在不同的操作系统中安装python

macOS环境下的安装

1、正确安装python

2、交互模式的使用

3、了解常用IDE

 

Python3.7和python3.8安装实战

注意

1、安装目录不要有中文、空格、特殊字符

2、非必要情况尽可能只安装一个python解释器

3、安装了多个版本的python需注意PATH环境变量的配置

强烈建议官网下载，因为怕有插件和木马

 

三、多个python解释器共存会有什么问题？

\>>>是python的交互解释器

1、当系统中安装了多个python版本的时候 当输入python时 运行脚本文件很难去区分版本

2、按两次tab可以补全显示

3、python3 -v 可以直到当前运行的版本

4、更改路径可以指定运行python版本，$PATH（环境变量） 搜索可以找到目录（这里需要掌握linux命令）

5、调换运行版本的顺序：

echo $PATH #查看

export PATH=python3.7路径:$PATH #调整顺序

sudo vim /etc/profile  #管理员编辑配置文件

进入vim 之后 添加 export PATH=python3.7路径:$PATH #调整顺序

\# 这里需要vim 的控制命令 

保存

Pip 也会存在多个版本的问题 

Ls site-packages 是第三方库的安装目录

Pip3.7 才是给3.7安装  pip3.8 才是给3.8安装

 

四、PEPL初体验与pip使用技巧

Python和pip命令：

1、python命令：python的解释器，官方采用CPython版本

2、pip命令：方便安装第三方库

 

PEPL(交互解释器)

1、python程序可以交互执行也可以采用文件形式加载执行

2、Ipython可以扩展python的交互功能

Pyhton3.7

\>>>Str1 = “hello,pyhton!”

\>>>print(str1)

Hello,python!

\>>>str1.upper()

‘HELLO,PYHTON!’

\>>> 

\>>>type(str1)

<class ‘str’>

\>>>help(str1)

\#显示帮助内容

\#这里无法进行自动补全

\>>>exit()

 

Pip install ipython #需要安装 要观察是安装到哪个版本中

Ipyton #进入并可以编辑

Str1 = ‘hello,python’

Str1.upper()

Help #ipython可以进行补全

exit()

 

如果安装比较慢的时候 有可能是国外的软件源

国内常见的镜像站：

1、豆瓣：http://pypi.doubanio.com/simple/

2、清华：https://mirrors.tuna.tsinghua.edu.cn/help/pypi/

升级pip:

1、方法一：

Pip install -I https://pypi.tuna.ysinghua.edu.cn/simple pip-U

2、方法二：

Pip config set global.index-url http://pypi.doubanio.com/simple/

Pip install pip -U

 

Pip安装加速

Windows: c:\User\xxx\pip\pip.ini

Linux: ~/.pip/pip.conf

配置文件格式：

【global】

Index-url = https://pypi.tuna.tsinghua.edu.cn/simple

 

\#进入终端

Cd ~

Mkdir -p .pip

Cd .pip

Ls

Cat pip.conf #查看设置

 

五、python IDE的使用技巧

中型的项目就会用到IDE工具

 

Python常用的IDE

Visual studio code

1、visual studio code 的安装

2、visual studio code 常用的快捷键演示

需要安装扩展 

Option（AIT） shift加F 调整代码格式

Command(,键)+上 快速移动到开头

F5调试运行 F11单步调试

3、使用visual studio code 和print 函数调试一个有BUG的python程序

 

其他常用ide

1、pycharm

安装、调试

2、jupyter notebook

安装、调试

 

六、python项目的一般开发流程及虚拟环境配置

一般开发流程

1、高清需求

2、编写源代码

3、使用python解释器转换为目标代码

4、运行程序

5、测试

开发环境中没有问题 需要牵引到生产环境。

引入虚拟环境

6、修复错误

7、再运行、测试

8、………

 

迁移部署

虚拟环境的用途和使用方法

如何正确使用官方文档

注意：

1、在生产环境中虚拟环境是保持一致性的必备工具

2、开发环境中可以不配置虚拟环境

\#进入终端

Vim a.py

Ls

Python a.py

Python a.py 第三方库 都要保持一致的环境

Python3 -m venv venv1 #python3在执行的时候venv 并创建venv1虚拟环境

 

Source venv1/bin/activate #激活虚拟环境

Deactivate #回到原始环境

Pip3 freeze > requirements.txt 第三方库的安装文件

Cat requirements.txt 

\#把第一个虚拟环境的三方库安装到第二个虚拟环境

Deactivate

Source venv2/bin/activate

Pip3 -v

Python3 -v

Which python3

Pip3 freeza 

Pip install -r ./ requirements.txt #安装

Pip3 freeza# 查看

 

七、python的基本数据类型

None 空对象

Bool  布尔值

数列  整数、浮点数、复数

序列  字符串、列表、元组

集合  字典 （哈希方式）

可调用 函数

“xxx” ‘xxx’ ‘’’xxx’’’

\#字符串常用方法 要去看下 提升熟练程度

【】列表

\#列表的常用方法

()元组

\#元组常用方法

{}字典

\#字典的常用方法

 

八、python的高级数据类型

Collections    容器数据类型

Nametuple()   命名元组

Deque      双端队列

Counter     计数器

Ordereddict    有顺序的字典

 

文档地址：

htttps://docs.python.org/zh-cn/3.7/library/collections.html

 

九、控制流

For主要用于迭代

条件判断 if elif else 

循环   while 

Len(list1) 查看长度

Pythonic python风格化的程序

 

十、函数和模块的区别

掌握常见python模块

函数、模块和包的区别是什么？

常见模块

1、time

2、datetime

3、logging

4、random

5、json

6、pathnlib

7、os.path

 

多个函数组成一个模块（.py文件） 多个模块组成包(特殊处理的文件夹)

自己定义模块：

Touch short.py

Touch main.py

Vim main.py

Import short

Short.Short._func()

If __name__ = ‘__main__’:

  Short_func()

防止调用的时候多次运行

 

十一、python标准库：日期时间处理

   Ipython

   Import time

​     Time.time() #时间戳

   Time.localtime() # 返回时间结构

   \# 当前时间

Time.strftime(‘%y-%k-%d %X’, time.localtime())

   \# 转成struct_time格式

Time.strptime(‘%y-%k-%d %X’, time.localtime())

\#时间偏移 用datetime

Import datetime

\#显示今天的日期时间

Datetime.datetime.today()

 

From datetime import *

Datetime.today()

Datetime.now()

 

\#昨天

Datetime.today() – timedelta(days = 1)

Datetime.today() + timedelta(days = -1)

 

 

十二、python标准库：日志处理

 

Logging模块的使用

工作中多数用来查问题 和解决BUG

Info级别 记录信息

Warning 级别  警告 单不会影响程序使用 

Error级别  需要关注和优化 例：用户在登录连接数据库失联

Critical 级别  严重的错误  程序崩溃了

Debug级别 调试

 

Import logging

Logging.debug(‘debug message’)

Logging.info(‘info message’)

Logging.warning(‘warning message’)

Longing.error(‘error message’)

Longing.critical(‘critical message’)

 

修改配置

Basicconfig

Filename 日志信息保存到哪一个文件

Level info以上记录日志 改这个

Datefmt 指定的日期和时间格式 time.strftime()格式相同 让python代码越用越简单

Format 使用的指定格式字符串

Logrecord属性  想要去记录哪些内容 要靠属性去写

Asctime 查看时间值

Lineno 行号

Levelname 

 

Demo1目录

Ipython

Import logging

Logging.basicConfig(filename=”test.log”)

Logging.debug(‘debug message’)

Logging.info(‘info message’)

Logging.warning(‘warning message’)

Longing.error(‘error message’)

Longing.critical(‘critical message’)

exit()

ls

 

import logging

logging.basicConfig(filename=’test.log’, level=logging.DEBUG, datefmt=’%Y-%m-%d %H:%M:%S’, format =’%(asctime)s %(name)-8s %(levelname)-8s [line:%(lineno)d] %(message)s’)

Logging.debug(‘debug message’)

Logging.info(‘info message’)

Logging.warning(‘warning message’)

Longing.error(‘error message’)

Longing.critical(‘critical message’)

exit()

 

十三、python标准库：路径处理

Random

From random import *

Random()

返回0.0-1.0的随机数  当前的时间戳实现的 

Randrange(0,101,2)

\# 0-100之间的偶数

Choice([‘red’, ‘blue’, ‘orange’])

Sample([1,2,3,4,5], k=4)

\#抽取多个

 

Import json

Json.load(‘[“foo”, {“bar”:[“baz”, null, 1.0, 2]}]’)

Json.dumps(“[‘foo’, {‘bar’:[‘baz’, null, 1.0, 2]}]”)

 

From pathlib import path

P = path()

p.resolv() #显示当前的完整路径

path = ‘/user/local/a.txt.py’

p = path(path)

常用的函数

p.name

p.stem #取出文件名

p.suffix #取出扩展名

双扩展名同样能处理

p.parent #返回路径

p.parents #返回可迭代对象 可以用for迭代

p.parts #取出路径名和文件名

 

os.path

import os

os.path.abspath(‘test.log’) #取出完整路径

path = ‘/user/local/a.txt’

os.path.basename(path) #获得文件名

os.path.dirname(path)# 获得路径

os.path.exists(‘/etc/passwd’)# 判断文件是否存在

os.path.isfile(‘/etc/passwd’) #判断文件是否文件

os.path.isdir(‘/etc/passwd’) #判断文件是否目录

os.path.join(‘a’,’b’)#结合路径 相对路径

os.path.join(‘/a’,’b’)# 结合路径 绝对路径

 

 

十四、python标准库：手动实现守护进程

Deamon进程 主要用于服务器端

第一用处 程序开机自动运行 没有终端的 

第二 在终端关闭的情况下  程序能继续运行

已经有一个标准了

PEP是标准和Python改进的思路

去看stack overflow 学写守护进程

APUE第十三章 守护进程

 

十五、python标准库：正则表达式实战

Re-正则表达式操作

需要去通读的文档

用户提交用户名 密码 用正则来进行验证

特殊字符需要全部掌握，而且要合理的组合

.*匹配任意字符和任意多次

$匹配什么什么结尾

+一次到任意次

模块内容

re.compile 

正则表达式对象

 

终端

Import re 

Content = “12332112312”

Re.match (“.{11}”, content)

Re.match(“.{11}”, content).group()

Re.match(“.{11}”, content).span()

Result = re.match(“.{11}”, content).group()

 

Re.match(“.*@.*”, “abc@123.com”).group()

Re.match(“(.*)@(.*)”, “abc@123.com”).group()

 

Re.search(“@”,”123@123.com”)

Re.findall(“123”, “123@123.com”)

Re.sub(“123”, “456”, “123@123.com”)

Re.sub(“\d”, “xyz”, “123@123.com”)

Re.sub(“\d+”, “abcxyz”, “123@123.com”)

Re.split(“(@)”, “123@123.com”)