import numpy as np
from sklearn.linear_model import LinearRegression

X = np.array([[300, 20,  350, 15],[400, 10, 320, 18]]).reshape(-1, 2)

Y = np.array([35.2, 40.1, 45.8, 38.5])

model = LinearRegression()
model.fit(X, Y)

a1, a2 = model.coef_
b = model.intercept_

print(f'线性方程:Y={a1:.2f}*X1 +{a2:.2f}*X2 + {b:.2f}')

# new_X = np.array([380, 12]).reshape(-1, 2)
# predicted_Y = model.predict(new_X)
# print(f'预测新配比（水泥380kg/m³，粉煤灰12%）的混凝土强度:{predicted_Y[0]:.2f}Mpa')
# 调整粉煤灰比例以降低成本，同时保证强度≥40MPa

# 优化调整：假设水泥用量固定为380kg/m³，寻找合适的粉煤灰比例
for fly_ash in range(10, 21): # 粉煤灰比例从10%到20%
    text_X = np.array([380, fly_ash]).reshape(-1, 2)
    text_Y = model.predict(text_X)
    if text_Y >= 40:
        print(f'粉煤灰比为{fly_ash}%时，强度为{text_Y[0]:.2f}')
        break
