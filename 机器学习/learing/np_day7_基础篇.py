import numpy as np

'''
每门课程(平均分，最高分，最低分)
每个学生(总分，平均分，排名)
总分最高学生(索引，成绩)
每门课程成绩高于该课程平均分的学生（布尔数组）
'''
scores = np.array([[85, 90, 78],
                   [70, 82, 88],
                   [92, 87, 95],
                   [65, 72, 68],
                   [88, 91, 85]])
# 每门课程(平均分，最高分，最低分)
scores_mean = np.mean(scores, axis=0)
scores_max = np.max(scores, axis=0)
scores_min = np.min(scores, axis=0)
# 每个学生(总分，平均分，排名)
student_all = np.sum(scores, axis=1)
student_mean = np.mean(scores, axis=1)
student_sort = np.argsort(student_all)[::-1]
# 总分最高学生(索引，成绩)
student_all_max = student_sort[0]
student_scores_max = scores[student_all_max]
# 每门课程成绩高于该课程平均分的学生（布尔数组）
above_mean_students = scores > scores_mean
print(above_mean_students)