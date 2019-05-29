import time
# print(time.time())
# print(time.localtime())
# print(time.strftime("%Y.%m.%d/%H:%M:%C",time.localtime()))
# print(time.strptime("2019.3.20/17:33","%Y.%m.%d/%H:%M"))

T=input("%Y.%m.%d")
T=time.strptime(T,"%Y.%m.%d")
print("星期",T[6]+1)
t=T.tm_wday
print("星期",t+1)
