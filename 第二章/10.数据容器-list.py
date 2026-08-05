# #列表操作
# #定义
# s = [56,60,70,"hello",True]
# print(type(s))
#
# #访问列表的元素
# #获取
# print(s[0])#正向索引,从0开始
# print(s[-5])#反向索引,从-1开始
#
# print(s[2])
# print(s[-3])
#
# #修改
# s[3] = "Hello python"
# print(s)
#
# #如果指定的索引超出范围,将会报错
# # s[7] = "2"
# # print(s)
#
# #删除
# del s[3]
# print(s)
#
# #遍历
# for item in s:
#     print(item, end=" ")
#
# #----------俩表list切片
# #定义列表
# s = ["A","B","C","D","E","F","G"]
#
# #切片操作 s[开始索引;结束索引;步长]
# print(s[0:5:1])
# print(type(s[0:5:1]))
# print(s[:5])
#
# print(s[0:5:2])
# print(s[0:-2])
#
#
# #---------------列表list常用方法
# #定义列表
# s = [59,78,6,5,44,455,45,65,4455,4]
# print(s)
#
# #append():在列表尾部追加元素
# s.append(188)
# print(s)
#
# #insert():在指定索引之前,插入元素
# s.insert(0,188)
# print(s)
#
# #remove():移除列表中第一个匹配的元素
# s.remove(188)
# print(s)
#
# #pop():删除列表中指定索引位置的元素并返回
# e = s.pop(1)
# print(e)
#
# e = s.pop()
# print(e)
#
# print(s)
#
#
# s.sort()
# print(s)
# s.reverse()
# print(s)


# #将用户输入的10个数字，存储到一个列表中，并将列表中的数字进行排序, 输出其中的最小值、最大值 和 平均值。
#
# #1.定义列表
# num_list = []
#
# #2.将用户输入的10个数字，存储到一个列表中
# for i in range(10):
#     num = int(input("请输入一个有效的数字:"))
#     num_list.append(num)
# print("列表为:",num_list)
#
# #3.排序
# num_list.sort()
# print("排序后的列表为:",num_list)
#
# #4.输出其中的最小值、最大值 和 平均值。
# print("最小值为:",min(num_list))
# print("最大值为:",max(num_list))
# print("平均值为:",sum(num_list)/len(num_list))

# #合并两个列表中的元素，并对合并的结果进行去重处理(去除列表中的重复元素)。
# # 定义列表
# num_list1 = [19, 23, 54, 64, 875, 20, 109, 232, 123, 54]
# num_list2 = [55, 80, 72, 35, 60, 123, 54, 29, 91]
# #1.合并列表
# """
# 方法一:for循环
# for i in num_list2:
#     num_list1.append(i)
# 方法二:
# 解包:将列表这一类容器解开成一个一个独立的元素
# 组包:将多个值合并到一个容器
# num_list = [*num_list1, *num_list2]
# """
# #方法三
# num_list = num_list1 + num_list2
# print("合并后的原始列表:",num_list1)
# #2.去除重复记录
# nem_list = []  #去除重复记录后的列表
# for num in num_list1:
#     #判断new_list中是否存在num元素,如果不存在,再添加
#     if num not in nem_list:
#         nem_list.append(num)
#
# print("去除重复元素后的列表:",nem_list)







# #生成1-20的平方列表。
# #方式一:传统方式
# new_list = []
# for i in range(1,21):
#     total = i**2
#     new_list.append(total)
# print("1-20的平方列表:",new_list)
#
# #方式二:列表推导式--->按照一定的规则快速生成一个列表的方法-->语法格式:[要插入的值 for i in 序列/列表 if 条件]
# new_list2 = [i**2 for i in range(1,21)]
# print("1-20的平方列表:",new_list2)




# #从如下数字列表中提取所有偶数，并计算其平方，组成一个新的列表。
# # 定义列表
# num_list = [19, 23, 54, 64, 87, 20, 109, 232, 123, 43, 26, 55, 72]
# new_list = [i**2 for i in num_list if i % 2 == 0]
# print("新的列表为:",new_list)


# #将如下多个列表合并为一个列表，并去重重复元素，排好序（升序）后输出到控制台。
# # 合并如下三个列表，并对合并后的列表进行元素的去重，然后排好序后输出到控制台
# list1 = ['M', 'A', 'C', 'E', 'F', 'G', 'H', 'L', 'N', 'I', 'J', 'K', 'O']
# list2 = ['X', 'Z', 'T', 'Y', 'D', 'E', 'F', 'G']
# list3 = ['W', 'A', 'S', 'D']
# list = list1 + list2 + list3
# print("合并后的列表:",list)
# new_list = []
# for i in list:
#     if i not in new_list:
#         new_list.append(i)
# print("去重后的列表为:",new_list)



# #将如下列表中能被3 或 5整除的元素提出来，并获取这些数字对应的平方，组成一个新的列表。
# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
# new_list = [i**2 for i in list1 if i % 3 == 0 or i % 5 == 0]
# print(new_list)


#将如下列表中的正数提取出来，封装为一个新的列表。
list1 = [11, 2, 31, 4, -5, 15, 17, 28, 49, 10, -11, 16, 54, -14, 36, -16, 87, -39]
new_list = [i for i in list1 if i > 0]
print(new_list)

















