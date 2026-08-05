from matrix_utils import matrix_add
from matrix_utils import matrix_transpose
from matrix_utils import matrix_multiply


matrix_a = [
    [1, 2],
    [3, 4]
]

matrix_b = [
    [5, 6],
    [7, 8]
]


print("调用导入的矩阵加法函数：")

result_add = matrix_add(matrix_a, matrix_b)

for row in result_add:
    print(row)


print("\n调用导入的矩阵转置函数：")

result_transpose = matrix_transpose(matrix_a)

for row in result_transpose:
    print(row)


print("\n调用导入的矩阵乘法函数：")

result_multiply = matrix_multiply(matrix_a, matrix_b)

for row in result_multiply:
    print(row)