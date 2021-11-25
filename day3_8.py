a=int(input("请决定打印几乘几乘法表"))
i=1

while i<(a+1):
    j=1
    while j<(i+1):
        print(j,"x",i,"=",i*j," ",end="")
        j+=1
    print()
    i+=1
