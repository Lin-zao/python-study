# score = 700
#
# if score > 700:
#     print("欢迎来到清华大学")
#     print("哈哈哈哈哈")
# print("---------")
#
#
#
#
# #案例
# #正确的账号和密码
# account_original = 13458890713
# password_original = 123456
# #接收
# account = int(input("请输入账号:"))
# password = int(input("请输入密码:"))
# if account == account_original and password == password_original:
#     print("登录成功,进入B站首页")
# else:
#     print("账户或密码错误,请重新输入")
#
#
#
#
# #练习
# # 根据用户输入的年份，判断这一年是闰年还是平年。
# # 非整百年份‌，且能被4整除的年份是闰年
# # ‌整百年份‌（如1900年、2000年）必须能被400整除才是闰年
# year = int(input("请输入年份:"))
# if year % 100 != 0 and year % 4 == 0 or year % 100 == 0 and year % 400 ==0:
#     print(f"{year}是闰年")
# else:
#     print(f"{year}是平年")
#
#
#
# #需求1：根据用户输入的数字，判断该数字是奇数还是偶数。
# num = int(input("请输入一个数字:"))
# if num % 2 == 0:
#     print(f"{num}是偶数")
# else:
#     print(f"{num}是奇数")
# # 需求2：根据用户输入的年龄，判断该用户是否已经成年（>=18，成年；否则，未成年）。
# age = int(input("请输入你的年龄:"))
# if age >= 18:
#     print("你已经成年")
# else:
#     print("你未成年")
# # 需求3：根据用户输入的数字，判断该数字是正数还是负数（不考虑0）。
# num1 = int(input("请输入一个数字:"))
# if num1 > 0:
#     print(f"{num1}是正数")
# else:
#     print(f"{num1}是负数")
# # 需求4：根据用户输入的考试分数，判断该分数是否及格了（大于等于60就是及格了）。
# score = float(input("请输入考试分数:"))
# if score >= 60:
#     print("及格")
# else:
#     print("未及格")




# #if...elif...else
# num = int(input("请输入数字:"))
#
# if num > 0:
#     print(f"{num}是一个正数")
# elif num < 0:
#     print(f"{num}是一个负数")
# else:
#     print(f"{num}是0")



# # 根据输入用户名、密码进行登录系统。
# # 用户名、密码为 admin/666888 或 root/547527 或 zhangsan/123456，则输出登录成功
# # 否则就提示用户名或密码错误
# account = input("请输入用户名:")
# password = input("请输入密码:")
# if account == "admin" and password == "666888":
#     print("登录成功")
# elif account == "root" and password == "547527":
#     print("登录成功")
# elif account == "zhangsan" and password == "123456":
#     print("登陆成功")
# else:
#     print("用户名或密码错误!请重新输入")



# # 1. 根据输入的考试成绩，判断成绩等级。
# # 大于等于85分为优秀
# # 60-85分为及格
# # 否则就是不及格
# score = int(input("请输入成绩:"))
# if score >= 85:
#     print("优秀")
# elif score >= 60:
#     print("及格")
# else:
#     print("不及格")


# # 2. 购物折扣计算：根据输入的购物车的商品总额，以及如下的折扣规则，计算实际应付的金额。
# # 金额 >= 500: 8折
# # 300 <= 金额 < 500: 9折
# # 100 <= 金额 < 300: 95折
# # 金额 < 100: 无折扣
# total_amount = float(input("请输入商品总额:"))
# if total_amount >= 500:
#     print(f"实际应付的金额为:{total_amount * 0.8}")
# elif total_amount >= 300:
#     print(f"实际应付的金额为:{total_amount * 0.9}")
# elif total_amount >= 100:
#     print(f"实际应付的金额为:{total_amount * 0.95}")
# else:
#     print(f"实际应付的金额为:{total_amount}")



# #三角形类型判断：根据输入的三个边的边长(正整数)，判定是等边三角形、等腰三角形、普通三角形 ，还是不能构成三角形。
# # 构成三角形的条件：两边之和大于第三边
# # 三角形判定规则：
# # 三个边都相等: 等边三角形
# # 两个边相等: 等腰三角形
# # 三个边都不相等: 普通三角形
# a = int(input("请输入三角形的边长:"))
# b = int(input("请输入三角形的边长:"))
# c = int(input("请输入三角形的边长:"))
# if a>0 and b>0 and c>0 and a + b > c and a + c > b and b + c > a:
#     if a == b == c:
#         print("该三角形是等边三角形")
#     elif a == b or b == c or c == a:
#         print("该三角形是等腰三角形")
#     else:
#         print("该三角形是普通三角形")
# else:
#     print("该三边不能构成三角形")


"""
北京市居民年度用电电费计算：根据输入的用电度数，计算电费
北京市居民电费采用阶梯电价计价方式，所谓阶梯电价是指按照用户消费的电量分段定价，用电价格随用电量增加呈阶梯状逐级递增的一种电价定价机制。
阶梯电价规则：
第一档：2880度以下，电费单价0.4883元/度
第二档：2880-4800度，电费单价0.5383元/度
第三档：4800度以上，电费单价0.7883元/度

"""
electricity_consume = float(input("请输入用电度数:"))
if electricity_consume < 2880:
    print(f"电费为:{electricity_consume * 0.4883}")
elif electricity_consume <4800:
    print(f"电费为:{(2880 * 0.4883) + (electricity_consume - 2880) * 0.5383}")
else :
    print(f"电费为:{(2880 * 0.4883) + (4800 - 2880) * 0.5383 + (electricity_consume - 4800) * 0.7883}")


