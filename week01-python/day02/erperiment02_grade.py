score=float(input("请输入成绩："))
if score<0 or score>100:
    print("成绩必须在0~100之间")
elif score>=90:
    print("优秀")
elif score>=80:
    print("良好")
elif score>=60:
    print("及格")
else:
    print("不及格")


