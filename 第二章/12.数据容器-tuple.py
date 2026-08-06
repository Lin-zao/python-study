#元组基本操作-tuple--->元素可以重复,有序,不可更改
#定义
t1 = (80,96,64,48,33,32,12)

print(t1)
print(type(t1))

print(t1[0:5])

s = t1.count(33)
print(s)

print(t1.index(80))
from calendar import firstweekday

from pandas.compat.numpy.function import validate_groupby_func

#------------- 元组tuple 组包与解包
#组包操作
t1 = (5,4,7,5,33,6,8,854)
t2 = 5,4,7,5,33,6,8,854

print(t1)
print(t2)

#解包操作
#基础解包操作(保证变量的数量与容器的元素个数一致)
a,b,c,d,e,f,g,h = t1
print(a,b,c,d,e,f,g,h)

#*  扩展解包 (*收集剩余的所有元素,封装列表list中)
first,second,*other,last = t1
print(first)
print(second)
print(other)
print(last)

