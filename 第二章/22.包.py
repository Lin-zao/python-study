#1,导入模块
# import utils.my_fun
# utils.my_fun.log_separator1()
# utils.my_fun.log_separator2()

# from utils import my_fun
# my_fun.log_separator1()


#注意:如果要通过from utils import *导入包下所有的模块,需要__init__.py文件中添加__all__ = []
from utils import *
my_fun.log_separator1()

#2.导入模块中的功能
from utils.my_fun import log_separator1
log_separator1()



