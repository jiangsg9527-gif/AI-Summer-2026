# Day 6 学习笔记：NumPy 基础与矩阵运算

## 一、今天学习了什么

今天主要学习了：

- 创建一维、二维 NumPy 数组
- `shape` 查看数组形状
- 二维数组索引与切片
- 数组整体运算与广播 broadcasting
- `*` 对应元素相乘
- `@` 矩阵乘法
- `.T` 矩阵转置
- 随机数
- `reshape()` 改变数组形状
- 用 NumPy 重写 Day 3 的矩阵函数

## 二、创建 NumPy 数组

```python
import numpy as np
```

一维数组：

```python
a = np.array([1, 2, 3, 4])
```

二维数组：

```python
b = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
```

## 三、查看数组形状

```python
print(a.shape)
print(b.shape)
```

例如：

```text
a.shape = (4,)
b.shape = (2, 3)
```

`(2, 3)` 表示 2 行 3 列。

## 四、二维数组索引

```python
b[行, 列]
```

例如：

```python
b[1, 0]
```

表示第 1 行、第 0 列。NumPy 下标从 0 开始。

## 五、切片

取整行：

```python
b[1, :]
```

取整列：

```python
b[:, 2]
```

取部分区域：

```python
b[0:2, 1:3]
```

切片的结束位置不包含。

## 六、数组整体运算

```python
b + 10
b - 1
b * 2
b ** 2
```

`**` 表示乘方。

注意：

```python
b ** 2
```

表示平方，而：

```python
b ^ 2
```

不是平方，`^` 是按位异或。

## 七、广播 Broadcasting

```python
b = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

c = np.array([10, 20, 30])

print(b + c)
```

NumPy 会在形状可以匹配时，自动扩展较小数组再进行运算。

再例如：

```python
d = np.array([
    [10],
    [20]
])

print(b + d)
```

## 八、`*` 和 `@` 的区别

对应元素相乘：

```python
A * B
```

矩阵乘法：

```python
A @ B
```

## 九、矩阵乘法形状规则

```text
(m, n) @ (n, p) → (m, p)
```

中间两个维度必须相同。

例如：

```text
(2, 3) @ (3, 2) → (2, 2)
```

## 十、矩阵转置

```python
A.T
```

如果：

```text
A.shape = (2, 3)
```

那么：

```text
A.T.shape = (3, 2)
```

## 十一、随机数

0 到 1 之间的随机小数：

```python
np.random.rand(6)
```

随机整数：

```python
np.random.randint(1, 101, size=(3, 4))
```

表示生成一个 3×4 的矩阵，元素范围是 1～100。右端 101 不包含。

## 十二、reshape()

```python
a = np.array([1, 2, 3, 4, 5, 6])

b = a.reshape(3, 2)
```

结果：

```text
[[1 2]
 [3 4]
 [5 6]]
```

元素总数不能改变。

## 十三、用 NumPy 重写 Day 3 矩阵函数

```python
def matrix_add(A, B):
    return A + B

def matrix_transpose(A):
    return A.T

def matrix_multiply(A, B):
    return A @ B
```

Day 3 中需要自己写循环，而 NumPy 可以直接完成矩阵运算。

## 十四、今天最需要记住的内容

```python
np.array(...)
A.shape
A[行, 列]
A[:, 1]
A + 1
A * B
A @ B
A.T
A.reshape(...)
np.random.rand(...)
np.random.randint(...)
```

其中最重要：

```text
*   对应元素相乘
@   矩阵乘法
```

## 十五、当前阶段要求

现阶段不要求完全默写所有 NumPy API。

重点是：

1. 能看懂数组的 `shape`
2. 能进行基本索引和切片
3. 能理解简单广播
4. 能区分 `*` 和 `@`
5. 会使用 `.T` 和 `reshape()`
6. 能用 NumPy 完成基础矩阵运算
