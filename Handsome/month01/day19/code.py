# tuple1=("悟空","八戒","唐僧","白龙马","沙僧","女儿国国王")
# iterator=tuple1.__iter__()
# while True:
#     try:
#         print(iterator.__next__())
#     except StopIteration:
#         break
#
# dic={"悟空":2000,"八戒":3000,"唐僧":1000,"沙僧":2700}
# iterator=iter(dic)
# while True:
#     try:
#         key=next(iterator)
#         print((key,dic[key]))
#     except StopIteration:
#         break
#
# iterator=dic.__iter__()
# while True:
#     try:
#         key=iterator.__next__()
#         print((key,dic[key]))
#     except StopIteration:
#         break

# class MyIterator:
#     def __init__(self,target):
#         self.target=target
#         self.index=0
#     def __next__(self):
#         if self.index>= self.target:
#             raise StopIteration
#         item=self.index
#         self.index +=1
#         return item
#
# class MyRange:
#     def __init__(self,target):
#         self.target=target
#
#     def __iter__(self):
#         iterator=MyIterator(self.target)
#         return iterator
#
# try:
#     for i in MyRange(5):
#         print(i)
# except:
#     pass
# ran=MyRange(5)
# iterator=ran.__iter__()
# while True:
#     try:
#         print(iterator.__next__())
#     except:
#         break

# class MyRange:
#     def __init__(self,stop):
#         self.stop=stop
#
#     def __iter__(self):
#         for i in range(self.stop):
#             yield i


def my_enumerate(list1):
    start=0
    for i in range(len(list1)):
        yield (start,list1[start])
        start +=1
    # while start<len(list1):
    #     result=(start,list1[start])
    #     yield result
    #     start +=1
lis=["a","b","c","d"]
# for i in my_enumerate(lis):
#     print(i)

def my_zip(lis,lis2,lis3):
    index=0
    for i in range(len(lis)):
        yield (lis[index],lis2[-index-1],lis3[index])
        index +=1
lis2=["A","B","C","D"]
lis3=["!","@","#","$"]
for i in my_zip(lis,lis2,lis3):
    print(i)









