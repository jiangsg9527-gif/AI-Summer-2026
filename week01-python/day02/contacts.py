contacts={
    "张三":{
        "phone":"11112431234",
        "email":"zhangshan@exampal.com"
    },
    "李四":{
        "phone":"19287652345",
        "email":"lisi@example.com"
    },
    "王二":{
        "phone":"12219198976",
        "email":"wanger@example.com"
    }

}

while True:
    print("==========通讯录管理系统===========")
    print("1.添加联系人")
    print("2.查询联系人")
    print("3.修改联系人")
    print("4.删除联系人")
    print("5.显示全部联系人")
    print("0.退出程序")
    print("=================================")

    choice=input("选择操作编号：")


# 1添加联系人
    if choice=="1":
        name=input("请输入需要添加联系人的姓名:")
        if name in contacts:
            print("该联系人已存在！")
        else:
            phone=input("请输入电话号码：")
            email=input("请输入邮箱：")
            contacts[name]={
                "phone":phone,
                "email":email
            }
            print("联系人添加成功！")
# 2查询联系人
    elif choice=="2":
        name=input("请输入要查询联系人的姓名：")
        if name in contacts:
            print("姓名：",name)
            print("电话：",contacts[name]["phone"])
            print("邮箱：",contacts[name]["email"])
        else:
            print("没有找到该联系人！")

# 3修改联系人
    elif choice=="3":
        name=input("请输入要修改联系人的姓名：")
        if name in contacts:
            new_phone=input("输入新的电话号码：")
            new_email=input("输入新的邮箱：")
            contacts[name]["phone"]=new_phone
            contacts[name]["email"]=new_email
            print("修改成功！")
        else:
            print("没有找到该联系人，无法修改。")

# 4删除联系人
    elif choice=="4":
        name=input("请输入要删除联系人的姓名：")
        if name in contacts:
            del contacts[name]
            print("删除成功！")
        else:
            print("不存在该联系人，无法删除")

# 5显示全部联系人
    elif choice=="5":
        for name,information in contacts.items():
            print("姓名：",name)
            print("电话：",information["phone"])
            print("邮箱：",information["email"])
            print("-------------------------")
    elif choice=="0":
        break
    else: 
        print("请输入0~5之间的序号！")
