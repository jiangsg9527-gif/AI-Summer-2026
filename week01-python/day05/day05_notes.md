# Day 5 学习笔记：文件读写与 Pandas 数据清洗

## 一、今天学习了什么

今天主要学习：

- TXT 文件读写
- CSV 文件读写
- JSON 文件保存
- `pathlib.Path` 路径处理
- Pandas 基础
- `DataFrame` 和 `Series`
- 缺失值检测
- `fillna()` 填补缺失值
- `dropna()` 删除缺失值
- 统计量计算
- 新增列
- 查找平均分最高学生
- 保存清洗后的 CSV
- 保存统计结果为 JSON

## 二、TXT 文件读写

写入：

```python
with open("message.txt", "w", encoding="utf-8") as file:
    file.write("今天学习文件读写。\n")
```

读取：

```python
with open("message.txt", "r", encoding="utf-8") as file:
    content = file.read()
```

其中：

```text
"w"：写入模式
"r"：读取模式
```

`with open(...)` 使用结束后会自动关闭文件。

## 三、Path 路径工具

导入：

```python
from pathlib import Path
```

获取当前 Python 文件所在目录：

```python
current_folder = Path(__file__).resolve().parent
```

拼接文件路径：

```python
csv_path = current_folder / "student_scores.csv"
```

也可以一行读取：

```python
data = pd.read_csv(
    Path(__file__).resolve().parent / "student_scores.csv",
    encoding="utf-8-sig"
)
```

## 四、Pandas 基础

导入：

```python
import pandas as pd
```

读取 CSV：

```python
data = pd.read_csv("student_scores.csv", encoding="utf-8-sig")
```

`data` 是一个 `DataFrame`，可以理解为 Python 中的表格。

常用查看方式：

```python
print(data)
print(data.shape)
print(data.columns)
print(data.head(2))
```

## 五、选择列

选择一列：

```python
math_scores = data["math"]
```

选择多列：

```python
selected = data[["name", "math"]]
```

一列通常是 `Series`，整张表是 `DataFrame`。

## 六、统计函数

```python
data["math"].mean()
data["math"].max()
data["math"].min()
data["math"].sum()
```

分别表示：

```text
mean()：平均值
max()：最大值
min()：最小值
sum()：总和
```

## 七、缺失值

缺失值通常显示为：

```text
NaN
```

检查缺失值：

```python
data.isna()
```

统计每一列缺失数量：

```python
data.isna().sum()
```

其中：

```text
True：缺失
False：有数据
```

## 八、fillna() 填补缺失值

先计算平均值：

```python
math_mean = data["math"].mean()
english_mean = data["english"].mean()
```

填补：

```python
data["math"] = data["math"].fillna(math_mean)
data["english"] = data["english"].fillna(english_mean)
```

含义：

```text
只把指定列中的 NaN 替换为平均值；
原来存在的数据不变。
```

也可以写：

```python
data = data.fillna({
    "math": math_mean,
    "english": english_mean
})
```

## 九、dropna() 删除缺失值

删除含缺失值的行：

```python
dropped_data = raw_data.dropna()
```

只检查指定列：

```python
dropped_data = raw_data.dropna(
    subset=["math", "english"]
)
```

记忆：

```text
fillna：补
dropna：删
```

## 十、增加总分和平均分

```python
data["total"] = data["math"] + data["english"]
data["average"] = data["total"] / 2
```

Pandas 会自动逐行计算。

## 十一、describe() 查看统计信息

```python
print(
    data[
        ["math", "english", "total", "average"]
    ].describe()
)
```

`describe()` 会给出：

```text
count：数量
mean：平均值
std：标准差
min：最小值
25%：第一四分位数
50%：中位数
75%：第三四分位数
max：最大值
```

## 十二、找到平均分最高学生

先找最大值所在行号：

```python
best_index = data["average"].idxmax()
```

再取整行：

```python
best_student = data.loc[best_index]
```

也可以直接写：

```python
best_student = data.loc[data["average"].idxmax()]
```

## 十三、保存清洗后的 CSV

```python
output_path = Path(__file__).resolve().parent / "cleaned_scores.csv"

data.to_csv(
    output_path,
    index=False,
    encoding="utf-8-sig"
)
```

其中：

```text
index=False：不保存左侧行号
utf-8-sig：减少中文乱码
```

## 十四、保存统计结果为 JSON

先整理成字典：

```python
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
```

保存：

```python
json_path = Path(__file__).resolve().parent / "score_summary.json"

with open(json_path, "w", encoding="utf-8") as file:
    json.dump(
        summary_data,
        file,
        ensure_ascii=False,
        indent=4
    )
```

记忆：

```text
to_csv()：保存表格
json.dump()：保存字典
```

## 十五、Day 5 完整流程

```text
读取原始 CSV
→ 查看数据
→ 检查缺失值
→ 计算各科平均值
→ 用 fillna() 填补缺失值
→ 计算总分和平均分
→ 查看统计信息
→ 找平均分最高学生
→ 保存 cleaned_scores.csv
→ 保存 score_summary.json
→ 用 dropna() 对比删除缺失值的效果
```

## 十六、今天需要记住的核心语句

```python
pd.read_csv(...)
data["列名"]
data.isna().sum()
data["math"].fillna(math_mean)
data.dropna()
data["total"] = ...
data.describe()
data.loc[data["average"].idxmax()]
data.to_csv(...)
json.dump(...)
```

## 十七、当前阶段要求

目前不要求完全记住所有 Pandas 写法。

达到这些目标即可：

1. 知道 CSV 可以用 Pandas 读取成 DataFrame；
2. 会选择列；
3. 会检查缺失值；
4. 会用 `fillna()` 和 `dropna()`；
5. 会新增总分和平均分列；
6. 会保存清洗后的 CSV；
7. 会把统计结果保存到 JSON。
