"""
class Student:
    #类变量:所有对象共用
    count = 0

    @classmethod       #类的方法
    def get_total_students(cls):
        print(cls.count)

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.count += 1
stu01=Student("张三",23)
Student.get_total_students()
Student02=Student("拉斯",21)
Student03=Student("板卡",22)
print(stu01.count)
"""


class Student:
    def __init__(self,name="",sex=0,age=0,score=0):
        self.name=name
        self.sex=sex
        self.age=age
        self.score=score
    def print_info(self):
        print(self.name,self.age,self.sex,self.score)


list_students_info=[]
for i in range(1):
    stu=Student()
    stu.name=input("请输入第%d个学生的姓名："%(i))
    stu.sex=input("请输入第%d个学生的性别："%(i))
    stu.age=int(input("请输入第%d个学生的年龄："%(i)))
    stu.score=int(input("请输入第%d个学生的分数："%(i)))
    list_students_info.append(stu)

for i in list_students_info:
    i.print_info()


