import time

print(time.time())

st1 = time.gmtime() # UTC 时间

print(st1)

st2 = time.localtime() # 根据系统环境返回当地时间

print(st2)

ti = time.mktime(st2)

print(ti)