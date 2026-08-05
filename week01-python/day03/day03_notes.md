# Day 3 学习笔记：函数、异常处理与矩阵工具

## 一、函数基础

### 1. 定义函数

```python
def 函数名(参数):
    函数内部代码
    return 返回结果
```

示例：

```python
def calculate_score(score1, score2, score3):
    total = score1 + score2 + score3
    average = total / 3
    return total, average
```

调用函数：

```python
total, average = calculate_score(80, 90, 70)
```

### 2. 形参与实参

定义函数时的参数叫形参：

```python
def add(a, b):
    return a + b
```

调用函数时传入的数据叫实参：

```python
result = add(10, 20)
```

### 3. `return` 与 `print` 的区别

- `print()`：只把内容显示在屏幕上。
- `return`：把结果返回给调用函数的程序，结果还可以继续参与计算。

```python
def add(a, b):
    return a + b

result = add(2, 3)
print(result)
```

函数可以一次返回多个结果：

```python
return total, average
```

接收时顺序要一致：

```python
total, average = calculate_score(...)
```

---

## 二、作用域

函数内部创建的变量叫局部变量，只能在函数内部使用。

```python
def test():
    number = 10
    print(number)
```

函数需要的数据最好通过参数传入，计算结果通过 `return` 返回，尽量不要依赖全局变量。

---

## 三、异常处理

### 1. `try-except`

可能出错的代码放在 `try` 中，出错后的处理代码放在 `except` 中。

```python
try:
    score = float(input("请输入成绩："))
except ValueError as error:
    print("输入错误：", error)
```

### 2. `raise`

`raise` 用于主动产生错误。

```python
if not 0 <= score <= 100:
    raise ValueError("成绩只能在0～100之间！")
```

完整示例：

```python
def calculate_score(score1, score2, score3):
    if not (
        0 <= score1 <= 100
        and 0 <= score2 <= 100
        and 0 <= score3 <= 100
    ):
        raise ValueError("成绩只能在0～100之间！")

    total = score1 + score2 + score3
    average = total / 3
    return total, average
```

注意：一次 `input()` 默认读取一整行。下面这句一次只能输入一个数字：

```python
score1 = float(input("请输入第一个成绩："))
```

输入 `120 90 11` 会转换失败，因为它不是一个单独的浮点数。

---

## 四、Python 中的矩阵表示

Python 可以使用嵌套列表表示矩阵：

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
```

其中：

```python
len(matrix)       # 行数
len(matrix[0])    # 列数
matrix[i][j]      # 第 i 行第 j 列的元素
```

Python 下标从 `0` 开始。

---

## 五、矩阵合法性检查

矩阵运算前需要检查：

1. 矩阵不能为空；
2. 矩阵中的行不能为空；
3. 每一行的长度必须相同。

```python
def check_matrix(matrix):
    if len(matrix) == 0:
        raise ValueError("矩阵不能为空！")

    if len(matrix[0]) == 0:
        raise ValueError("矩阵的行不能为空！")

    column_count = len(matrix[0])

    for row in matrix:
        if len(row) != column_count:
            raise ValueError("矩阵每一行的长度必须相同！")
```

---

## 六、矩阵加法

两个矩阵只有在行数和列数都相同时才能相加。

```python
def matrix_add(matrix_a, matrix_b):
    check_matrix(matrix_a)
    check_matrix(matrix_b)

    if len(matrix_a) != len(matrix_b):
        raise ValueError("两个矩阵的行数不同，不能相加！")

    if len(matrix_a[0]) != len(matrix_b[0]):
        raise ValueError("两个矩阵的列数不同，不能相加！")

    result = []

    for i in range(len(matrix_a)):
        new_row = []

        for j in range(len(matrix_a[0])):
            value = matrix_a[i][j] + matrix_b[i][j]
            new_row.append(value)

        result.append(new_row)

    return result
