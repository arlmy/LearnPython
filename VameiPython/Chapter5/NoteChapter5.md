## 文件操作

f.open("test.txt","r")
"r"读取
"w"新建并写
"a"如文件存在则写入结尾，如不存在则新建+写入

方法：read(), readline(), readlines()

f.close()
记得关闭文件，否则占用计算机资源

## 上下文管理(context manager)：

with open("new.text", "w") as f:
	f.write("Hello World!")
print(f.closed)

[写文件模式详解](http://www.cnblogs.com/dkblog/archive/2011/02/24/1980651.html)

wb 二进制写，生成
rb 二进制读，解析

dump 和 dumps 的唯一区别是 dump 会生成一个类文件对象，dumps 会生成字符串
同理，load 和 loads 分别解析类文件对象和字符串格式

dump load 类文件
dumps loads 字符串

[Python & JSON](http://www.hulufei.com/post/201004161735)

with ... as ...
	程序块
程序块执行结束的时候，会自动关闭文件

## pickle 包

pickle 包储存方法
import pickle
pickle.dumps() 序列化对象（转换成字符串的形式）

pickle.loads()
可以将文本转化为对象

## time 包

import time

time.time()
time.clock()
time.struct_time 将挂钟时间格式化：tm_year, tm_mon, tm_mday, tm_hour ...

t = datetime.datetime(2012,9,3,21,30)
hour, minute, second, millisecond 毫秒, microsecond 微秒
year, month, day, weekday

%Y 年 %m 月 %d 日
%H 24小时制小时 %M 分 %S 秒
%I 12小时制小时
%A 英文星期 %a 英文简写星期 
%p 上午/下午
%f 毫秒

[datetime 官方文档](https://docs.python.org/3/library/datetime.html#datetime.timedelta)

## 正则表达式（regular expression）

从字符串中通过特定的模式，搜索希望找到的内容。

```import re```

*需要专门学习一下*

## 爬虫
