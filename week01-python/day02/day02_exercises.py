# 第一题：计算矩形面积和周长
# ###########################
# chang=float(input("请输入长："))
# kuan=float(input("请输入宽："))
# print("面积=",chang*kuan)
# print("周长=",2*(chang+kuan))


# # 第二题，输入一个数判断它的奇偶性

# a=float(input("请输入一个数："))
# if a%2==0:
#     print("该数是偶数")
# else:
#     print("该数是奇数")
    
# # 第三题，找出最大的数
# a=float(input("输入第一个数："))
# b=float(input("输入第二个数："))
# c=float(input("输入第三个数："))
# print("最大数是：",max(a,b,c))

# # 第四题，输出1-100能被3整除的数
# for i in range(1,101):
#     if i%3==0:
#         print(i)


# # 第五题，输出1-100的整数和
# sum=0
# for i in range(1,101):
#     sum=sum+i;
# print(sum)

# # 第六题，统计字符串中字母a出现的次数
# sum=0;
# string=input("请输入字符串：")
# for len in string:
#     if(len=='a'):
#         sum=sum+1
# print("a出现了",sum,"次")

# # 第七题，删除列表中重复的元素
# numbers=[1,2,2,21,1,2,13,466,78,8954,3,1,1,1,1,1]

# # print(set(numbers))
# newnumber=[]
# for i in numbers:
#     if i not in newnumber:
#         newnumber.append(i)

# print("原来的列表:",numbers)
# print("去重的列表：",newnumber)      



# # 第八题，字典保存三个学生成绩，并计算平均成绩
# students={
#     "张三":89,
#     "李四":99,
#     "王二":81
# }
# sum=0;
# for value in students.values():
#     sum=sum+value
# print("平均成绩：",sum/len(students))



# # 第九题，输出九九乘法表
# for i in range(1,10):
#     for j in range(1,i+1):
#             print(j,"*",i,"=",i*j,end="\t");
#     print(" ")        



# 第十题，输入成绩以及统计及格与不及格成绩人数

count=int(input("请输入需要输入成绩的总人数："))
pass_count=0
fail_count=0
for i in range(1,count+1):
    score=float(input(f"请输入第{i}个学生成绩："))
    if score>=60:
        pass_count=pass_count+1
    else:
        fail_count=fail_count+1
print("总人数：",count)
print("及格人数:",pass_count)        
print("不及格人数：",fail_count)
