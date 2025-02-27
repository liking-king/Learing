import matplotlib.pyplot as plt
import pandas as pd
from sklearn.tree import DecisionTreeClassifier, plot_tree

# 模拟检测数据（6组样本）
data = {
    "抗压强度": [35, 42, 28, 38, 45, 30],
    "坍落度": [160, 180, 150, 170, 190, 155],
    "氯离子含量": [0.08, 0.05, 0.12, 0.06, 0.04, 0.10],
    "验收结果": [1, 1, 0, 1, 1, 0]  # 1=合格，0=不合格
}

df = pd.DataFrame(data)

X = df[["抗压强度", "坍落度", "氯离子含量"]]
Y = df[["验收结果"]]

model = DecisionTreeClassifier(max_depth=3)
model.fit(X, Y)

plt.rc('font', family='YouYuan')
plt.figure(figsize=(15, 8))
plot_tree(model,  feature_names=X.columns,
          class_names=["合格", '不合格'], filled=True, rounded=True)
plt.show()