```

注意：`result = []` 是空列表，不能直接写：

```python
result[i][j] = value
```

必须先用 `append()` 创建元素。

---

## 七、矩阵转置

矩阵转置就是把原矩阵的行和列交换。

原矩阵：

```text
1  2  3
4  5  6
```

转置后：

```text
1  4
2  5
3  6
```

代码：

```python
def matrix_transpose(matrix):
    check_matrix(matrix)

    result = []

    for j in range(len(matrix[0])):
        new_row = []

        for i in range(len(matrix)):
            new_row.append(matrix[i][j])

        result.append(new_row)

    return result
```

外层循环遍历原矩阵的列，内层循环遍历原矩阵的行。

---

## 八、矩阵乘法

矩阵 `A` 和矩阵 `B` 能够相乘的条件是：

```text
A 的列数 = B 的行数
```

若 `A` 是 `m×n`，`B` 是 `n×p`，结果就是 `m×p`。

```python
def matrix_multiply(matrix_a, matrix_b):
    check_matrix(matrix_a)
    check_matrix(matrix_b)

    if len(matrix_a[0]) != len(matrix_b):
        raise ValueError(
            "第一个矩阵的列数必须等于第二个矩阵的行数！"
        )

    result = []

    for i in range(len(matrix_a)):
        new_row = []

        for j in range(len(matrix_b[0])):
            value = 0

            for k in range(len(matrix_a[0])):
                value = value + matrix_a[i][k] * matrix_b[k][j]

            new_row.append(value)

        result.append(new_row)

    return result
```

三个循环变量的含义：

- `i`：结果矩阵的行；
- `j`：结果矩阵的列；
- `k`：A 的一行和 B 的一列中对应元素的位置。

核心计算：

```python
value = value + matrix_a[i][k] * matrix_b[k][j]
```

---

## 九、`if __name__ == "__main__":`

可以把它理解为：

> 只有直接运行当前文件时，才执行下面的测试代码。

```python
if __name__ == "__main__":
    # 测试代码
```

直接运行：

```powershell
python matrix_utils.py
```

测试代码会执行。

在其他文件中导入：

```python
from matrix_utils import matrix_add
```

只会导入函数，不会自动执行 `if __name__ == "__main__":` 下面的测试代码。

因此，一个工具文件通常这样组织：

```python
def 工具函数1():
    pass

def 工具函数2():
    pass

if __name__ == "__main__":
    # 只用于测试
    pass
```

---

## 十、今天遇到的典型错误

### 1. 错误地同时判断三个成绩

错误写法：

```python
(score1 and score2 and score3) >= 0
```

正确写法：

```python
0 <= score1 <= 100 and 0 <= score2 <= 100 and 0 <= score3 <= 100
```

### 2. `try` 后面的代码没有缩进

正确结构：

```python
try:
    # 缩进代码
except ValueError as error:
    # 缩进代码
```

### 3. 给空列表中不存在的位置赋值

错误写法：

```python
result = []
result[0][0] = 1
```

正确做法：

```python
result = []
row = []
row.append(1)
result.append(row)
```

### 4. 转置时行列循环范围写反

转置应该使用：

```python
for j in range(len(matrix[0])):
    for i in range(len(matrix)):
        value = matrix[i][j]
```

---

## 十一、Day 3 完成内容

- 掌握函数定义与调用；
- 理解参数、返回值和多个返回值；
- 理解 `return` 与 `print` 的区别；
- 初步理解局部变量和作用域；
- 掌握 `try-except` 和 `raise`；
- 不使用 NumPy 实现矩阵加法；
- 不使用 NumPy 实现矩阵转置；
- 不使用 NumPy 实现矩阵乘法；
- 增加空矩阵、不规则矩阵和维度错误检查；
- 使用 `if __name__ == "__main__":` 分离工具函数和测试代码。

## 十二、建议目录

```text
week01-python/
└── day03/
    ├── function_basics.py
    ├── matrix_utils.py
    ├── test_matrix_import.py
    └── day03_notes.md
```
