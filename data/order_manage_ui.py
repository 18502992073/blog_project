from data.order_manage import *

"""
    order_manage_ui.py(UI:user interface,用户接口)
    订单管理程序用户接口层（视图层，view）
    接收用户指令，显示执行结果
"""


class View:
    def __init__(self):
        self.__ordermanage = OrderManage()  # 订单管理对象，全局变量

    def print_menu(self):  # 打印主菜单
        menu = '''------订单管理程序------
        1 - 查询所有订单
        2 - 根据ID号查询订单
        3 - 新增订单
        4 - 修改订单
        5 - 删除订单
        其他 - 退出'''
        print(menu)

    def query_all(self):
        order_list = self.__ordermanage.query_all_order()
        for o in order_list:
            print(o)

    def select_by_id(self,id):
        order=self.__ordermanage.query_one_order(id)
        for o in order:
            print(o)

    def main(self):
        while 1:
            self.print_menu()
            oper = input("请选择要执行的操作")
            if oper == "1":  # 查询所有订单
                self.query_all()
            elif oper == "2":  # 根据ID号查询订单
                oper = input("请输入要查询的ID")
                self.select_by_id(oper)
            elif oper == "3":  # 新增订单
                pass
            elif oper == "4":  # 修改订单
                pass
            elif oper == "5":  # 删除订单
                pass
            else:  # 其他则退出
                break


