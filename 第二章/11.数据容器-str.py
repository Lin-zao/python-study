# #字符串 基本操作--->无法修改 有序性 可迭代性
# s = "Hello-Python"
#
# print(s[4])#正向索引
# print(s[-7])#反向索引
#
# for i in s:
#     print(i)
#
# #切片
# print(s[0:5])
# print(s[:5])
# print(s[6:])


# #-----------字符串常用方法--------
# s = "Hello-Python-Hello-World"
# #find() 查找指定字符串第一次出现的位置
# index = s.find("-")
# print(index)
#
# #count() 统计子字符串在指定字符串中出现的次数
# c = s.count("o")
# print(c)
#
# #upper()转为大写
# su = s.upper()
# print(su)
#
# #lower()转为小写
# ls = s.lower()
# print(ls)
#
# #split()将字符串按照指定字符串切割-列表
# slist = s.split("-")
# print(slist)
#
# #strip() 去除字符串两端的空格
# ss = s.strip()
# print(ss)
#
# #replace() 将字符串中的指定子串替换为新的内容
# sr = s.replace("-", "_")
# print(sr)
#
# #startswith()/endswith()判断字符串是否是以指定的字符串开头/结尾,返回布尔值
# print(s.startswith("Hello"))
# # print(s.endswith("Python"))
#
#
# print("------------")
# print(s)








# #邮箱格式验证：用户输入一个邮箱, 验证邮箱格式是否正确(包含一个@和至少一个.), 如果输入正确, 输出"邮箱格式正确", 否则输出"邮箱格式错误"。
# while True:
#     email = input("请输入邮箱:")
#     if email.count("@") == 1 and "." in email:
#         print("邮箱格式正确")
#         break
#     else:
#         print("邮箱格式错误,请重新输入!")



# """
# 输入一个字符串, 判断该字符串是否是回文(两边对称) 。
# 黄山落叶松叶落山黄
# 上海自来水来自海上
#
# """
# num = input("请输入:")
# if num[:] == num[::-1]:
#     print(f"{num}是回文")
# else:
#     print(f"{num}不是回文")

#需求2：将用户输入的10个字符串, 反转后全部转换为大写, 然后记录在列表中, 最后将列表内容，遍历输出出来。
num_list = []
for i in range(10):
    num = input("请输入字符串:")
    num_re = num[::-1]
    num_re_up = num_re.upper()
    num_list.append(num_re_up)
for s in num_list:
    print(s)

