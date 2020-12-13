学习笔记

一、MYSQL安装

企业级MYSQL 部署在Linux操作系统上，需要注意的重点：

1、注意操作系统平台（32位，64位）

2、注意安装MYSQL的版本（MYSQL企业版、社区版、MariaDB）

3、注意安装后避免yum自动更新

4、注意数据库的安全性。比较复杂的密码，访问用户、访问权限等

Ssh root@server1 #连接一个远程的Linux服务器

Arch #查看多少位的操作系统

Cat/etc.redhat-release #查看系统版本

Ls-lh 把包都下载完整

Yum install mysql57- community -release-el7-10.noarch.rpm

Yum install mysql-community-server

从网络当中找到这些包

能够用网络不断更新mysql的社区版

Yum install *.rpm #下载包到本地后的安装

Yum update #更新

\#当出现开发环境和生产环境的数据库版本不兼容的时候，就要把新版版移除掉

Yum remove mysql57-community-release-el7-10.nnarch

Systemctl start mysqld.service

Systemctl enable mysqld

Systemctl statuws mysqld.service

Rpm -qa l grep -I ‘mysql’  #查看版本

Grep ‘password’ /var/log/mysqld/log | head -1

Mysql -u root -p #临时生成的密码

ALTER USER ‘root’@’localhost’ IDENTIFIED BY ‘new_password’

\# 密码入宫设置过于简单 会报错。

SHOW VARIABLES LIKE ‘validate_password%’

\# 查看密码的设置。

Set global validate_password_policy=0

修改密码复杂度

 

二、正确使用MYSQL字符集

经常会设置和调整MYSQL 为了让他能跑在不同配置的服务器上。

查看字符集：

Mysql> show variables like ‘%character%’;

查看校队规则

Mysql> show variables like ‘collation_%’

注意：mysql 中的utf8不是 utf-8 字符集

show variables like ‘%character%’;

vim/rtc/my.cnf #mysql的配置文件，默认在etc下面

字符集：就是多个字符的集合  可以是英文可以是汉字。可以实其他的字符，也可以是emoji表情 不同的字符集会占用不同的位数

客户端：

ASCII 罗马字符集 

LATIN

GBK 4个字节

UTF-8 4个字节

UTF8 最多只能占3个字节

服务端

根据DBA设置合理的值

需要去做压力测试的时候 就要改大连接数。

Character_set_server = utf8mb4 默认内部操作字符集

Init_connection = ‘set names utf8mb4’ 在客户端进行连接的时候在里面使用的。

需要保存退出

Systemctl status mysqld  #重启数据库

Create database db1 # 创建数据库

 

保证字符集的统一问题

校对规则

_ci _cs 能够区分大小写

 

三、多种方式连接MYSQL数据库

Python连接mysql的方法

统一概念：

其他语言：连接器、绑定、binding

Python语言：python database API  、DB-API

主语：mysqldb是python2的包，适用于mysql5.5和python2.7

 

Python连接mysql:

Python3安装的mysqldb包叫做mysqlclient，加载的依然是mysqldb

Shell> pip install mysqlclient

Python> import mysqldb

其他DB-API:

Shell> pip install pymysql #流行度最高

Shell> pip install mysql-connector-python # mysql官方

Python连接时建议使用ORM：

Shell> pip install sqlalchemy

 

回到mysql当中

Use testdb

Show tables

Show create table book ;

Show create table author ;

 

再次回到mysql里面

Show table ;

Show create table authororm;

四、必要的SQL知识

SQL语言功能划分：

DQL：Data Query Language, 数据查询语言，开发工程师学习的重点。

DDL：Data Definition Language, 数据定义语言，操作库和表结构。

DML：Data Manipulation Language, 数据操作语言，操作表中记录。

DCL：Data Control Language, 数据控制语言， 安全和访问权限控制。

 

那些你需要精通的SQL知识

创建表要注意哪些问题？

CREATE TABLE ‘book’(

‘book_id’ int(11) NOT NULL AUTO_INCREMENT,

‘book_name’ varchar(255),

PRIMARY KEY (‘book_id’)

) ENGINE = innoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci;

建议一、

创建数据表的个数其实是越少越好

建议二、

表中的字段也是越少越好 尽量少 相互独立

建议三、

表的联合主键的字段也是越少越好。

建议四、

要不要有外键  对内部的系统压力不高重点关注数据的正确性 用外键

如果是对外的  外键要在应用层来解决。要不会在跟新时阻塞

 

查询数据要注意哪些问题？

SELECT查询时关键字的顺序

SELECT ...FROM…WHERE…GROUP BY…HAVING…ORDER BY…LIMIT

