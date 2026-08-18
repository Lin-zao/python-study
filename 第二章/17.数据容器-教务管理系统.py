menu = """
# # # # # # # # # # # # # # # # # # # # # # # # [菜单] # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# 1.添加学生信息     2.修改学生信息     3.删除学生信息    4.查询学生信息     5.列出所有学生   6.统计班级成绩    7.退出系统     #

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

"""
#scores_manege = {"淋枣":{"语文成绩":95,"数学成绩":95,"英语成绩":95}}

scores_manege = {}
print("欢迎来到教务管理系统!")
while True:
    print(menu)
    choice = input("请选择要执行的操作(1-7):")
    match choice:
        case "1":
            name = input("请输入姓名:")
            if name not in scores_manege:
                chinese_scores = float(input("请输入语文成绩:"))
                math_scores = float(input("请输入数学成绩:"))
                english_scores = float(input("请输入英语成绩:"))
                scores_manege[name] = {"语文成绩":chinese_scores,"数学成绩":math_scores,"英语成绩":english_scores}
                print(f"添加{name}学生信息成功!")
            else:
                print("学生已存在,请重新选择!")
        case "2":
            name = input("请输入姓名:")
            if name in scores_manege:
                chinese_scores = float(input("请输入需要1修改的语文成绩:"))
                math_scores = float(input("请输入需要修改的数学成绩:"))
                english_scores = float(input("请输入需要修改的英语成绩:"))
                scores_manege[name] = {"语文成绩": chinese_scores, "数学成绩": math_scores, "英语成绩": english_scores}
                print(f"修改{name}学生信息成功!")
            else:
                print("学生不存在,请重新选择!")
        case "3":
            name = input("请输入姓名:")
            if name in scores_manege:
                del scores_manege[name]
            else:
                print("学生不存在,请重新选择!")
        case "4":
            name = input("请输入需要查询学生姓名:")
            if name in scores_manege:
                info = scores_manege[name]
                print("\n=====学生信息=====")
                print(f"姓名:{name}")
                print("语文:",info["语文成绩"])
                print("数学:",info["数学成绩"])
                print("英语:",info["英语成绩"])
            else:
                print("学生不存在,请重新选择!")
        case "5":
            print("\n====全部学生列表====")
            for manege_name in scores_manege.keys():
                manege_info = scores_manege[manege_name]
                print(f"姓名:{manege_name},语文:{manege_info['语文成绩']},数学:{manege_info['数学成绩']},英语:{manege_info['英语成绩']}")
        case "6":
            if not scores_manege:
                print("系统中暂无学生信息，请先添加学生 ~")
                continue
            chinese_list = []
            math_list = []
            english_list = []

            for student_name,scores in scores_manege.items():
                chinese_list.append(scores["语文成绩"])
                math_list.append(scores["数学成绩"])
                english_list.append(scores["英语成绩"])

            chinese_max = max(chinese_list)
            math_max = max(math_list)
            english_max = max(english_list)

            chinese_min = min(chinese_list)
            math_min = min(math_list)
            english_min = min(english_list)

            chinese_avg = sum(chinese_list) / len(chinese_list)
            math_avg = sum(math_list) / len(math_list)
            english_avg = sum(english_list) / len(english_list)

            chinese_max_stu = [stu_name for stu_name,scores in scores_manege.items() if scores["语文成绩"] == chinese_max]
            chinese_min_stu = [stu_name for stu_name,scores in scores_manege.items() if scores["语文成绩"] == chinese_min]

            math_max_stu = [stu_name for stu_name,scores in scores_manege.items() if scores["数学成绩"] == math_max]
            math_min_stu = [stu_name for stu_name,scores in scores_manege.items() if scores["数学成绩"] == math_min]

            english_max_stu = [stu_name for stu_name, scores in scores_manege.items() if scores["英语成绩"] == english_max]
            english_min_stu = [stu_name for stu_name, scores in scores_manege.items() if scores["英语成绩"] == english_min]

            print("===== 班级成绩统计 =====")
            print(f"语文 - 最高分: {chinese_max}, 最低分: {chinese_min}, 平均分: {chinese_avg:.2f}")
            print(f"     最高分学生: {chinese_max_stu}")
            print(f"     最低分学生: {chinese_min_stu}")

            print(f"数学 - 最高分: {math_max}, 最低分: {math_min}, 平均分: {math_avg:.2f}")
            print(f"     最高分学生: {math_max_stu}")
            print(f"     最低分学生: {math_min_stu}")

            print(f"英语 - 最高分: {english_max}, 最低分: {english_min}, 平均分: {english_avg:.2f}")
            print(f"     最高分学生: {english_max_stu}")
            print(f"     最低分学生: {english_min_stu}")
            print("========================")
        case "7":
            print("感谢使用教务管理系统，程序退出！")
            break
        case _:
            print("输入有误,请输入1~7之间的数字！")
