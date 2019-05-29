"""
    学生系统界面
"""
from models import *
from bll import *
class StudentManagerView:
    """
        学生管理器界面
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

    def __input_int(self,msg):
        while True:
            try:
                return int(input("请输入%s:"%(msg)))
            except:
                print("输入有误")
                continue
    def input_students(self):
        while True:
            if input("按y继续") == "y":
                stu = StudnetModel()
                stu.name = str(input("请输入姓名:"))
                stu.age = self.__input_int("年龄")
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