注意： 1.生产环境下因为列数相对较多，一般禁用SELECT*

2、WHERE字段为避免全表扫描，一般需要增加索引

 

五、 使用聚合函数汇总数据

SQL 函数有哪些？

算术函数、字符串函数、日期函数、转换函数、聚合函数

聚合函数

COUNT()   行数

MAX()    最大值

MIN()    最小值

SUM()    求和

AVG()    平均值

注意： 聚合函数忽略空行

打开mysql

Show databases;

Use db1

Show tables;

Select * from t1 limit 5 \G

 

SELECT COUNT(*) FROM t1 ;

SELECT COUNT(*) , AVG(n_star), MAX(n_star) FROM t1 WHERE id < 10;

SELECT COUNT(*) , n_star FROM t1 GROUP BY n_star;

SELECT COUNT(*) ,n_star FROM t1 GROUP BY n_star HAVING n_star > 3 ORDER BY n_star DESC ;

 

六、多表操作用到的子查询和join关键字解析 

什么是子查询？

需要从查询及过集中再次进行查询，才能得到想要的结果

嵌套代码

子查询需要关注的问题？

关联子查询与非关联子查询区别。

非关联子查询相对比较简单

何时使用IN，何时使用EXISTS

进入mysql

SELECT COUNT(*), n_star FROM t1 GROUP BY n_star HAVING n_star > 3 ORDER BY n_star DESC;

SELECT avg(n_star) from t1;;

Select count(*), n_star FROM GROUP BY n_star HAVING n_star > (SELECT avg(n_star) from t1 ) ORDER BY n_star DESC; #非关联子查询

EXIST IN 

TABLE A TABLE B \c

SELECT * FROM TABLE_A WHERE condition IN (SELECT condition FROM TABLE_B) \c

SELECT * FROM TABLE_A WHERE EXIST (SELCT condition FROM B WHERE B.condition=A.condition) \c

当B小于A的时候 应该用IN 当A小于B的时候 用exist 

For I in TABLE_B;

   For j in TABLE_A:

​      If TABLE_B.condition == TABLE_A.condition;

转换成python的操作

 

常见的连接（JOIN）有哪些？

自然连接

ON连接

USING连接

外连接

 左外连接

  右外连接

  全外连接（MYSQL 不支持）

​                               

 ![image-20201211211235507](C:\Users\jxncl\AppData\Roaming\Typora\typora-user-images\image-20201211211235507.png)

七、事务的特性和隔离级别

什么是事务？

要么全执行，要么不执行

事务的特性—ACID

A  原子性（Atomicity）

C  一致性 （Consistency）

I  隔离性（Isolation）

D  持久性（Durability）

事务的隔离级别—用来保证事务的特性

读未提交： 允许读到未提交的数据

读已提交： 只能读到已经提交的内容

可重复读： 同一事物在相同查询条件下两次查询得到的数据结果一致

可串行化：事务进行串行化，但是牺牲了并发性能。

进入mysql

Show varables like ‘autocommit’;

Set autocommit=0;

Show varables like ‘autocommit’; # 这时已经关闭了自动提交

BEGIN COMMIT ROLLBACK TO # 开启自动提交 回滚

 

八、pymysql的增删改查操作演示

进入mysql

Desc book

Select * from book;

 

回到mysql

大部分的代码时不需要改变的 需要改变的就是占位符 都是通过外部的应用程序

 

九、多文件插入&如何设计一个良好的数据库连接配置文件

 

十、 使用SQLAlchemy插入数据到MySQL数据库

使用orm 工作中需要大量的迭代

十一、 使用SQLAlchemy查询MySQL（上）

进入mysql

Select * from bookworm;

 

十二、 使用SQLALchemy查询MySQL(下)

 

十三、使用SQLAlchemy更新和删除MySQL

进入MYSQL

Select * from bookworm;

ID19 已经删除

 

十四、使用连接池优化&数据库建立连接的过程

数据库打开文件的时候 会受到操作系统限制。

 

十五、优化数据库使用的基本原则

如何对数据库做调优

调优的原则：

调优不是万能的，升级硬件往往比调优效果更明显

调优的效果会随着次数增加，逐渐递减

应该有体系的调整，而不是发现一个参数可以改动就试试

 

Cpu是需要程序尽快的去响应，能一次性处理大量的数据

内存是尽快的去刷磁盘，把数据保存在磁盘当中，保证数据安全。

网络希望吞吐率更大，把数据包切成更小的块去相应。

 

调优是出现瓶颈然后去调优

可以从网络中去下载阿里巴巴Java开发手册 建表的规则

优化的前提是把平衡状态调整到适合自己业务的状态。（增加大量的监控系统，找到瓶颈后，在去更改。）