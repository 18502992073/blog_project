"""
    for range
"""
# for item in "我爱python":
#     print(item)
# for i in range(10):
#     print(i)
# 5 4   3   2   1     0
# for i in range(5, -1, -1):
#     print(i)
#练习1：1－100累加
# sum=0
# for i in range(1,101):
#     sum+=i
# print(sum)
#练习2：1－100偶数累加
# sum=0
# for i in range(1,101):
#     # if i%2==0:
#     #     sum+=i
#     if i%2!=0:
#         continue
#     sum+=i
# print(sum)


# number=int(input("请输入一个数："))
# if number<2:
#     print(str(number) + "不是素数")
# else:
#     #依次生成2－number-1之间的整数
#     for item in range(2,number):
#         if number % item==0:
#             print(str(number) + "不是素数")
#             #如果有了结论，后续数字不再判断
#             break
#     else:
#         print(str(number) + "是素数")
#         #没有执行break

# print(ord("Z"))
# print(chr(97))

#在控制台中输入一个字符串，打印该字符串的每个字符编码．
string=input("请输入字符串")
for i in string:
    print(ord(i))

#循环输入编码值，显示字符．待输入负数时退出．
while True:
    num = int(input("请输入编码值："))
    if num<0 :
        break
    print(chr(num))







