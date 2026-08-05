# i = 0
# while i < 10:
#     print("人生苦短,我用python")
#     i += 1
# else:
#     print("循环正常结束,执行完毕")



#计算1-100之间所有偶数的累加之和。
total = 0
i = 1
while i <=100:
    if i % 2 == 0:
        total += i
    i += 1
print(f"1-100之间所有偶数的累加之和为:{total}")