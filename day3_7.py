'''
print(1,end="")可以不换行输出
'''
a=int(input("请决定三角形一共几行"))

for i in range(a):
    j=0
    print(" "*(a-1-i),end="")
    while j<(2*(i+1)-1):
        if (j+1)%2!=0:
            print("*",end="")
        else:
            print(" ",end="")
        j+=1
    print()