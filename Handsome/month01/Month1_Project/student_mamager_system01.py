"""
学生管理系统
"""


class StudnetModel:
    """
    学生数据模型
    """

    def __init__(self, id=0, name="", age=0, score=0):
        """
        创建学生对象
        :param id: 编号
        :param name: 姓名
        :param age: 年龄
        :param score: 分数
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


class StudentManagerController:
    """
    学生核心逻辑控制器
    """

    def __init__(self):
        """
        创建学生管理器对象
        """
        self.__list_stu = []

    @property
    def list_stu(self):
        return self.__list_stu

    def add_stduent(self, stu):
        """
        添加学生对象
        :param stu: 需要添加的学生对象
        :return:
        """
        stu.id = int(len(self.__list_stu) + 1)
        self.__list_stu.append(stu)

    def order_id(self):
        for i in range(len(self.__list_stu)):
            self.__list_stu[i].id = i + 1

    def remove_student(self, id):

        """
        根据id删除对应学生信息
        :param id:
        :return:
        """
        for item in self.__list_stu:
            if item.id == id:
                self.__list_stu.remove(item)
                self.order_id()
                return True
        return False

    def updata_student(self, stu_info):
        """
        根据id查找并修改对应学生信息
        :param id:
        :return:
        """
        for item in self.list_stu:
            if item.id == stu_info.id:
                item.name = stu_info.name
                item.age = stu_info.age
                item.score = stu_info.score
                return True
        return False

    def order_by_score(self):
        new_list = self.__list_stu[:]
        for i in range(len(new_list) - 1):
            for j in range(i + 1, len(new_list)):
                if new_list[i].score < new_list[j].score:
                    new_list[i], new_list[j] = new_list[j], new_list[i]
        return new_list


class StudentManagerView:
    """

    """

    def __init__(self):
        """
        创建学生管理控制器对象
        """
        self.__controller = StudentManagerController()

    def __display_menu(self):
        print("------------------")
        print("1)添加学生")
        print("2)显示学生")
        print("3)删除学生")
        print("4)修改学生")
        print("5)按照成绩排序降序")
        print("------------------")

    def __select_menu(self):
        """
        选择菜单
        :return:
        """
        number = input("选择菜单")
        if number == "1":
            self.input_students()
        elif number == "2":
            self.output_students(self.__controller.list_stu)
        elif number == "3":
            self.__delete_student()
        elif number == "4":
            self.__modify_student()
        elif number == "5":
            target_list = self.__controller.order_by_score()
            self.output_students(target_list)

    def main(self):
        """
        学生管理器入口
        :return:
        """
        while True:
            self.__display_menu()
            self.__select_menu()

    def input_students(self):
        while True:
            if input("按y继续") == "y":
                stu = StudnetModel()
                stu.name = str(input("请输入姓名:"))
                stu.age = int(input("请输入年龄:"))
                stu.score = int(input("请输入成绩:"))
                self.__controller.add_stduent(stu)
            else:
                break

    def output_students(self,list_stu):
        for item in list_stu:
            print("序号：%d  |  姓名：% 4s  |  年龄：%d  |  成绩：%d" % (item.id, item.name, item.age, item.score))

    def __delete_student(self):
        while True:
            id = int(input("请输入要删除学生的id:"))
            if self.__controller.remove_student(id):
                print("删除成功！")
            else:
                print("删除失败！")
            if input("按e退出") == "e":
                break

    def __modify_student(self):
        while True:
            stu_info = StudnetModel()
            stu_info.id = int(input("请输入要修改学生的id:"))
            name = str(input("请输入要修改学生的姓名:"))
            stu_info.name = self.__controller.list_stu[stu_info.id - 1].name if name == "" else name
            age = input("请输入要修改学生的年龄:")
            stu_info.age = self.__controller.list_stu[stu_info.id - 1].age if age == "" else int(age)
            score = input("请输入要修改学生的成绩:")
            stu_info.score = self.__controller.list_stu[stu_info.id - 1].score if score == "" else int(score)
            if self.__controller.updata_student(stu_info):
                print("修改成功！")
            else:
                print("修改失败！")
            if input("按e退出") == "e":
                break



view = StudentManagerView()
view.main()
