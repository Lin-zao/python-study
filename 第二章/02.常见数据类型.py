#常见数据类型 --->type() 获取指定的字面量或变量的类型
from platform import libc_ver

print(type("hello"))

#常见数据类型 ---> isinstance(数据,类型)-->判定数据是否是指定的类型,如果是:True,否则:False
num = 100
print(isinstance(num,int))
print(isinstance(num,float))


#字符串
#定义字符串的三种方式
s1 = "Hello"
s2 = 'Hello'
s3 = """
Hello:
    欢迎大家来到
"""
print(s1)
print(s2)
print(s3)
print(type(s1))
print(type(s2))
print(type(s3))


#转义字符 \'  \" \n \t
msg = 'It\'s very good'
print(msg)

msg2 = "Hello的意思就是\"你好\""
print(msg2)

print("hahahha\nhah")



#字符串拼接
s1 = "人生苦短" "我用python"
print(s1)
s2 = "人生苦短"+"我用python"
print(s2)


name = "林子豪"
age = 21
sub = "计算机科学与技术"
love = "base"
print(f"大家好,我是{name},今年{age}岁,学习的专业是{sub},爱好是{love}")

s1 = "lzh"
s2 = 18
print("大家好,我是%s,今年:%s" %(s1,s2)) 