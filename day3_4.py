'''
从键盘输入任意三边，判断是否能形成三角形，若可以，则判断形成什么三角形
（结果判断：等腰，等边，直角，普通，不能形成三角形。）
'''
print("请输入三个数")
a=int(input("请输入第一个数"))
b=int(input("请输入第二个数"))
c=int(input("请输入第三个数"))
if a+b>c and a+c>b and b+c>a:
    print("这三个数能形成三角形")
    if a==b and b==c:
        print("结果判断：等边")
    elif a==b or b==c or a==c:
        print("结果判断：等腰")
    elif a*a+b*b==c*c or b*b+c*c==a*a or a*a+c*c==b*b:
        print("结果判断：直角")
    else:
        print("判断结果：普通")
else:
    print("这三个数不能形成三角形")