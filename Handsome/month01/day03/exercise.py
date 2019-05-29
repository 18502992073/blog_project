#1. 判断一个数的正负
numb = int(input("请输入一个整数"))
if numb > 0:
    print("正数")
elif numb < 0:
    print("负数")
else:
    print("零")

#2.月份判断季节（1）
month = input("请输月份")
if month in ("1", "2", "3"):
    print("春")
elif month in ("4", "5", "6"):
    print("夏")
elif month in ("7", "8", "9"):
    print("秋")
elif month in ("10", "11", "12"):
    print("冬")
else:
    print("输入错误，请重新输入！")

#3.月份判断季节（2）
month = int(input("请输月份"))
if month >=1 and month<=12:
    if month <= 3:
        print("春")
    elif month <= 6:
        print("夏")
    elif month <= 9:
        print("秋")
    else :
        print("冬")
else:
    print("输入错误，请重新输入！")


#4.月份判断天数（1）
month = int(input("请输月份: "))
if 1 <= month <= 12:
    if month == 2:
        print("28天")
    elif month == 4 or month == 6 or month == 9 or month == 11:
        print("30天")
    else:
        print("31天")
else:
    print("错误")

# 5.月份判断天数（2）
month = input("请输月份: ")
if month in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12",):
    if int(month) == 2:
        print("28天")
    elif int(month) == 4 or int(month) == 6 or int(month) == 9 or int(month) == 11:
        print("30天")
    else:
        print("31天")
else:
    print("错误")

# 6.在控制台中获取一个整数，打印奇数或偶数
numb = int(input("请输入一个整数"))
if numb % 2 == 0:
    print("偶数")
else:
    print("奇数")


# 7.判断润年，如果是闰年输出29天，否则输出28天．
year = int(input("输入年份"))
day = 29 if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 else 28
print(day)

# 8.一张纸折多少次超过珠峰高度
star, end = int(input("循环开始值")), int(input("循环结束值"))
while star <= end:
    print(star)
    star += 1
th = 0.01
count = 0
hight = 8844.43 * 1000
while th <= hight:
    th *= 2
    count += 1
print(count)
print(th)

# 9.猜数不限次数
import random

number = random.randint(1, 101)
print(number)
guess = None
count = 0
while guess != number:
    guess = int(input("请猜一个数"))
    count += 1
    if guess < number:
        print("猜小了！")
    else:
        print("猜大了")
else:
    print("猜对了")
print("猜了" + str(count)+"次")


# 10.猜数限次数
import random

number = random.randint(1, 100)#random.randint()包含两端，random.random()不包含两端
print(number)
count = 0
while count < 3:
    guess = int(input("请猜一个数"))
    count += 1
    if number > guess:
        print("猜小了！")
    elif guess > number:
        print("猜大了")
    else:
        print("猜对了,猜了" + str(count) + "次")
        break
else:
    print("没机会了")