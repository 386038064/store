import random
shop=[
    # 0     1
    ["酱油",20],#0
    ["醋",15],#1
    ["腊肠",50],#2
    ["卫龙",5.5],
    ["电饭煲",299],
    ["威猛先生",60],
    ["软华子",70],#抽烟
    ["鸡蛋面",10]
]
mycar=[]#购物车
money=1000#初始化钱包

zhekou=random.randint(1,31)
if zhekou>=1 and zhekou<=10:
    print("恭喜获得辣条3折优惠券")
elif zhekou>=11 and zhekou<=30:
    print("恭喜获得威猛先生9折优惠券")
else:
    print("恭喜获得免单优惠卷")

# 枚举
while True:
    for i in enumerate(shop):#列举商品
        print(i)
    o=input("请选择商品")#str  转换成int类型
    # 一个元素在某一个容器里面：
    if o.isdigit():#.isdigit判读字符串内是不是由数字组成
        o=int(o)#把str转换成int
        if o <len(shop):#判断输入的范围
            if money>shop[o][1]:#钱够不够
                mycar.append(shop[o])#加入购物车
                money=money-shop[o][1]#减钱
                print("此商品已经加入购物车，您的余额为：",money)
            else:print("穷鬼，gun")
        else:print("请输入正确的商品编号")
    elif o =="q" or o=="Q":#输入内容退出并打印小条
        print("再见,以下是您购买的商品")
        for i in enumerate(mycar):
            print(i)
        break
    else:print("您输入的有误")
cost=0
if  zhekou == 31:
    cost=0
    print("恭喜你获得免单优惠")
elif zhekou>=11 and zhekou<=30:
    print("恭喜获得威猛先生就这优惠券")
    for i in range(len(mycar)):
        if mycar[i][0] == "威猛先生":
            cost=mycar[i][1]*0.8*0.9+cost
        else:
            cost=cost+mycar[i][1]*0.8
else:
    print("恭喜获得卫龙三折优惠券")
    for i in range(len(mycar)):
        if mycar[i][0] == "卫龙":
            cost=mycar[i][1]*0.8*0.3+cost
        else:
            cost=cost+mycar[i][1]*0.8
print("您需花费了",cost,"元")