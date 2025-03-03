import numpy as np
import matplotlib.pyplot as plt

# 用数组画一个「国际象棋棋盘」（提示：利用切片设置黑白块）
height = 500
weight = 500
grad_size = 50
# 创建一个500x500像素的全零三维矩阵
image = np.zeros((height, weight, 3), float)
# 循坏0-height步长为grad_size的数
for i in range(0, height, grad_size):
    # i每循坏一次j就要循坏完，j循坏完i又循坏一次，j又要循坏完
    for j in range(0, weight, grad_size):
        # 当循坏一次i=0，j=0，下面=(0//50+0//50)%2=0%2=0
        if (i//grad_size+j//grad_size) % 2 == 0:
            # image[行=0:0+50,列=0:0+50]表示image的0行到49行，0列到49列都表示白色[1,1,1]
            image[i:i+grad_size, j:j+grad_size] = [1, 1, 1]
        else:
            image[i:i+grad_size, j:j+grad_size] = [0, 0, 0]
plt.imshow(image)
plt.show()