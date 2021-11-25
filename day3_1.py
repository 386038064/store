'''
实现输入10个数字，并打印10个数的求和结果
'''
num=[]
i=0
while i<10:
    num.append(int(input("在这输入")))
    i=i+1
a=0
for i in range(len(num)):
    a=a+num[i]
print(a)
