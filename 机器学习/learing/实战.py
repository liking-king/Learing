import numpy as np
"""
生成50个学生的随机成绩（40-100分）找出:
全科及格的学生数量
数学成绩前3名
"""
scores = np.random.randint(40, 100, (50, 3))
pass_all = np.all(scores>=60, axis=1)
pass_all_sum = np.sum(pass_all[True])
# print(pass_all_sum)

math_scores = scores[:,0]
math_scores_sort = np.argsort(math_scores)[::-1]
top3_math = math_scores_sort[:3]
for i , index in enumerate(top3_math):
    print(f'数学前三名成绩第{i+1}名:{math_scores[index]},'
          f'语文成绩:{scores[index, 1]}, 语文成绩:{scores[index, 2]}')
'''
1.生成随机成绩：
np.random.randint(40, 101, size=(50, 3)) 会创建一个形状为 (50, 3) 的二维 numpy 数组，其中 50 代表学生数量，3 代表三门课程（这里假设是数学、语文、英语），数组中的每个元素是 40 到 100 之间（包含 40 但不包含 101）的随机整数，作为学生的课程成绩。

2.计算全科及格的学生数量：
scores >= 60 会对 scores 数组中的每个元素进行判断，若元素大于等于 60 则返回 True，否则返回 False，得到一个布尔型的二维数组。
np.all(..., axis = 1) 沿着行的方向（axis = 1）判断每一行的元素是否都为 True，即判断每个学生的三门课程是否都及格，返回一个布尔型的一维数组。
np.sum(pass_all) 统计布尔数组中 True 的数量，也就是全科及格的学生数量

3.找出数学成绩前 3 名：
scores[:, 0] 提取所有学生的数学成绩，得到一个一维数组。
np.argsort(math_scores)[::-1] 对数学成绩进行排序，返回排序后元素的索引，[::-1] 使索引按照成绩从高到低排列。
sorted_indices[:3] 取出前 3 个索引，代表数学成绩前 3 名学生的索引。
通过循环输出这 3 名学生的三门课程成绩。
'''
"""
1.np.argsort() 是 numpy 库中的一个函数，它的作用是返回数组元素排序后的索引。
            也就是说，它不会对数组本身进行排序，而是返回一个新的数组，
            这个新数组中的元素是原数组排序后各元素在原数组中的索引位置。

2. enumerate(top_3_indices, start=1)
    enumerate() 是 Python 的内置函数，用于将一个可迭代对象（如列表、元组、字符串等）组合为一个索引序列，同时列出数据和数据的索引。
    top_3_indices 是一个包含数学成绩排名前 3 名学生索引的列表。
    start=1 是 enumerate 函数的一个可选参数，用于指定索引的起始值。默认情况下，索引从 0 开始，这里设置为 1，意味着索引从 1 开始计数。
    
3. for i, index in ...
    这是一个 for 循环，用于遍历 enumerate(top_3_indices, start=1) 返回的结果。
    i 是 enumerate 函数生成的索引，代表学生的排名，从 1 开始。
    index 是 top_3_indices 列表中的元素，即数学成绩排名前 3 名学生在 scores 数组中的索引。
    
4. print(f"第 {i} 名: 数学成绩 {math_scores[index]}，语文成绩 {scores[index, 1]}，英语成绩 {scores[index, 2]}")
    这是一个使用了 f-string 格式化的 print 语句，用于输出每个学生的排名和各科成绩。
    {i} 会被替换为当前学生的排名。
    {math_scores[index]} 会被替换为该学生的数学成绩，math_scores 是一个包含所有学生数学成绩的一维数组，index 是该学生在 math_scores 数组中的索引。
    {scores[index, 1]} 会被替换为该学生的语文成绩，scores 是一个二维数组，index 是该学生在 scores 数组中的行索引，1 表示语文成绩所在的列索引。
    {scores[index, 2]} 会被替换为该学生的英语成绩，2 表示英语成绩所在的列索引。
"""