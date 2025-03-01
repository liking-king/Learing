import numpy as np
'''
shape:要生成的形状如果 shape 是一个整数，例如 3，np.full(3, 5) 输出: [5 5 5]，
shape:()里有多少个数就是多少维度np.full(3, 5,2)三维
fill_value:要填充的值
'''
# 1,创建一个3行4列的「温度计阵列」（所有元素为25.5）
temperature_matrix = np.full((3, 4), 25.5)
# 返回一个3行4列的一，在分别乘25.5
temperature_matrix1 = np.ones((3, 4))*25.5
# 返回一个3行4列的零，在分别加25.5
temperature_matrix2 = np.zeros((3, 4))+25.5

# 2,用np.linspace()创建从0到100的5个等距数值（类比5个均匀分布的温度计)
# np.linspace(start, stop, num)，start开始值，stop结束值，num平均分成多少份
temperature_points = np.linspace(0, 100, num=5)
