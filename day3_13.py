'''
用循环来实现20以内的数的阶乘。（1! +2!+3!+…..+20!）
'''
a=20
num=[None]*a
for i in range(a):
    num[i]=i+1
print(num)
_rusult=0#用来储存最后结果

for i in range(len(num)):
    _factorial=1#阶乘
    for j in range(i+1):
        _factorial=_factorial*num[j]
        _rusult=_rusult+_factorial
print("结果为",_rusult)

