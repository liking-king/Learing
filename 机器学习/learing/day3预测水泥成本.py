import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

'''用np创建数据,机器学习需要二维数组，所以要用reshape转换-1表示自动识别行数，1表示生成一列
题：预测水泥的成本
1，创建水泥数据
2，创建回归模型，并训练
3，输出模型参数，加载回归方程
4，预测输入水泥用量成本
5，画图显示
'''

# # 假设我们有历史数据：水泥用量（吨）和成本（万元）
# X = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)  # 水泥用量
# Y = np.array([5.1, 10.2, 15.1, 20.3, 25.2])  # 成本
#
# # 创建线性回归模型
# model = LinearRegression()
# model.fit(X, Y) #训练模型
#
# # 输出模型参数
# a = model.coef_[0] # 斜率
# b = model.intercept_ # 截距
# print(f'回归方程Y={a:.2f}*X + {b:.2f}')
#
# # 预测新的水泥用量对应的成本
# new_X = np.array([6]).reshape(-1, 1) # 预测6吨水泥的成本
# predicted_Y = model.predict(new_X)
# print(f'{predicted_Y[0]:.2f}')
#
# # 画图显示结果
# plt.rc('font', family='YouYuan') # 设置字体
# plt.scatter(X, Y, color='blue', label='历史数据') # 散布图
# plt.plot(X, model.predict(X), color='red', label='回归直线') # 画回归直线
# plt.xlabel('水泥用量（吨）')
# plt.ylabel('成本')
# plt.legend()
# plt.show()

"""
用线性回归预测施工60天的总成本。
修改代码，画出散点图和回归直线。
"""
X = np.array([10, 20, 30, 40, 50]).reshape(-1, 1)  # 施工天数
Y = np.array([15, 25, 35, 45, 55])  # 项目总成本（万元）

model = LinearRegression()
model.fit(X, Y)

a = model.coef_[0]
b = model.intercept_
print(f'线性方程：Y={a:.2f}*X+{b:.2f}')

new_X = np.array([60]).reshape(-1, 1)
predicted = model.predict(new_X)
print(f'60天的总成本:{predicted[0]:.2f}万元')

plt.rc('font', family='YouYuan')
plt.scatter(X, Y, color='blue', label='历史数据')
plt.plot(X, model.predict(X), color='red', label='回归直线')
plt.xlabel('施工天数（天）')
plt.ylabel('成本')
plt.legend()
plt.show()