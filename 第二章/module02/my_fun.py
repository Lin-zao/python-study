#__all__指定 from ... import * 导入哪些功能
__all__ = ["log_separator1", "log_separator3", "PI", "NAME"]
#常量(大写---不会发生变化的数据)
PI = 3.1415926

NAME = "黑马☆涛哥"


def log_separator1():
    print("- " * 30)# "_ "重复输出30次


def log_separator2():
    print("+ " * 30)


def log_separator3():
    print("# " * 30)


def log_separator4():
    print("* " * 30)

#测试
#__name__ : Python中内置变量,表示的当前模块的名字(直接运行当前模块,__name__的值为"__main__";当该模块被导入时,__name__的值就是模块名)
if __name__ == "__main__":
    log_separator1()

