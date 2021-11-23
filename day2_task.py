import random#随机生成数字 （开始int，结束int）
print("猜数字游戏规则：随机一个数，当每猜对就再随机一个数。")
print("且开局有3000分，每次猜对就给300，猜错就扣除200，当猜错15回的时候就game over")
life=3000
i=0
while i<15:
    a=0
    Ran = random.randint(1,20)
    while 1:
        num=input("猜个数吧╮(╯▽╰)╭：")
        # 键盘输入
        num=int(num)
        if num == Ran:
            print("猜对了_(:з」∠)_")
            life=life+300
            break
        elif num > Ran:
            print("再猜小点哟(￣︶￣)ψ")
            life=life-200
            i=i+1
        else:
            print("再猜大点哟(￣︶￣)ψ")
            life=life-200
            i=i+1
        a=a+1
        if i==15:
            break
    print("还剩下",life)
print("游戏结束，还剩",life)