"""
作业1：单词反转
”How are you”  --> “you are How”
"""
str_list = "How are you".split()  # .split把字符串转化为列表
# str_list.reverse()
# print(" ".join(str_list))   #.join把列表转化为字符串
str_result = " ".join(str_list[::-1])
print(str_result)

"""
作业3【扩展】：
在控制台中购买彩票
一注彩票：7个球(整数)
6个红球：1 --- 33  【不能重复】
1个蓝球：1 – 16  
例如：请输入第1个红球号码：
请输入第2个红球号码：
号码超过范围
已经存在
最后输出彩票：红球号码升序排列
"""
num_list = []
while len(num_list) < 6:
    num = int(input("请输入第%d红球号码：" % (len(num_list) + 1)))
    if num < 1 or num > 33:
        print("号码超出范围，请重新输入！")
        continue
    if num not in num_list:
        num_list.append(num)
    else:
        print("号码已存在，请重新输入！")
        continue
num_list.sort()
while len(num_list) < 7:
    num = int(input("请输入蓝球号码："))
    if num < 1 or num > 16:
        print("号码超出范围，请重新输入！")
    else:
        num_list.append(num)
print(num_list)
