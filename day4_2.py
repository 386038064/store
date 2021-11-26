#求其中是5的倍数的和
a = [1,5,21,30,15,9,30,24]
_sum=0
for i in range(len(a)):
    if a[i]%5==0:
        _sum=_sum+a[i]
print(_sum)