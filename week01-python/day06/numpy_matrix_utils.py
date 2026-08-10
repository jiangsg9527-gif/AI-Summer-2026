import numpy as np

def matrix_add(A,B):
    return A+B

def matrix_transpose(A):
    return A.T

def matrix_multyply(A,B):
    return A@B

if __name__=="__main__":
    A=np.array([
        [1,2],
        [2,3]
    ])

    B=np.array([
        [4,3],
        [7,8]
    ])
    print("矩阵加法：")
    print(matrix_add(A,B))
    print("\n矩阵转置：")
    print(matrix_transpose(A))
    print("\n矩阵乘法：")
    print(matrix_multyply(A,B))


