import numpy as np
import pandas as pd
from docutils.nodes import label
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt

# 模拟工地天气数据（降雨量, 风速, 是否停工）
data = {
    "降雨量(mm)": [5, 30, 15, 50, 10, 45, 25, 60],
    "风速(m/s)": [3, 12, 6, 18, 5, 15, 8, 20],
    "停工": [0, 1, 0, 1, 0, 1, 0, 1]
}
df = pd.DataFrame(data)

# 准备数据
X = df[["降雨量(mm)", "风速(m/s)"]]
y = df["停工"]

# 训练逻辑回归模型
model = LogisticRegression()
model.fit(X, y)

# 预测新天气下的停工概率
new_weather = np.array([[40, 16]])  # 降雨40mm，风速16m/s
prob = model.predict_proba(new_weather)[:, 1]  # 停工概率
print(f"停工概率: {prob[0]:.0%}")  # 示例输出：92.35%
# 可视化决策边界（选做）
# 代码参考昨日多元线性回归的网格生成方法
plt.rc('font', family='YouYuan')
plt.rcParams['axes.unicode_minus'] = False    # 修复负号显示

# 生成网格点数据（覆盖所有可能的降雨和风速范围）
x1_min, x1_max = df['降雨量(mm)'].min()-10, df['降雨量(mm)'].max()+10
x2_min, x2_max = df['风速(m/s)'].min()-5, df['风速(m/s)'].min()+5

xx, yy = np.meshgrid(np.linspace(x1_min, x1_max, 100),
                     np.linspace(x2_min, x2_max, 100))

# 预测网格点的停工概率
z = model.predict_proba(np.c_[xx.ravel(), yy.ravel()])[:, 1]
z = z.reshape(xx.shape)
# 绘制决策边界和散点图
plt.figure(figsize=(10, 6))
# 背景色表示停工概率（红色越深概率越高）
plt.contourf(xx, yy, z, levels=[0, 0.3, 1], alpha=0.3,
             colors=['green', 'red'])
# 原始数据点
plt.scatter(df['降雨量(mm)'][y==0], df['风速(m/s)'][y==0],
            c='green', edgecolors='k', label='正常施工')
plt.scatter(df['降雨量(mm)'][y==1], df['风速(m/s)'][y==1], c='red',
            marker='x', s=100, label='停工记录')
# 标注新数据点
plt.scatter(40, 16, c='blue', marker='x', s=200,
            label='预测点 (40mm, 16m/s)')

# 标签和标题
plt.xlabel('降雨量(mm)'), plt.ylabel('风速(m/s)')
plt.title('工地停工决策边界 (逻辑回归)')
plt.legend()
plt.colorbar(label='停工概率')
plt.grid(alpha=0.2)
plt.show()