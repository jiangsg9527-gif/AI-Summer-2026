import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt

raw_data = pd.read_csv(
    Path(__file__).resolve().parent / "student_scores.csv",
    encoding="utf-8-sig"
)

print(raw_data)
print(raw_data.shape)
print(raw_data.isna().sum())

math_mean = raw_data["math"].mean()
english_mean = raw_data["english"].mean()
raw_data["math"] = raw_data["math"].fillna(math_mean)
raw_data["english"] = raw_data["english"].fillna(english_mean)

raw_data["total"] = raw_data["math"] + raw_data["english"]+raw_data["python"]
raw_data["average"] = raw_data["total"] / 3

print("\n增加总分和平均分后的数据：")
print(raw_data)

ranking=raw_data.sort_values(

    by="average",
    ascending=False
)
ranking["rank"]=range(1,len(ranking)+1)

ranking_path = Path(__file__).resolve().parent / "ranking.csv"

ranking.to_csv(
    ranking_path,
    index=False,
    encoding="utf-8-sig"
)

print("\n排名结果保存成功！")
print("保存位置：", ranking_path)

print("\n学生平均分排名：")
print(ranking[["rank","name", "average"]])

top3=ranking.head(3)
print("\n前三名学生：")
print(top3[["rank","name","average"]])
print(type(top3))

print(raw_data["average"]<85)

low_score_students=raw_data[raw_data["average"]<85] 
   

print("\n平均分低于85分的学生：")
print(low_score_students[["name","average"]])

high_score_students=raw_data[(raw_data["math"]>=85) & (raw_data["english"]>=85)]      

# &并且 |或者 ~取反  
print("\n数学与英语同时大于85分学生：")
print(high_score_students[["name","math","english"]])

average_85_90=raw_data[(raw_data["average"]>85)&(raw_data["average"]<=90)]

print(average_85_90[["name","average"]])

AA=raw_data[raw_data["average"].between(85,90)]
print(AA[["name","average"]])


high_students=raw_data[(raw_data["average"]>=90)]
print("平均分大于或等于90分的学生人数：",len(high_students))


low_index=raw_data["python"].idxmin()
low_student=raw_data.loc[low_index]

print("python最低分：",low_student["python"])
print("学生：",low_student["name"])

math_mean=raw_data["math"].mean()
math_max=raw_data["math"].max()
math_min=raw_data["math"].min()

english_mean = raw_data["english"].mean()
english_max = raw_data["english"].max()
english_min = raw_data["english"].min()

python_mean = raw_data["python"].mean()
python_max = raw_data["python"].max()
python_min = raw_data["python"].min()


summary = pd.DataFrame({
    "subject": ["math", "english", "python"],
    "mean": [math_mean, english_mean, python_mean],
    "max": [math_max, english_max, python_max],
    "min": [math_min, english_min, python_min]
})

print("\n各科统计汇总：")
print(summary)


summary_path = Path(__file__).resolve().parent / "subject_summary.csv"

summary.to_csv(
    summary_path,
    index=False,
    encoding="utf-8-sig"
)

print("\n各科统计汇总保存成功！")
print("保存位置：", summary_path)



bars = plt.bar(summary["subject"], summary["mean"])

plt.xlabel("Subject")
plt.ylabel("Average Score")
plt.title("Average Score by Subject")
plt.bar_label(bars, fmt="%.2f")

figure_path = Path(__file__).resolve().parent / "average_scores.png"

plt.savefig( figure_path, dpi=300, bbox_inches="tight")
   
plt.show()


