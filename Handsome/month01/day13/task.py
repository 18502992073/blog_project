"""
定义技能数据类(技能编号，技能名称，消耗法力，冷却时间)
作业1：在技能数据列表中，查找指定名称的技能对象。
作业2：查找冷却时间大于5的所有技能对象。
作业3：查找技能数据列表中，消耗法力最小的技能。
作业4：查找技能数据列表中，冷却时间最大的技能。
作业5：根据冷却时间，对技能列表进行升序(小到大)排列。
"""


class SkillData:
    __slots__ = ("__id", "__name", "__cost_sp", "__cool_time", "__animation_name")

    def __init__(self, id=0, name="", cost_sp=0, cool_time=0, animation_name=""):
        self.id = id
        self.name = name
        self.cost_sp = cost_sp
        self.cool_time = cool_time
        self.animation_name = animation_name

    @property
    def animation_name(self):
        return self.__animation_name

    @animation_name.setter
    def animation_name(self, value):
        self.__animation_name = value

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
        print(self.id, self.name, self.cost_sp, self.cool_time)


skill_list = [
    SkillData(1, "降龙十八掌", 80, 20),
    SkillData(2, "冰冻", 50, 15),
    SkillData(3, "乾坤大挪移", 60, 10),
    SkillData(4, "禁锢", 20, 5),
    SkillData(5, "九阴白骨爪", 70, 2)
]


# 作业1：在技能数据列表中，查找指定名称的技能对象。
def get_skill_by_name(skill_list, name):
    for item in skill_list:
        if item.name == name:
            return item


sk = get_skill_by_name(skill_list, "禁锢")
sk.print_self()


# 作业2：查找冷却时间大于5的所有技能对象。
def get_skill_by_cool_time(skill_list, time):
    result = [item for item in skill_list if item.cool_time > time]
    return result


sk = get_skill_by_cool_time(skill_list, 5)
for i in sk:
    i.print_self()


# 作业3：查找技能数据列表中，消耗法力最小的技能。
def get_min_cost_sp(skill_list):
    min = skill_list[0]
    for i in range(1, len(skill_list)):
        if min.cost_sp > skill_list[i].cost_sp:
            min = skill_list[i]
    return min


sk = get_min_cost_sp(skill_list)
sk.print_self()


# 作业4：查找技能数据列表中，冷却时间最大的技能。
def get_max_cool_time(skill_list):
    max = skill_list[0]
    for item in skill_list:
        if max.cool_time < item.cool_time:
            max = item
    return item


sk = get_max_cool_time(skill_list)
sk.print_self()


#作业5：根据冷却时间，对技能列表进行升序(小到大)排列。
def order_by_cool_time(skill_list):
    for i in range(len(skill_list)-1):
        for j in range(i+1,len(skill_list)):
            if skill_list[i].cool_time>skill_list[j].cool_time:
                skill_list[i],skill_list[j]=skill_list[j],skill_list[i]
order_by_cool_time(skill_list)
for i in skill_list:
    i.print_self()


