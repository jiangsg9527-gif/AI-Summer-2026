from pathlib import Path
import pandas as pd


# 获取当前Python文件所在的文件夹
current_folder = Path(__file__).resolve().parent

# 拼接CSV文件路径
csv_path = current_folder / "student_scores.csv"

# 使用Pandas读取CSV文件
data = pd.read_csv(csv_path, encoding="utf-8-sig")


print("完整表格：")
print(data)

print("\n数据类型：")
print(type(data))

print("\n表格的行数和列数：")
print(data.shape)

print("\n所有列名：")
print(data.columns)

print("\n前两行数据：")
print(data.head(2))

print("\n数学成绩这一列：")
math_scores = data["math"]
print(math_scores)

print("\n数学平均分：")
print(math_scores.mean())

print("\n数学最高分：")
print(math_scores.max())

print("\n数学最低分：")
print(math_scores.min())

print("\n数学成绩总和：")
print(math_scores.sum())