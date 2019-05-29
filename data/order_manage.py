from data.order_dao import *

"""
    order_manage.py
    订单管理类（业务逻辑层/控制层）
    处理跟订单相关的逻辑操作，调用DAO来实现数据存取
"""


class OrderManage:
    def __init__(self):
        self.order_dao = OrderDao() #实例化对象

    def query_all_order(self):  #查询所有订单
        #做业务逻辑方面处理，但此处不需要做
        return self.order_dao.query_all_order()

    def query_one_order(self,id):
        return self.order_dao.query_one_order(id)
