import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression

data = {
    "降雨量(mm)": [35, 50, 15, 60],
    "风速(m/s)": [10, 18, 8, 25],
    '温度(℃)':[28, 22,35, 19],
    "停工": [0, 1, 0, 1]
}

df = pd.DataFrame(data)
# 使用逻辑回归模型，选择 3个关键特征（温度+降雨+风速）预测停工概率
X = df[['降雨量(mm)', "风速(m/s)", '温度(℃)']]
Y = df['停工']

model = LogisticRegression()
model.fit(X, Y)

# 输出模型系数
coef_df = pd.DataFrame({
    "特征":X.columns,
    "系数":model.coef_[0],
    "影响方向": np.where(model.coef_[0]>0, "增加工程风险", "降低工程风险")
})
print(f'回归系数分析:\n', coef_df)
print(f'截距项(基础风险):{model.intercept_[0]:.2f}')

# 若明日预报天气：降雨45mm，风速20m/s，温度25℃
new_weather = np.array([[45, 20, 25]])
predicted = model.predict_proba(new_weather)[:, 1]
print(f'停工的概率为:{predicted[0]:.0%}')
