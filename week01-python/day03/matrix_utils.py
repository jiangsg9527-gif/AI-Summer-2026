def matrix_add(matrix_a,matrix_b):
    check_matrix(matrix_a) 
    if len(matrix_a)!=len(matrix_b):
        raise ValueError("两个矩阵的行数不同，不能相加！")
    if len(matrix_a[0])!=len(matrix_b[0]):
        raise ValueError("两个矩阵的列数不同，不能相加！")
    result=[]
    for i in range(0,len(matrix_a)):
        new_row=[]
        for j in range(0,len(matrix_a[0])):
            value=matrix_a[i][j]+matrix_b[i][j]
            new_row.append(value)
        result.append(new_row)
    return result


# matrix_a=[
#     [1,2],
#     [3,4]
# ]
# matrix_b=[
#     [2,3],
#     [3,6]
# ]
# try:
#     result=matrix_add(matrix_a,matrix_b)
#     print("矩阵相加结果：")
#     for row in result:
#         print(row)
# except ValueError as error:
#     print("矩阵运算错误：",error)


def matrix_transpose(matrix):
    check_matrix(matrix)
    
    result=[]
    for j in range(len(matrix[0])):
        row=[]
        for i in range(len(matrix)):
            value=matrix[i][j]
            row.append(value)
        result.append(row)
    return result


# matrix=[
#         [1,2,3],
#         [3,4,5],
        
#     ]   
# try:
#     result=matrix_transpose(matrix)
#     print("矩阵转置结果：")
#     for row in result:
#         print(row)

# except ValueError as error:
#     print("矩阵运算错误：",error)



# 矩阵乘法

def matrix_multiply(matrix_a, matrix_b):

    check_matrix(matrix_a)
    check_matrix(matrix_b)
    # 判断A的列数是否等于B的行数
    if len(matrix_a[0]) != len(matrix_b):
        raise ValueError("第一个矩阵的列数必须等于第二个矩阵的行数！")

    result = []

    # 遍历结果矩阵的每一行
    for i in range(len(matrix_a)):
        new_row = []

        # 遍历结果矩阵的每一列
        for j in range(len(matrix_b[0])):
            value = 0

            # 将A的一行和B的一列对应相乘并累加
            for k in range(len(matrix_a[0])):
                value = value + matrix_a[i][k] * matrix_b[k][j]

            new_row.append(value)

        result.append(new_row)

    return result

# matrix_a = [
#     [1, 2, 3],
#     [4, 5, 6]
# ]

# matrix_b = [
#     [7, 8],
#     [9, 10],
#     [11, 12]
# ]

# matrix_a = [
#     [1, 2, 3],
#     [4, 5, 6]
# ]

# matrix_b = [
#     [1, 2],
#     [3, 4]
# ]

# try:
#     result = matrix_multiply(matrix_a, matrix_b)

#     print("矩阵乘法结果：")

#     for row in result:
#         print(row)

# except ValueError as error:
#     print("矩阵运算错误：", error)


def check_matrix(matrix):
    if len(matrix) == 0:
        raise ValueError("矩阵不能为空！")

    if len(matrix[0]) == 0:
        raise ValueError("矩阵的行不能为空！")

    column_count = len(matrix[0])

    for row in matrix:
        if len(row) != column_count:
            raise ValueError("矩阵每一行的长度必须相同！")

if __name__ == "__main__":
    matrix_a = [
        [1, 2, 3],
        [4, 5, 6]
    ]

    matrix_b = [
        [7, 8, 9],
        [10, 11, 12]
    ]

    matrix_c = [
        [7, 8],
        [9, 10],
        [11, 12]
    ]

    try:
        print("矩阵加法：")
        result_add = matrix_add(matrix_a, matrix_b)

        for row in result_add:
            print(row)

        print("\n矩阵转置：")
        result_transpose = matrix_transpose(matrix_a)

        for row in result_transpose:
            print(row)

        print("\n矩阵乘法：")
        result_multiply = matrix_multiply(matrix_a, matrix_c)

        for row in result_multiply:
            print(row)

    except ValueError as error:
        print("矩阵运算错误：", error)

