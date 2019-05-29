# 练习1使用列表推到式，生成1--10以内的奇数列表
# list_num = []
# for i in range(0, 10):
#     if i % 2 == 1:
#         list_num.append(i)
# print(list)
# list_num = [i for i in range(0, 10) if i % 2 == 1]
#
# print([i for i in range(1, 11, 2)])

# [3,56,7,6,19,3]获取列表大于10的元素
# list_original = [3, 56, 7, 6, 19, 3]
# print([i for i in list_original if i > 10])

# 在控制台中输入一个起始值和一个终止值将偶数和奇数分别存入一个列表
# begin = int(input("请输入开始值："))
# end = int(input("请输入终止值："))
# list_even = [i for i in range(begin, end) if i % 2 == 0]
# list_odd = [i for i in range(begin, end) if i % 2 == 1]
# print(list_even)
# print(list_odd)

# 计算某年某月某日是这一年的第几天．
# year = int(input("请输入年"))
# mon = int(input("请输入月"))
# day = int(input("请输入日"))
# mon2 = 29 if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 else 28
# tp = (31, mon2, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
# dy = 0
# for i in tp[:mon - 1]:
#     dy += i
# result = dy + day
# print(result)
# result = sum(tp[:mon - 1]) + day
# print(result)

# 月份判断天数
# month = int(input("请输月份: "))
# tp = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
# if 1 <= month <= 12:
#     print(tp[month - 1])
# else:
#     print("错误！")
"""
嵌套列表解析
Python的列表还可以嵌套。
以下实例展示了3X4的矩阵列表：
"""
matrix = [
     [1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12],
 ]
# 以下实例将3X4的矩阵列表转换为4X3列表：

print([[row[i] for row in matrix] for i in range(4)])

# 以下实例也可以使用以下方法来实现：

transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])
print(transposed)

# 另外一种实现方法：
transposed = []
for i in range(4):
# the following 3 lines implement the nested listcomp
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)
print(transposed)
