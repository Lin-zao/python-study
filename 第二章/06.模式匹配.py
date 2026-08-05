# day = input("请输入星期几:")
# match day:
#     case "1":
#         print("星期一")
#     case "2":
#         print("星期二")
#     case "3":
#         print("星期三")
#     case "4":
#         print("星期四")
#     case "5":
#         print("星期五")
#     case "6" | "7":
#         print("周末")
#     case _:
#         print("输入有误")
#
# #实现一个计算器，可以实现+ - * / 运算，用户输入需要运算的两个数以及运算符之后，就可以进行计算。
# num1 = float(input("请输入数字1:"))
# num2 = float(input("请输入数字2:"))
# operator = input("请输入运算符:")
# match operator:
#     case "+":
#         print(f"{num1} + {num2} = {num1 + num2}")
#     case "-":
#         print(f"{num1} - {num2} = {num1 - num2}")
#     case "*":
#         print(f"{num1} * {num2} = {num1 * num2}")
#     case "/" if num2 != 0:
#         print(f"{num1} / {num2} = {num1 / num2}")
#     case _:
#         print("运算符输入有误,请重新输入!")



#练习
instruction = input("请输入指令:")
match instruction:
    case "上" | "w" | "W":
        print("角色向上移动")
    case "下" | "s" | "S":
        print("角色向下移动")
    case "左" | "a" | "A":
        print("角色向左移动")
    case "右" | "d" | "D":
        print("角色向右移动")
    case "跳" | " " :
        print("角色跳跃")
    case "攻击" | "j" | "J":
        print("角色发动攻击")
    case "退出" | "esc" | "ESC":
        print("角色退出游戏")
    case _:
        print("请重新输入指令!")
