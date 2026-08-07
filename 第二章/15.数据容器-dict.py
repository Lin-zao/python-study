# #字典 --key不能重复(如果重复,后面的值会覆盖前面的值),key必须得是不可变类型(str,tuple,int,float)
# #定义字典
# dict1 = {"林子豪":720,"利姆湾":710}
# print(dict1)
# print(type(dict1))
#
# #key必须得是不可变类型(str,tuple,int,float),不能是list,set,dict
# dict2 = {"林子豪":720,"利姆湾":710,0:1,2:3,(70,80):29}
# print(dict2)
#
# #访问
# print(dict1["林子豪"]) #获取值
# dict1["林子豪"] = 688
# print(dict1)

# ---------------------------------------- 字典 常见操作 ---------------------------------------
dict1 = {"王林":670, "李慕婉":608, "许立国":580, "韩立":688}
print(dict1)

# 添加 - key不存在就是添加
dict1["涛哥"] = 550
print(dict1)

# 修改 - key存在就是修改
dict1["涛哥"] = 620
print(dict1)

# 查询
print(dict1["涛哥"]) # 根据key获取value
print(dict1.get("涛哥")) # 根据key获取value

print(dict1.keys()) # 获取所有的key
print(dict1.values()) # 获取所有的value
print(dict1.items()) # 获取所有的键值对 key:value

# 删除
score = dict1.pop("许立国")
print(score)
print(dict1)

del dict1["韩立"]
print(dict1)


# 遍历
for k in dict1.keys():
    print(f"{k} : {dict1[k]}")

for item in dict1.items():
    print(f"{item[0]} : {item[1]}")

for k,v in dict1.items():
    print(f"{k} : {v}")

