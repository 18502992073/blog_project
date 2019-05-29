for i in range(4):
    if i % 2 == 0:
        for j in range(5):
            print("*", end="")
    else:
        for j in range(5):
            print("#", end="")
    print()

for i in range(4):
    for j in range(i + 1):
        print("*", end="")
    print()

print()

for i in range(4):
    for m in range(i):
        print(" ", end="")
    for j in range(4 - i):
        print("*", end="")
    print()



