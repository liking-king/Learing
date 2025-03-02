import numpy as np
# 计算BMI指数，体重（kg）/身高（m）^2
height = np.array([1.70, 1.73, 1.75, 1.80])
weight = np.array([60, 62, 65, 70])
# 身高里面的数值分别2次方，算出结果后，体重里的数值对应除身高算出来的结果
BMI = weight / height**2
for i in BMI:
    # round改变小数点后的位数，2代表保留两位
    # print(round(i, 2))
    pass

matrix = np.array([[10,20],
                   [30,40]])
# print(matrix)
vector = np.array([[3, 4],[1,2]])
# print(vector)
matrix_of_vector = matrix@vector
# print(matrix_of_vector)
'''
# 矩阵乘法用@，或np.dot() *代表元素相乘
matrix@vector =[10 20] [3 4] =[x y]
               [30 40] [1 2]  [z t]
x(第一行第一列)=matrix第一行*vector第一列[10 20] [3]=50                
                                             [1]

z(第二行第一列)=matrix第二行*vector第一列[30 40] [3]= 130               
                                             [1]  
'''