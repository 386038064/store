'''
请编程统计列表中的每个数字出现的次数(百度初级测试开发笔试题)
List = [1,4,7,5,8,2,1,3,4,5,9,7,6,1,10]
'''
List = [1,4,7,5,8,2,1,3,4,5,9,7,6,1,10]
a=[]
#去重的简便方法：a=list(set(List))
# set(列表名) 顺序会变  输出不是列表要转换
#通过循环去重
for i in List:
    if i in a:
        continue
    a.append(i)
for i in range(len(a)):
    time=0
    num=a[i]
    for j in range(len(List)):
        if num == List[j]:
            time+=1
    print(num,"出现了",time,"次")