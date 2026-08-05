"""打印一个长度为10，宽度为5的长方形
* * * * * * * * * *
* * * * * * * * * *
* * * * * * * * * *
* * * * * * * * * *
* * * * * * * * * *

print("*")：自带换行效果，每一次执行都会输出新的一行；

print("*", end="")：end表示的是每一次输出以什么结束；默认\n，表示换行。


m = int(input("请输入长度:"))
n = int(input("请输入宽度:"))

for i in range(n):#控制行
    for j in range(m):#控制列
        print("*",end=" ")
    print()
"""


# #打印99乘法表
# for i in range(1,10):#行
#     for j in range(1,i+1):
#         print(f"{j} * {i} = {i * j}",end="\t")
#     print()

# #1.
# a = int(input("请输入直角边的边长:"))
# for i in range(1,a+1):
#     for j in range(1,i+1):
#         print("*",end="\t")
#     print()

# #2.
# num = int(input("请输入数字:"))
# for i in range(1,num+1):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()

# for i in range(8):
#     for j in range(8):
#         if (i + j) % 2 == 0:
#             print("■",end=" ")
#         else:
#             print("□",end=" ")
#     print()



# """
# 需求：根据输入的用户名密码执行登录操作，具体要求如下：
# 正确的用户名和密码为admin/666888 、zhangsan/123456
# 输入用户名和密码进行登录，直到登录成功，程序结束运行; 如果登录失败，则继续输入用户名和密码进行登录
# 输入的用户名和密码不能为空！
# 登录成功：输出 "登录成功，进入B站首页~"
# 登录失败：输出 "用户名或密码错误, 请重新输入!"
# """
#
#
# while True:
#     user_name = input("请输入用户名:")
#     password = input("请输入密码:")
#     if user_name == "" or password == "":
#         print("输入的用户名和密码不能为空,请重新输入!")
#     elif (user_name == "admin" and password == "666888") or (user_name == "zhangsan" and password == "123456"):
#         print("登录成功，进入B站首页~")
#         break
#     else:
#         print("用户名或密码错误, 请重新输入!")


# import random
# random_num = random.randint(1,100)
# while True:
#     num = int(input("请输入一个数字:"))
#     if num > random_num:
#         print("输入的数字太大了!")
#     elif num < random_num:
#         print("输入的数字太小了")
#     else:
#         print("猜对了")
#         break
# print(f"随机生成的数字是{random_num}")





# #将1-1000之间（含1000）所有的5的倍数的数字累加起来。
# total = 0
# for i in range(1,1001):
#     if i % 5 == 0:
#         total += i
# print(f"1-1000之间（含1000）所有的5的倍数的数字累加起来为:{total}")



#统计字符串 "akiwksjakdiklowiqaamnvbamvaxnsjdsjkaaxkjd" 字符串中有多少个a和k。
total = 0
for i in "akiwksjakdiklowiqaamnvbamvaxnsjdsjkaaxkjd":
    if i == "a" or i == "k":
        total += 1
print(f"字符串中有{total}个a和k")







