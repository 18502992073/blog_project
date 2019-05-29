"""
    技能(编号、名称、法力消耗、冷却时间)
    1.	查找指定编号的技能
    2.	查找法力消耗大于10的所有技能
---------------------------------------
    3.	查找技能冷却时间最小的技能
    4.	根据法力消耗降序排列
    5.	删除冷却时间大于10的技能
"""
from common.list_tools import ListHelper


class SkillData:
    def __init__(self, id=0, name="", cost_sp=0, cool_time=0):
        self.id = id
        self.name = name
        self.cost_sp = cost_sp
        self.cool_time = cool_time

    @property
    def cool_time(self):
        return self.__cool_time

    @cool_time.setter
    def cool_time(self, value):
        self.__cool_time = value

    @property
    def cost_sp(self):
        return self.__cost_sp

    @cost_sp.setter
    def cost_sp(self, value):
        self.__cost_sp = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    def print_self(self):
        print(self.id, self.name, self.cost_sp, self.cool_time,end=" / ")


list_skill = [
    SkillData(101, "惩戒", 15, 30),
    SkillData(102, "闪现", 20, 2),
    SkillData(103, "点燃", 1, 80),
    SkillData(104, "净化", 25, 10),
    SkillData(105, "治疗", 10, 20)
]

ListHelper.find_one(list_skill, lambda s: s.id == 102).print_self()
print()

for item in ListHelper.find_all(list_skill,lambda s:s.cost_sp>10):
    item.print_self()
print()

ListHelper.get_min_value(list_skill, lambda s: s.cool_time).print_self()
print()

for item in ListHelper.order_by_down(list_skill,lambda s:s.cost_sp):
    item.print_self()
print()

for item in ListHelper.delete(list_skill,lambda s:s.cool_time>10):
    item.print_self()


