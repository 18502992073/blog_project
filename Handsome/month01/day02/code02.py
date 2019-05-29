# 数字交换.1
numb1, numb2 = input("请输入第一个值"), input("请输入第二个值")
numb1, numb2 = numb2, numb1
print("第一个值为:" + numb1)
print("第二个值为:" + numb2)
# 数字交换.2
numb1, numb2 = input("请输入第一个值"), input("请输入第二个值")
numb3 = numb1
numb1 = numb2
numb2 = numb3
print("第一个值为:" + numb1)
print("第二个值为:" + numb2)
# 时间化秒
hour = float(input("请输入小时数"))
minute = int(input("请输入分钟数"))
second = int(input("请输入秒数"))
total = hour * 60 * 60 + minute * 60 + second
print("总秒数为：" + str(total))
# 四位数各位相加
number = int(input("请输入一个四位整数"))
a = number // 1000
b = number % 1000 // 100
c = number % 100 // 10
d = number % 10
result = a + b + c + d
print(result)
# 润年判断.1
year = int(input("输入年份"))
value1 = year % 4 == 0 and year % 100 != 0
value2 = year % 400 == 0
result = value1 or value2
print(result)
# 润年判断.2
year = int(input("输入年份"))
if year % 4 == 0 and year % 100 != 0:
    print("润年")
elif year % 400 == 0:
    print("润年")
else:
    print("平年")
