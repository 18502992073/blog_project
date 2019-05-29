import os

print("**********")
a = 1
pid = os.fork()

if pid < 0:
    print("create process failed")
elif pid == 0:
    print("a = ",a)
    a = 10000
    print("the new process")
else:
    print("a:",a)
    print("the old process")
print("fork test over")
