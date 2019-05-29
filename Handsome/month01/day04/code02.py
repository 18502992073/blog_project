"""
    字符串字面值
 """
for i in range(120, -1, -1):
    minute = i // 60
    second = i % 60
    print("%.2d秒显示为：%.2d:%.2d" % (i, minute, second))

"""
练习1：在控制台中输入一个很长的字符串，如果该字符串中包含”qtx”，则提示”老师好”.
"""
string = input("请输入字符串：")
if "qtx" in string:
    print("老师好！")
"""
练习2：输入一个字符串，打印如下内容。
(1)	打印字符串第一个字符
(2)	打印字符串最后一个字符串
(3)	如果长度是奇数，则打印字符串中间的字符串len(字符串) 返回长度
"""
string = input("请输入字符串：")
print(string[0])
print(string[-1])
if len(string) % 2 != 0:
    length = len(string) // 2
    print(string[length])
    print("字符串长度%d" % (len(string)))
else:
    print(" ")

"""练习3：在控制台中输入一个整数，打印一个矩形."""
number = int(input("请输入边长："))
for i in range(1, number + 1):
    if i == 1 or i == number:
        print("*" * number)
    else:
        print("*%s*" % (" " * (number - 2)))
"""
练习4：写一个程序，输入一个字符串，把字符串的第一个字符串和最后一个字符去掉。
"""
string = input("请输入字符串：")
print(string[1:-1])
"""扩展：输入一个字符串，判断是否为回文。
        回文是中心对称的文字。
        例如：上海自来水来自海上
        山西运煤车煤运西山
"""
string = input("请输入字符串：")
length = len(string)
for i in range(0, length // 2):
    if string[i] != string[(- 1 - i)]:
        print("不是回文")
        break
else:
    print("是回文")



string = input("请输入字符串：")
if string != string[::-1]:
    print("不是回文")
else:
    print("是回文")