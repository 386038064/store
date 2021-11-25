name="root"
password="admin"
i=0
while i<3:
    password_input=input("请输入密码")
    if password != password_input:
        i=i+1
    else:
        print("输入正确")
        break
    if i==3:
        print("输入错误三次，系统锁定")