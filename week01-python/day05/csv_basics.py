import csv
from pathlib import Path


# 获取当前Python文件所在的文件夹
current_folder = Path(__file__).resolve().parent

# 设置CSV文件路径
csv_path = current_folder / "student_scores.csv"


# 准备要写入的数据
students = [
    ["name", "math", "english"],
    ["小明", 85, 90],
    ["小红", 92, 88],
    ["小刚", 78, 80]
]


# 写入CSV文件
with open(csv_path, "w", newline="", encoding="utf-8-sig") as file:
    writer = csv.writer(file)

    for row in students:
        writer.writerow(row)

print("CSV文件写入成功！")
print("文件保存位置：", csv_path)


# 读取CSV文件
with open(csv_path, "r", encoding="utf-8-sig") as file:
    reader = csv.reader(file)

    print("\nCSV文件内容：")

    for row in reader:
        print(row)