class Student:
    def __init__(self, id, name, score):
        self.id = id
        self.name = name
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
    def score(self):
        return self.__score

    @score.setter
    def score(self, value):
        self.__score = value

    def print_self(self):
        print(self.id, self.name, self.score)


def get_student_by_id(list_stu, stu_id):
    for item in list_stu:
        if item.id == stu_id:
            return item


list_stu = [
    Student("106", "zs", 85),
    Student("102", "ls", 90),
    Student("105", "xm", 80),
    Student("104", "xh", 95),
    Student("101", "qw", 98),
    Student("103", "fr", 76),
    Student("107", "ly", 99),
    Student("104", "qw", 89)
]
stu = get_student_by_id(list_stu, "03")
if stu != None:
    stu.print_self()
else:
    print("无")


def get_student_by_score(list_stu, stu_score):
    list_result = []
    for item in list_stu:
        if item.score >= stu_score:
            list_result.append(item)
    return list_result


stu = get_student_by_score(list_stu, 90)
for item in stu:
    print(item.id, item.name, item.score)


def get_max_score_student(list_stu):
    max = list_stu[0]
    for c in range(1, len(list_stu)):
        if max.score < list_stu[c].score:
            max = list_stu[c]
    return max


stu = get_max_score_student(list_stu)
print(stu.score)


# 查找id最小的学生
def get_min_id_student(list_stu):
    min = list_stu[0]
    for i in range(1, len(list_stu)):
        if min.id > list_stu[i].id:
            min = list_stu[i]
    return min


stu = get_min_id_student(list_stu)
print(stu.id)


# 在列表中查找指定姓名的学生(同名学生全部查找)
def get_students_by_name(list_stu, stu_name):
    list_result = [item for item in list_stu if item.name == stu_name]
    return list_result


stu = get_students_by_name(list_stu, "qw")
for i in stu:
    i.print_self()


#将学生列表按照成绩按降序排列
def scort_student_by_score(list_stu):
    for i in range(len(list_stu)-1):
        for j in range(i+1,len(list_stu)):
            if list_stu[i].score<list_stu[j].score:
                list_stu[i],list_stu[j]=list_stu[j],list_stu[i]
scort_student_by_score(list_stu)
for i in list_stu:
    i.print_self()