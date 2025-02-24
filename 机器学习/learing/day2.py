import pandas as pd

# 求大风天停工的概率，先求停工的天数，在基础上求大风的天数，=
data = {
  "日期": ["1号", "2号", "3号", "4号", "5号", "6号", "7号"],
  "天气": ["晴", "大风", "大风", "晴", "雨", "大风", "雨"],
  "停工": [False, True, True, False, True, False, True]
}
df = pd.DataFrame(data)

# 停工的天数
t_day = df[df['停工']==True]
t_days = len(t_day)

# 大风的天数
d_day = t_day[t_day['天气']=='大风']
d_days = len(d_day)

# 停工的概率
prob_stop = d_days / t_days
print(prob_stop)
