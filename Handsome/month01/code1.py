def hanoi(n,left,right,middle):
    if n==1:
        print("%d:%s-->%s"%(n,left,right))
    else:
        hanoi(n-1,left,middle,right)
        print("%d:%s-->%s" % (n, left, right))
        hanoi(n-1,middle,right,left)

# hanoi(5,"A","C","B")



count=0
for i in ("a","b","c"):
    for j in ("a","b","c"):
        for k in ("a","b","c"):
            if i !=j and j !=k and i !=k:
                print("%c%c%c"%(i,j,k))
                count +=1
print(count)

