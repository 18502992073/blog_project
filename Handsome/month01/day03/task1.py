# 1.输入一个季度，打印该季度的月份
quarter = input("请输入季度，例如：第一季度")
if quarter == "第一季度":
    print("该季度的月份为：1，2，3")
elif quarter == "第二季度":
    print("该季度的月份为：4,5,6")
elif quarter == "第三季度":
    print("该季度的月份为：7,8,9")
elif quarter == "第四季度":
    print("该季度的月份为：10,11,12")
else:
    print("输入错误！")
"""一个球从100m的高度落下，
每次弹回原高度的一半。
计算：1. 总共经过？次最终落地(可以弹起的最小高度0.01m)。"""
upspring_hight = 0
hight = 100
count = 0
while hight/2 > 0.01:
    upspring_hight += hight     #下降高度
    hight /= 2
    upspring_hight += hight     #上升高度
    count += 1
    if hight<0.01:
        upspring_hight += hight #下降高度
print("小球反弹" + str(count) + "次")
print("总共经过" + str(round(upspring_hight)) + "米")


hight = 100
count = 0
upspring_hight = hight
while hight/2 > 0.01:
    hight /= 2
    upspring_hight += hight*2
    count += 1
    print(count,hight)
print("小球反弹" + str(count) + "次")
print("总共经过" + str(round(upspring_hight)) + "米")
