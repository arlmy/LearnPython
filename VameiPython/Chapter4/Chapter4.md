class Bird(object)
	def chirp(self, sound)

对象.属性（object.attribute）
self 必须是第一个参数，相当于 JS 的 this
下属 def 即定义方法

魔法方法（Magic Method）：__init__ ，class 创建的时候自动执行

super().chirp()
super 可调用父类中被覆盖的源方法

dir(list)
help(list)
对自带的类，可以通过这两个函数调用说明文档

pass 
什么都不做，以保持语法结构的完整性

help(list.append)
list 中 append 方法的帮助文档

字符串是特殊的元组

example_iter = iter([1,2])
example_iter.__next__()
利用 iter() 和 __next__() 将列表转换为循环对象
如：
for item in iter([1,2,3]): （for 结构自动调用 __next__() ）
	print(item)

生成器 generator 来自定义循环对象
return 的地方改为 yield，遇到 yield 时暂停生成
(相当于 alert)

from time import *
from time import sleep 
sleep(10) 延迟十秒