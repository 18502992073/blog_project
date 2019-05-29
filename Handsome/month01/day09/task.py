"""
定义数值累加函数
"""
def sum_number(*args):
    result=0
    for item in args:
        result +=item
    return result

sum_number(2,3,4,5,6,7,8,9)





