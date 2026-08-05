def calculate_score(score1,score2,score3):
    if not(0<=score1<=100 and 0<=score2<=100 and 0<=score3<=100):
        raise ValueError("成绩只能在0~100之间！")
    total=score1+score2+score3
    average=total/3
    return total,average


try:
    score1=float(input("请输入第一个成绩："))
    score2=float(input("请输入第二个成绩："))
    score3=float(input("请输入第三个成绩："))
    total,average=calculate_score(score1,score2,score3)
    print("总成绩：",total)
    print("平均成绩：",average)

except ValueError as error:
    print("输入错误：",error)
