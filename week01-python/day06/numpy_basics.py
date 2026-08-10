import numpy as np

# a=np.array([1,2,3,4])

# print(a)
# print(type(a))
# print(a.shape)

b=np.array([[1,2,3],
            [4,5,6]])
print(b.shape)

print(b[0,1])

# 取整行,以下两种都是取第一（从0开始）
print(b[0])
print(b[0,:])

# 取整列
print(b[:,1])

print(b[1,0])  #4
print(b[0,2])
print(b[1,:])
print(b[:,2])

#切片
print(b[0:2,0:2])
print(b[0:2,1:3])



print(b*2)
print(b-1)
print(b**2)#平方


#广播
print(b**2)
c=np.array([10,20,30])
print(b+c)
d=np.array([[10],
            [20]])
print(d)
print(b+d)


A=np.array([[1,2],
            [3,4]])
B=np.array([[5,6],
            [7,8]])
print(A*B)#对应位置相乘
print(A@B)#矩阵乘法

C=np.array([[1,2],
            [3,4],
            [5,6]])
print(C.shape)
print(C.T)  #矩阵转置
print(C.T.shape)

##NumPy随机数
import numpy as np
random_number=np.random.rand(5)#生成0-1的随机数
print(random_number)

random_matrix=np.random.rand(2,3)
print(random_matrix)
print(random_matrix.shape)

numbers=np.random.randint(1,10,size=5)#从1-9中生成随机整数
print(numbers)


random_a=np.random.rand(6)
random_b=np.random.randint(1,101,size=(3,4))
print(random_a)
print(random_b)

A=np.array([
    [1,2],
    [3,4]
])
B=np.array([
    [5,6],
    [7,8]
])

def matrix_add(A,B):
    return A+B

C=matrix_add(A,B)
print(C)


A=np.array([
    [1,2,3],
    [4,5,6]
])
def  matrix_transpose(A):
    return A.T
B=matrix_transpose(A)
print(B)

def matrix_multiply(A,B):
    return A@B

A=np.array([
    [1,2],
    [3,4]
])
B=np.array([
    [5,6],
    [7,8]
])
print(matrix_multiply(A,B))


A=np.array([
    [1,2,3],
    [1,2,3]
])

B=np.array([
    [1,2],
    [2,3],
    [4,5]
])
print(A.shape)
print(B.shape)
print(A@B)
print((A@B).shape)

# reshape()改变数组形状

a=np.array([1,2,3,4,5,6])
b=a.reshape(3,2)
print(a)
print(b)
