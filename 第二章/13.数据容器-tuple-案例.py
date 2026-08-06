"""
    根据如下提供的学生成绩单，完成如下需求：
        1. 计算每个学生的总分、各科平均分，然后一并输出出来。
        2. 统计各科成绩的最低分、最高分、平均分，并输出。
        3. 查找成绩优秀（平均分大于90）的学生，并输出。
"""
students = (
    ("S001", "王林", 85, 92, 78),
    ("S002", "李慕", 92, 88, 95),
    ("S003", "十三", 78, 85, 82),
    ("S004", "曾牛", 88, 79, 91),
    ("S005", "周轶", 95, 96, 89),
    ("S006", "王卓", 76, 82, 77),
    ("S007", "红蝶", 89, 91, 94),
    ("S008", "徐立", 75, 69, 82),
    ("S009", "许木", 86, 89, 98),
    ("S010", "遁天", 66, 59, 72)
)
#1. 计算每个学生的总分、各科平均分，然后一并输出出来。
print("学号\t\t姓名\t\t语文\t\t数学\t\t英语\t\t总分\t\t平均分")
#方法一:基础
for s in students:
    total = s[2] + s[3] + s[4]
    avg = total / 3
    print(f"{s[0]}\t{s[1]}\t\t{s[2]}\t\t{s[3]}\t\t{s[4]}\t\t{total}\t\t{avg:.1f}")

print("-----------------------------------------------------")
#方法二:解包
for id,name,chinese,math,english in students:
    total = chinese + math + english
    avg = total / 3
    print(f"{id}\t{name}\t\t{chinese}\t\t{math}\t\t{english}\t\t{total}\t\t{avg:.1f}")

#2. 统计各科成绩的最低分、最高分、平均分，并输出。
chinese_scores = [i[2] for i in students]
math_scores = [i[3] for i in students]
english_scores = [i[4] for i in students]
print(f"语文最低分为:{min(chinese_scores)},语文最高分为:{max(chinese_scores)},语文平均分为:{sum(chinese_scores)/len(chinese_scores)}")
print(f"数学最低分为:{min(math_scores)},数学最高分为:{max(math_scores)},数学平均分为:{sum(math_scores)/len(math_scores)}")
print(f"英语最低分为:{min(english_scores)},英语最高分为:{max(english_scores)},英语平均分为:{sum(english_scores)/len(english_scores)}")

#3. 查找成绩优秀（平均分大于90）的学生，并输出。
print("优秀学生(平均分 > 90)名单如下: ")
for i in students:
    total = i[2] + i[3] + i[4]
    avg = total / 3
    if avg > 90:
        print(f"学号: {i[0]}, 姓名: {i[1]}, 平均分: {avg:.1f}")
