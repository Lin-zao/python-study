# # 注意: 函数定义的时候并不会执行, 只有在调用函数的时候, 函数体的逻辑才会执行 ; 函数必须先定义, 后调用;
# #函数定义
# def out_line():
#     print("------------------------------------------------")
#     print("------------------------------------------------")
#
# # 函数调用
# out_line()
#
# #函数的参数与返回值
# #函数1:计算圆的面积-->半径
# def circle_area(r):
#     area = 3.14 * r**2
#     return area
# area = circle_area(10)
# print(area)
#
#
# #函数2:计算长方形的面积--长,宽
# def rectangle(l,w):
#     """
#     计算长方形的面积
#     :param l: 长
#     :param w: 宽
#     :return: 长方形的面积
#     """
#     area = l * w
#     return area
# area = rectangle(10,20)
# print(area)
#
# #函数3:计算圆的面积,周长 --半径---->如果返回值有多个,多个返回值之间用逗号隔开
# def circle_area_len(r):
#     """
#     计算圆的面积,周长
#     :param r: 半径
#     :return: 圆的面积,周长
#     """
#     return round(3.14 * r**2,1) , round(2 * 3.14 * r,1)
# area , len = circle_area_len(10)
# print(area)
# print(len)
#
# # 函数的嵌套调用
# def function_a():
#     print("a ... before")
#     function_b()
#     print("a ... after")
#
# def function_b():
#     print("b ... before")
#     function_c()
#     print("b ... after")
#
# def function_c():
#     print("c ...")
#
# function_a()
#
# print("函数调用完毕 ~")
#
# #案例1: 定义一个函数：根据传入的底和高计算三角形面积的函数（三角形面积 = 底 * 高 / 2）。
# def triangle_area(bottom,high):
#     """
#     计算三角形面积
#     :param bottom: 三角形底
#     :param high: 三角形高
#     :return: 三角形面积
#     """
#     return bottom * high / 2
# print("底长为 30, 高度为 20 的三角形面积: ", triangle_area(30, 20))
#
# # 案例2: 定义一个函数：计算传入的字符串中元音字母的个数（元音字母为 aeiouAEIOU）。
# def count_y(s):
#     """
#     统计字符串中元音字母的个数
#     :param s:字符串
#     :return:元音字母的个数
#     """
#     num = 0
#     for i in s:
#         if i in "aeiouAEIOU":
#             num += 1
#     return num
# print(count_y("Hello Python Hello World OK"))
#
# # 案例3: 定义一个函数：计算传入的班级学员高考成绩列表中成绩的最高分、最低分、平均分(保留1位小数)，并返回。
# def calc_score(score_list):
#     """
#     计算传入的班级学员高考成绩列表中成绩的最高分、最低分、平均分
#     :param score_list:分数列表
#     :return:最高分, 最低分, 平均分
#     """
#     max_s = max(score_list)
#     min_s = min(score_list)
#     avg_s = sum(score_list) / len(score_list)
#     return max_s, min_s, avg_s
# s_list = [589, 609, 605, 643, 677, 455, 477, 489, 503]
# max_score, min_score, avg_score = calc_score(s_list)
# print("最高分: ", max_score)
# print("最低分: ", min_score)
# print("平均分: ", avg_score)




# 定义一个函数，根据传入的分数，计算对应的分数等级并返回。
# 分数 >= 90：A
# 分数 >= 75：B
# 分数 >= 60：C
# 分数 < 60：D
def score(s):
    if s >= 90:
        return "A"
    elif s >= 75:
        return "B"
    elif s >= 60:
        return "C"
    else:
        return "D"
print(score(59))



# 需求2：定义一个函数，用于判断一个字符串是否是回文串，返回bool值。
# 把字符串反转，如果和原字符串相同，就是回文串。（如："level"，"radar"，"黄山落叶松叶落山黄"）
def palindrome(s):
    if s == s[::-1]:
        return True
    else:
        return False
print(palindrome("level"))


