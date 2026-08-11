# Day 7 学习笔记：学生成绩分析小项目

## 一、项目目标

使用 Python、Pandas 和 Matplotlib 完成一个学生成绩分析小项目。

主要流程：

```text
读取 CSV
→ 检查缺失值
→ 填补缺失值
→ 计算总分和平均分
→ 排名
→ 条件筛选
→ 查找最高/最低分
→ 各科统计汇总
→ 保存 CSV
→ 绘制并保存柱状图
```

## 二、读取 CSV

```python
import pandas as pd
from pathlib import Path

raw_data = pd.read_csv(
    Path(__file__).resolve().parent / "student_scores.csv",
    encoding="utf-8-sig"
)

print(raw_data)
print(raw_data.shape)
print(raw_data.isna().sum())
```

## 三、填补缺失值

```python
math_mean = raw_data["math"].mean()
english_mean = raw_data["english"].mean()

raw_data["math"] = raw_data["math"].fillna(math_mean)
raw_data["english"] = raw_data["english"].fillna(english_mean)
```

## 四、计算总分和平均分

```python
raw_data["total"] = (
    raw_data["math"]
    + raw_data["english"]
    + raw_data["python"]
)

raw_data["average"] = raw_data["total"] / 3
```

## 五、排序与排名

```python
ranking = raw_data.sort_values(
    by="average",
    ascending=False
)

ranking["rank"] = range(1, len(ranking) + 1)
```

## 六、取前三名

```python
top3 = ranking.head(3)
print(top3[["rank", "name", "average"]])
```

## 七、条件筛选

平均分低于 85：

```python
low_score_students = raw_data[
    raw_data["average"] < 85
]
```

数学和英语都不低于 85：

```python
high_score_students = raw_data[
    (raw_data["math"] >= 85)
    & (raw_data["english"] >= 85)
]
```

记住：

```text
&  并且
|  或者
~  取反
```

## 八、区间筛选

```python
students_85_90 = raw_data[
    raw_data["average"].between(85, 90)
]
```

`between(85, 90)` 默认包含两端。

## 九、统计人数

```python
high_students = raw_data[
    raw_data["average"] >= 90
]

print(len(high_students))
```

## 十、查找最高分和最低分

```python
best_index = raw_data["math"].idxmax()
best_student = raw_data.loc[best_index]

low_index = raw_data["python"].idxmin()
low_student = raw_data.loc[low_index]
```

记忆：

```text
idxmax()：最大值所在行号
idxmin()：最小值所在行号
loc[]：按行号取数据
```

## 十一、各科统计汇总

```python
summary = pd.DataFrame({
    "subject": ["math", "english", "python"],
    "mean": [
        raw_data["math"].mean(),
        raw_data["english"].mean(),
        raw_data["python"].mean()
    ],
    "max": [
        raw_data["math"].max(),
        raw_data["english"].max(),
        raw_data["python"].max()
    ],
    "min": [
        raw_data["math"].min(),
        raw_data["english"].min(),
        raw_data["python"].min()
    ]
})
```

## 十二、保存 CSV

```python
summary_path = Path(__file__).resolve().parent / "subject_summary.csv"

summary.to_csv(
    summary_path,
    index=False,
    encoding="utf-8-sig"
)
```

排名结果：

```python
ranking_path = Path(__file__).resolve().parent / "ranking.csv"

ranking.to_csv(
    ranking_path,
    index=False,
    encoding="utf-8-sig"
)
```

## 十三、Matplotlib 柱状图

```python
import matplotlib.pyplot as plt

bars = plt.bar(
    summary["subject"],
    summary["mean"]
)

plt.xlabel("Subject")
plt.ylabel("Average Score")
plt.title("Average Score by Subject")

plt.bar_label(bars, fmt="%.2f")
```

## 十四、保存图片

```python
figure_path = Path(__file__).resolve().parent / "average_scores.png"

plt.savefig(
    figure_path,
    dpi=300,
    bbox_inches="tight"
)

plt.show()
```

## 十五、今天最重要的 Pandas 思路

```text
需要筛选 → 布尔条件
需要排序 → sort_values()
需要前几名 → head()
需要最高分 → idxmax()
需要最低分 → idxmin()
需要取整行 → loc[]
需要保存 → to_csv()
需要画图 → matplotlib
```

当前阶段不要求把所有 API 背下来，重点是能根据任务想到应该用哪一类工具。
