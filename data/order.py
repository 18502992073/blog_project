"""
    order.py
    订单类：存放订单属性
"""


class Order:
    def __init__(self, order_id, cust_id, products_num, amt):
        self.__order_id = order_id
        self.__cust_id = cust_id
        self.__products_num = products_num
        self.__amt = amt

    def __str__(self):
        ret = "编号:%s,客户编号:%s,数量:%d,金额:%.2f" \
              % (self.__order_id, self.__cust_id, self.__products_num, self.__amt)
        return ret

    def __repr__(self):
        return "order(%s,'%s',%d,%.2f)" \
               % (self.__order_id, self.__cust_id, self.__products_num, self.__amt)
