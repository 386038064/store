import random
user_sys={}
#添加用户模块（传入参数：用户的所有信息（字典）。返回值：整型值（1：成功，2：用户已存在，3：用户库已满））
def user_add(new_user):#参数格式new_user={"姓名":"name","密码":"六位数字","地址":"地址","开户行":"开户行"}
    time=0
    if len(user_sys)>=100:
        time=3
    if new_user["姓名"] in user_sys:
        time=2
    if time == 0:
        time = 1
        user_sys.update({new_user["姓名"]:new_user})
    return time
        # elif new_user["姓名"] in user_sys[i]["姓名"]:
#根据手动输入信息生成用户字典，并自动生成用户ID
def user_input():
    ID=str(random.randint(10000000,99999999))
    while True:#本循环作用为让随机的ID不重复
        ID_xiangtong=0
        for i in user_sys:
            if ID == user_sys[i]["账号"]:
                ID=str(random.randint(10000000,99999999))
                ID_xiangtong+=1
        if ID_xiangtong == 0:
            break
    new_user={
        "账号":ID,
        "姓名":input("请输入姓名"),
        "密码":input("请输入六位数字"),
        "地址":{
            "国家":input("请输入国家"),
            "省份":input("请输入省份"),
            "街道":input("请输入街道"),
            "门牌号":input("请输入门牌号"),
                },
        "余额":0,
        "开户行":"中国工商银行"
    }
    return new_user
#存钱模块（传入值：用户的账号、存取的金额。返回值：布尔类型值）
def save_money(user_ID,money_save):
    user_name='0'
    for i in user_sys:
        if user_ID == user_sys[i]["账号"]:
            user_name=i
    if user_name != '0':
        user_sys[user_name]["余额"]+=money_save
        print('余额为',user_sys[user_name]["余额"])
        return True
    else:
        return False
#取钱（传入值：用户的账号，用户密码，取钱金额。返回值：整型值（0：正常，1：账号不存在，2：密码不对，3：钱不够））
def out_money(user_ID,user_password,out_money):
    user_name='0'
    for i in user_sys:
        if user_ID == user_sys[i]["账号"]:
            user_name=i
    if user_name == '0':
        return 1
    else:
        if user_password != user_sys[user_name]["密码"]:
            return 2
        else:
            if out_money > user_sys[user_name]["余额"]:
                return 3
            else:
                user_sys[user_name]["余额"]-=money_out
                print('余额为',user_sys[user_name]["余额"])
                return 0
#转账（传入值：转出的账号，转入的账号，转出账号的密码，转出的金额。返回值：0：正常，1：账号不对，2密码不对，3钱不够）
def transfer_money(ID_out,ID_enter,password_out,money_out):
    user_name_out='0'
    user_name_enter='0'
    for i in user_sys:
        if ID_out == user_sys[i]["账号"]:
            user_name_out=i
    for i in user_sys:
        if ID_enter == user_sys[i]["账号"]:
            user_name_enter=i
    if user_name_out == '0' or user_name_out == '0':
        return 1
    elif password_out != user_sys[user_name_out]["密码"]:
        return 2
    elif money_out>user_sys[user_name_out]["余额"]:
        return 3
    else:
        user_sys[user_name_out]["余额"]-=money_out
        user_sys[user_name_enter]["余额"]+=money_out
        print('您的余额为',user_sys[user_name_out]["余额"])
        return 0
#查询账户功能（传入值：账号，账号密码，返回值：空）
def check_user(user_ID,password):
    user_name='0'
    for i in user_sys:
        if user_ID == user_sys[i]["账号"]:
            user_name=i
    if user_name == '0':
        print('该用户不存在')
    elif password != user_sys[user_name]["密码"]:
        print('密码输入错误')
    else:
        mould='''
当前账号：%s
密码：%s
余额：%s
用户居住地址：%s %s %s %s
当前账户开户行：中国工商银行
        '''
        print(mould % (user_sys[user_name]["账号"],user_sys[user_name]["密码"],user_sys[user_name]["余额"],new_user["地址"]["国家"],new_user["地址"]["省份"],new_user["地址"]["街道"],new_user["地址"]["门牌号"]))


print("*******************************************")
print("*           中国工商银行                  *")
print("*           账户管理系统                  *")
print("*             v1.0                        *")
print("*******************************************")
print("*1.开户")
print("*2.存钱")
print("*3.取钱")
print("*4.转账")
print("*5.查询")
print("*6.Bye！")
while True:
    a=int(input("请输入操作编号"))
    result=0
    if a == 1:
        new_user=user_input()
        result=user_add(new_user)
        if result == 1:
            print("开户成功")
            info='''
该账户信息为
*账号：  %s
*用户名：%s
*密码：  ******
*地址：  %s %s %s %s
*余额：  %s
*开户行：中国工商银行
            '''
            print(info % (new_user["账号"],new_user["姓名"],new_user["地址"]["国家"],new_user["地址"]["省份"],new_user["地址"]["街道"],new_user["地址"]["门牌号"],new_user["余额"]))
        elif result == 2:
            print("用户名已存在请更换用户名再次输入")
        else:
            print("数据库已满")

    elif a == 2:
        user_ID=input("请输入要存钱的账户账号")
        money_save=int(input("请输入要存入的钱数"))
        result=save_money(user_ID,money_save)
        if result == 0:
            print("账号不存在")
        else:
            print("存钱成功")

    elif a == 3:
        user_ID=input("请输入取款账户账号")
        password=input("请输入用户密码")
        money_out=int(input("请输入要取钱的数量"))
        result=out_money(user_ID,password,money_out)
        if result == 0:
            print("取钱成功")
        elif result == 1:
            print("用户不存在")
        elif result == 2:
            print("密码输入错误")
        else:
            print("钱不够")

    elif a == 4:
        out_ID=input('请输入转出户的账号')
        out_password=input('请输入转出户的密码')
        enter_ID=input('请输入转入户的账号')
        money_out=int(input('请输入转账金额'))
        result=transfer_money(out_ID,enter_ID,out_password,money_out)
        if result == 0:
            print('转账成功')
        elif result == 1:
            print('账号不对')
        elif result == 2:
            print('密码输入错误')
        else:
            print('钱不够')

    elif a == 5:
        user_ID=input('请输入用户账号')
        user_password=input('请输入用户密码')
        check_user(user_ID,user_password)

    elif a == 6:
        break
    else:
        print("请输入正确的操作编号")
