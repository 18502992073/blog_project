打印正三角形
length = int(input("输入一个正整数"))
i = 1
while i <= length:
    print(" "*(length-i)+"*"*i)
    i += 1


length= int(input("输入一个正整数"))
i = 0
while i < length:
    print(" "*i+"*"*(length-i))
    i += 1


length = int(input("输入一个正整数"))
i = 0
while i < length:
    print("*"*(length-i)+" "*i)
    i += 1


num1 = int(input("输入一个数"))
num2 = int(input("输入一个数"))
num3 = int(input("输入一个数"))
if num1 > num2:
    num1, num2 = num2, num1
if num1 > num3:
    num1, num3 = num3, num1
if num2 > num3:
    num2, num3 = num3, num2
print(num1, num2, num3)

result=0
for i in range(1,100):
    if i % 2 ==1:
        result += i
    else:
        result -=i
print(result)

result=0
i=0
while i< 100:
    if i % 2 ==1:
        result += i
        i +=1
    else:
        result -=i
        i+=1
print(result)

result=0                    #i=0
for i in range (1,10):      #while i<10:
    result +=int("8"*i)
    print(int("8"*i))
print(result)


