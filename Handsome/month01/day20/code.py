# from common.list_tools import ListHelper
class StudentModel:
    """
        数据模型类
    """

    def __init__(self, id=0, name="", age=0, score=0):
        """
        创建学生对象
        :param id: 编号
        :param name: 姓名
        :param age: 年龄
        :param score: 成绩
        """
        self.id = id
        self.name = name
        self.age = age
        self.score = score

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__age = value

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, value):
        self.__score = value

    def __str__(self):
        return "%d,%s,%d,%d" % (self.id, self.name, self.age, self.score)

    def __repr__(self):
        return "StudentModel(%d,'%s',%d,%d)" % (self.id, self.name, self.age, self.score)


stu1 = StudentModel(1, "zs1", 27, 92)
stu2 = StudentModel(2, "zs2", 24, 99)
stu3 = StudentModel(101, "zs3", 36, 97)
list_stu = [stu1, stu2, stu3]

class ListHelper:
    @staticmethod
    def order_by(list_target, func_condition):
        """
            按条件升序排列
        :param list_target:　对象列表
        :param func_condition:　排序条件
        :return:
        """
        new_list = list_target[:]
        for i in range(len(list_target) - 1):
            for j in range(i + 1, len(list_target)):
                if func_condition(new_list[i]) > func_condition(new_list[j]):
                    new_list[i], new_list[j] = new_list[j], new_list[i]
        return new_list


for i in ListHelper.order_by(list_stu, lambda s: s.score):
    print(i, end="  ")
print()





# re5 = ListHelper.find_one(list_stu, lambda s: s.id == 101)
# print(re5)
# for i in ListHelper.find_all(list_stu, lambda s: s.score > 60):
#     print(i, end="  ")
#
# print()
#
# for i in ListHelper.find_all(list_stu, lambda s: s.age < 25 and s.score > 80):
#     print(i)
#
# print(ListHelper.get_max_value(list_stu, lambda s: s.score))
#
# print(ListHelper.sum(list_stu,lambda s:s.age))
#
# for i in ListHelper.select(list_stu,lambda s:s.id):
#     print(i,end="  ")
# print()
