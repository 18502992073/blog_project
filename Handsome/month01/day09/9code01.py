"""
实参传递方式
    位置传参
        序列传参
    关键字传参
        字典传参
"""
def fun1(a,b,c):
    print("a=",a)
    print("b=",b)
    print("c=",c)
#位置传参：实参与形参的位置依次相对应.
# fun1(1,2,3)


#序列传参：实参用*将序列拆解后与形参的位置依次对应
# fun1(*{2:1,"b":"s","c":"d"})
# fun1(*{1,2,6})


#关键字传参：实参根据形参的名字进行对应.
# fun1(c=1,b=2,a="a")

#字典传参：实参用**将字典拆解与形参的名字进行对应.
# fun1(**{"b":1,"a":"s","c":"d"})



#缺省(默认)参数
def fun2(a=0,b=0,c=0):
    print("a=",a)
    print("b=",b)
    print("c=",c)

# fun2(*(3,2,3))

# def transform_to_second(min=0,hour=0,days=0):
#     result=days*24*60*60+hour*60*60+min*60
#     return result
#
# print(transform_to_second(hour=1),"s")

def fun6(a,b,*,c,d):
    print(a,b,c,d)



fun6(c=1,d=2,b=1,a=3)





