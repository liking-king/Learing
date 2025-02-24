import numpy as np

vector = np.array([1, 2])
matrix = np.array([[1, 2, 3], [4, 5, 6]])

# 向量相加
sum_vector = vector + np.array([3, 4])
print(sum_vector)

# 矩阵相乘dot(A, B)A的列等于B的行
product_matrix = np.dot(matrix, np.array([[4, 4 , 4], [5, 5, 5], [3, 3, 3]]))
print(product_matrix)