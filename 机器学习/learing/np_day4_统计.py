import numpy as np

scores = np.array([[70, 71, 80],
                   [80, 90, 85],
                   [90, 85, 70]])

print(np.max(scores, axis=0))
total = np.sum(scores, axis=1)
print(total)
print(np.argsort(total)[::-1])