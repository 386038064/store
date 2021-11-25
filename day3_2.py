'''
从键盘依次输入10个数，最后打印最大的数、10个数的和、和平均数。
'''
print("请输入10个数")
num = []
i = 0
while i < 10:
    num.append(int(input("在这输入")))
    i = i + 1
num_sum=0#数组之和
for i in range(len(num)):
    num_sum =num_sum + num[i]
num_max = 0#数组最大值
for i in range(len(num)):
    if num_max < num[i]:
        num_max = num[i]
average=num_sum / 10
print("最大的数为",num_max)
print("10个数的和为",num_sum)
print("平均数为",average)