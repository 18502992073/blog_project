# n = int(input("输入学生总数"))
# list01 = []
# for i in range(n):
#     list01.append(input("请输依次入学生成绩："))
# print(list01)
# total = 0
# for i in list01:
#     total += int(i)
# print(total)
# print(total / n)
# print(max(list01))
# print(min(list01))

# list02 = []
# while True:
#     num = int(input("输入整数:"))
#     if num == -1:
#         break
#     if num not in list02:
#         list02.append(num)
#     else:
#         print("数据已存在！")
# list02.sort()
# print(list02)
# print(max(list02))
# print(min(list02))
# print(list02[-2])


str_list = []
while True:
    string = input("输入字符串:")
    if string == "q":
        break
    str_list.append(string)
print("".join(str_list))
