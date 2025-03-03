import numpy as np
import matplotlib.pyplot as plt

grad_size = 50
height = 400
width = 400

image = np.zeros((height, width, 3))
lows = np.arange(height) // grad_size
cols = np.arange(width) //grad_size
checkerboard = (lows[:, np.newaxis]+cols) % 2 == 0
image[checkerboard] = [1, 1, 1]
plt.imshow(image)
plt.show()

'''
# 定义格子大小
grid_size = 50

# 创建一个 2x2 的基础棋盘单元
base_pattern = np.array([[1, 0], [0, 1]], dtype=float)

# 使用 np.tile 函数重复基础单元
checkerboard = np.tile(base_pattern, (grid_size, grid_size))

# 将一维的棋盘扩展为三维的 RGB 图像
image = np.repeat(np.repeat(checkerboard[:, :, np.newaxis], 3, axis=2), grid_size, axis=0)
image = np.repeat(image, grid_size, axis=1)

# 显示图像
plt.imshow(image)
plt.axis('off')
plt.show()
'''
