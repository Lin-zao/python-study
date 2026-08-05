#字面量的写法
print(100)#整数(int)
print(3.14)#浮点数/小数(float)
print(True)#布尔类型(bool)
print(False)#布尔类型(bool)
print("Hello Python")#字符串(str)
print("----------")#字符串(str)
print(None)#空值(None Type)

#布尔类型本质也是整数类型(True -- 1,False --0)
print(True + 1)#2
print(False - 1)#-1


#变量
num = 1114.1
print(num)

num =  num + 1
print(num)

num = "OK"
print(num)

num = True
print(num)


#案例
#基础播放量
base = 20.7
#每月新增播放量
increase = 50
#输出未来两个月每个月的播放量
print("未来第一个月的播放量:",base + increase)
print("未来第二个月的播放量:",base + increase + increase)


#案例 -- 升级:一次性可以定义多个变量
base,increase = 20.7,50
print("未来第一个月的播放量:",base + increase)
print("未来第二个月的播放量:",base + increase + increase)



