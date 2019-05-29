"""
    学生系统管理器逻辑
"""
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