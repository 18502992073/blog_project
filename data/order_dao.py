from data.db_helper import *
from data.order import *

"""
    order_dao.py
    订单数据访问对象
    d:data a:access o:object
    拼装各种sql语句，调用DBHelper
    实现数据库的操作
"""


class OrderDao:
    def __init__(self):  # 构造函数
        self.__db_helper = DBHelper()  # 创建持有DBHelper对象
        self.__db_helper.open_conn()

    def __del__(self):  # 析构函数，对象销毁时调用
        self.__db_helper.close_conn()

    def query_all_order(self):  # 查询所有订单，返回订单对象列表
        sql = 'select * from orders'
        order_list = []  # 订单对象列表
        result = self.__db_helper.do_query(sql)
        if not result:
            print("查询结果为空")
            return None
        for row in result:
            order_id = row[0]
            cust_id = row[1]
            if row[4]:
                products_num = int(row[4])
            else:
                products_num = 0
            if row[5]:
                amt = float(row[5])
            else:
                amt = 0.00
            order_list.append(Order(order_id, cust_id, products_num, amt))
        return order_list  # 返回对象列表

    def query_one_order(self,id):
        order = []
        sql = 'select * from orders where order_id='+id
        result = self.__db_helper.do_query(sql)
        if not result:
            print("查询结果为空")
            return None
        order_id = result[0][0]
        cust_id = result[0][1]
        if result[0][4]:
            products_num = int(result[0][4])
        else:
            products_num = 0
        if result[0][5]:
            amt = float(result[0][5])
        else:
            amt = 0.00
        order.append(Order(order_id, cust_id, products_num, amt))
        return order


# 测试
if __name__ == '__main__':
    orderDao = OrderDao()
    order_list = orderDao.query_all_order()
    for o in order_list:
        print(o)