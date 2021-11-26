'''
请编程实现列表的数据翻转
简便方式
python中反转列表的三种方式
1、内建函数reversed()
    li =[1, 2, 3, 4, 5, 6]
    a = list(reversed(li))
    print (a)
注意：reversed()函数返回的是一个迭代器，而不是一个List，所以需要list函数转换一下
2、内建函数sorted()
sorted()语法
    sorted(iterable[, cmp[, key[, reverse]]])
参数说明：
iterable -- 可迭代对象。
cmp -- 比较的函数，这个具有两个参数，参数的值都是从可迭代对象中取出，此函数必须遵守的规则为，大于则返回1，小于则返回-1，等于则返回0。
key -- 主要是用来进行比较的元素，只有一个参数，具体的函数的参数就是取自于可迭代对象中，指定可迭代对象中的一个元素来进行排序。
reverse -- 排序规则，reverse = True 降序 ， reverse = False 升序（默认）。
返回值
返回重新排序的列表。
    a=[1,2,3,4,5,6,7,8,9]
    c=sorted(a, reverse=True)
    print (c)
注意：sorted()按降序排列，对于反转内容不是顺序排列的无效果，此处待改善。
3: 使用分片
    a=[1,2,3,4,5,6,7,8,9]
    d=a[::-1]
    print （d） 　
    注意：其中[::-1]代表从后向前取值，每次步进值为1
'''
List = [1,2,3,4,5,6,7,8,9]
temp=0
for i in range(len(List)//2):
    temp=List[len(List)-i-1]
    List[len(List)-i-1]=List[i]
    List[i]=temp
print(List)
