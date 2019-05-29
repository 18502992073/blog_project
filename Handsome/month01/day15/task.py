"""
一家公司有如下几种岗位，
程序员：底薪 + 项目分红
软件测试：底薪 + Bug数 * 5
销售：底薪 + 销售额*5%
定义员工管理器，记录所有员工，计算所有员工的总薪资。
要求：增加新的岗位，员工管理器满足开闭原则。
     画出架构图，写出体现依赖倒置原则、开闭原则的点
"""
class StaffManagement:
    def __init__(self):
        self.list_staffs=[]
    def add_staff(self,staff):
        self.list_staffs.append(staff)
    def get_total_money(self):
        sum=0
        for item in self.list_staffs:
            sum +=item.get_salary()
        return sum
class Job:
    def __init__(self,name,basic_pay):
        self.name = name
        self.basic_pay = basic_pay
    # @property
    # def basic_pay(self):
    #     return self.basic_pay


    def get_salary(self):
        raise NotImplementedError()

class Programmer(Job):
    def __init__(self,name,basic_pay,distribution):
        super().__init__(name,basic_pay)
        self.basic_pay=3000
        self.distribution = distribution
    def get_salary(self):
        return int(self.basic_pay)+int(self.distribution)

class SoftwareTest(Job):
    def __init__(self,name,basic_pay,number_bug):
        super().__init__(name,basic_pay)
        self.basic_pay=2500
        self.number_bug = number_bug
    def get_salary(self):
        return int(self.basic_pay)+int(self.number_bug)*5

class Sell(Job):
    def __init__(self,name,basic_pay,sale_money):
        super().__init__(name,basic_pay)
        self.basic_pay=2000
        self.sale_money = sale_money
    def get_salary(self):
        return int(self.basic_pay)+int(self.sale_money)*0.05

maneger=StaffManagement()
p1=Programmer("ZS"," ",8000)
maneger.add_staff(p1)
t1=SoftwareTest("ls",2500,250)
maneger.add_staff(t1)
s1=Sell("zt",1500,100000)
maneger.add_staff(s1)
print(maneger.get_total_money())
for i in maneger.list_staffs:
    print(i.basic_pay)









