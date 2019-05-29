"""
练习：实现两个列表元素的全排列
[“香蕉”,”苹果”,”哈密瓜”,”草莓”]
[“牛奶”,”咖啡”,”雪碧”]
"""
# ls1 = ["香蕉", "苹果", "哈密瓜", "草莓"]
# ls2 = ["牛奶", "咖啡", "雪碧"]
# re = [i + j for i in ls1 for j in ls2]
# for i in re:
#     print(i, end=",")

"""
作业2：在控制台中录入学生信息name,age,score将每个学生输出到控制台(一个学生一行)
数据结构：
[
{
“name”:”zs”,
”age”:25,
”score”:100, 
},
{
“name”:”ls”,
”age”:35,
”score”:80, 
}
 ]
"""

# ls = []
# while True:
#     str_name = input("请输入姓名(空值结束)：")
#     str_age = input("请输入年龄(空值结束)：")
#     str_score = input("请输入分数(空值结束)：")
#     if str_name == "" and str_age == "" and str_score == "":
#         break
#     dt = {}
#     dt["name"] = str_name
#     dt["age"] = str_age
#     dt["score"] = str_score
#     ls.append(dt)
#     print(ls)
# for i in range(len(ls)):
#     print("姓名:", ls[i]["name"], "  年龄:", ls[i]["age"], "  分数:", ls[i]["score"])

"""
扩展作业:设计一个算法，判断列表中是否具有相同元素。
[1,4,7,5,1,9,8]
"""
# str_input = input("请输入一串字符：")
# old_len = len(str_input)
# set1 = set(str_input)
# new_len = len(set1)
# if old_len == new_len:
#     print("字符串中没有相同元素")
# else:
#     print("字符串中有相同元素")

str_input = input("请输入一串字符：")
ls = list(str_input)
state = False
for i in range(len(ls)-1):
    for j in range(i + 1, len(ls)):
        if ls[i] == ls[j]:
            state = True
            break
if state == True:
    print("有相同")
else:
    print("无相同")
