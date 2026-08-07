from pathlib import Path
import pandas as pd
import json


# 读取 CSV 文件
data = pd.read_csv(r"E:\python_work\AI-Summer-2026\week01-python\day05\student_scores_missing.csv", encoding="utf-8-sig")


# ============================================================
# 一、查看原始数据和缺失值
# ============================================================

print("原始数据：")
print(data)

print("\n缺失值的位置：")
print(data.isna())

print("\n每一列缺失值的数量：")
print(data.isna().sum())


# ============================================================
# 二、计算各科平均分
# ============================================================

math_mean = data["math"].mean()
english_mean = data["english"].mean()

print("\n数学平均分：", math_mean)
print("英语平均分：", english_mean)


# ============================================================
# 三、使用各科平均分填补缺失值
# ============================================================

data["math"] = data["math"].fillna(math_mean)
data["english"] = data["english"].fillna(english_mean)

# data = data.fillna({
#     "math": math_mean,
#     "english": english_mean
# })

print("\n填补缺失值后的数据：")
print(data)

print("\n清洗后每列缺失值数量：")
print(data.isna().sum())


# ============================================================
# 四、计算每个学生的总分和平均分
# ============================================================

data["total"] = data["math"] + data["english"]
data["average"] = data["total"] / 2

print("\n增加总分和平均分后的数据：")
print(data)


# ============================================================
# 五、查看统计信息
# ============================================================

print("\n各列统计信息：")
print(
    data[
        ["math", "english", "total", "average"]
    ].describe()
)


# ============================================================
# 六、保存清洗后的 CSV 文件
# ============================================================

output_path = Path(__file__).resolve().parent / "cleaned_scores.csv"

data.to_csv(
    output_path,
    index=False,
    encoding="utf-8-sig"
)

print("\n清洗后的数据保存成功！")
print("保存位置：", output_path)


# 找到平均分最高值所在的行号
best_index=data["average"].idxmax()

# 根据行号取出该学生的整行数据
best_student=data.loc[best_index]

# 整理要保存到JSON中的数据
summary_data = {
    "math_mean": float(data["math"].mean()),
    "english_mean": float(data["english"].mean()),
    "total_mean": float(data["total"].mean()),
    "average_mean": float(data["average"].mean()),

    "best_student": {
        "name": str(best_student["name"]),
        "math": float(best_student["math"]),
        "english": float(best_student["english"]),
        "total": float(best_student["total"]),
        "average": float(best_student["average"])
    }
}

# 设置JSON文件路径
json_path = Path(__file__).resolve().parent / "score_summary.json"

# 保存为JSON文件
with open(json_path, "w", encoding="utf-8") as file:
    json.dump(
        summary_data,
        file,
        ensure_ascii=False,
        indent=4
    )

print("\n统计结果保存成功！")
print("JSON文件位置：", json_path)

print("\n平均分最高学生：")
print(best_student)

raw_data = pd.read_csv(
    Path(__file__).resolve().parent / "student_scores_missing.csv",
    encoding="utf-8-sig"
)

print("\n原始数据行数：", len(raw_data))

# 检查指定行，若有缺失值，则删除整行
dropped_data = raw_data.dropna(
    subset=["math", "english"]
)

print("删除缺失值后的行数：", len(dropped_data))
print("\n删除缺失值后的数据：")
print(dropped_data)



